# TalentMesh — Technical Architecture

> Reference architecture for the production system. The prototype in `prototype/` is a UI-only mock to show the senior — production is what's described below.

---

## 1. High-level system diagram (text)

```text
                 ┌────────────────────────────────────────────────────────────────┐
                 │                       SAP BTP (Customer Tenant)                │
                 │                                                                │
   Recruiter ──▶ │  SAP Joule  ──▶  Joule Agentic Runtime                         │
   (Joule UI)    │                       │                                        │
                 │                       ▼                                        │
                 │  ┌──────────────────────────────────────────────────────────┐ │
                 │  │           TalentMesh Multi-Agent Orchestrator            │ │
                 │  │  Sourcer → Screener → Interviewer → Scheduler → Offer    │ │
                 │  └──────────────────────────────────────────────────────────┘ │
                 │                       │                                        │
                 │                       ▼                                        │
                 │  SAP AI Core   ◀──▶   Foundation Models (customer choice)     │
                 │  + AI Launchpad        (GPT-class, Claude-class, on-prem)     │
                 │                       │                                        │
                 │                       ▼                                        │
                 │  SAP Knowledge Graph  ◀──▶  Skills Ontology + Job Profiles    │
                 │                       │                                        │
                 └───────────────────────┼────────────────────────────────────────┘
                                         │
                ┌────────────────────────┼─────────────────────────┐
                ▼                        ▼                         ▼
   ┌──────────────────────┐ ┌──────────────────────┐ ┌──────────────────────┐
   │ SuccessFactors       │ │ S/4HANA HR           │ │ AuditReady AEDT      │
   │ Recruiting · EC ·    │ │ Compensation · Org   │ │ (independent module) │
   │ Onboarding · Time    │ │                      │ │ Tamper-evident logs  │
   └──────────────────────┘ └──────────────────────┘ │ Bias-audit engine    │
                                                     │ LL144 / AIVIA / EEOC │
                                                     └──────────────────────┘
                                                              │
                                                              ▼
                                                   Sedna Audit Practice
                                                   (independent sign-off)
```

---

## 2. Component breakdown

### 2.1 Frontend surfaces
- **SAP Joule** — primary recruiter chat surface (built into S/4 / SuccessFactors)
- **TalentMesh Web App** (SAP Build Apps + Fiori) — Recruiter Workspace, Compliance Cockpit, Executive Dashboard
- **Candidate Portal** — public-facing notice + alternative-selection request

### 2.2 Orchestration
- **Multi-Agent Orchestrator** — runs on SAP BTP Cloud Foundry / Kyma; uses SAP AI Core for model invocations; delegates per-agent tasks; maintains a **shared state graph** so agents pass context.
- Implementation: TypeScript service using a deterministic state machine + LangGraph-style agent nodes; no agent has direct DB write — every write goes through a guard layer that produces an audit event.

### 2.3 The five agents
| Agent | Inputs | Outputs | Tools |
|---|---|---|---|
| Sourcer | Open req, JD, target persona | Ranked candidate list (50–200) | LinkedIn API, GitHub, internal alumni DB, Knowledge Graph |
| Screener | Resume + responses + req | Score (0–100) + rationale + citations | LLM via AI Core; SF Recruiting fields |
| Interviewer | Approved candidate + rubric | Transcript + rubric scores | Joule chat or Google Meet; Whisper-class STT |
| Scheduler | Interviewer panels + candidate availability | Booked slots | Outlook/Google Calendar; SF interview blocks |
| Offer Drafter | Approved candidate + req + comp band | Offer letter draft | S/4 HR comp tables; SF Compensation; DocuSign |

### 2.4 Audit core
- **Tamper-evident event log** — append-only; each event hash-chained to predecessor.
- **Bias audit engine** — computes selection rate, scoring rate, impact ratios, four-fifths rule, intersectional cells, scoring distribution by group.
- **Report renderer** — produces (a) Independent Auditor's Report PDF, (b) Public Summary HTML/PDF, (c) machine-readable JSON for regulators, (d) candidate notice templates.
- **Reproducibility** — given raw event log + audit config, audit re-runs to byte-identical output.

### 2.5 Identity, security, compliance
- **AuthN/AuthZ:** SAP IAS + customer's IdP (SAML/OIDC); RBAC enforced in BTP.
- **Data residency:** customer-tenant data stays in customer BTP; Sedna audit practice receives a **read-only attestation feed**, never raw PII.
- **Encryption:** TLS 1.3 in transit; AES-256-GCM at rest; secrets in SAP Credential Store / customer KMS.
- **PII minimization:** no candidate PII in logs that leave the customer tenant.
- **No log of:** passwords, SSNs, full DOB, biometric data.
- **Audit trail:** all agent decisions + recruiter overrides + admin actions; immutable.
- **DPIA / GDPR / CCPA:** templates included; data subject access request (DSAR) endpoint.

---

## 3. Data model (audit-relevant subset)

```text
RequisitionEvent { req_id, jd_hash, opened_at }
CandidateEvent   { candidate_id (pseudonymized), req_id, source, applied_at }
AgentDecision    { decision_id, candidate_id, agent_type, action,
                   score, rationale_hash, model_version, prompt_hash,
                   prev_event_hash, this_event_hash, ts }
RecruiterOverride{ override_id, decision_id, reason_code, free_text_hash, ts }
DemographicSelf  { candidate_id, sex, race, ethnicity, intersectional_key }
                 (always self-reported, optional, stored separately)
NoticeEvent      { candidate_id, notice_type, sent_at, channel }
```

The bias-audit engine joins `AgentDecision` + `DemographicSelf` only for aggregate computation — never for per-candidate disclosure.

---

## 4. SAP integrations (what we touch)

| SAP product | Read | Write |
|---|---|---|
| SuccessFactors Recruiting | Reqs, applications | Candidate stage, scores, notes |
| SuccessFactors EC | Org, manager, location | New-hire records (post-offer) |
| SuccessFactors Onboarding 2.0 | — | Trigger onboarding |
| SuccessFactors Compensation | Comp bands | — |
| S/4HANA HR | Org structure | — |
| SAP AI Core / AI Launchpad | Model registry | Model invocations |
| SAP Knowledge Graph | Skills ontology | Custom skill nodes |
| SAP Joule | Conversational surface | — |
| SAP BTP Build Process Automation | — | Approval workflows |
| SAP GRC | — | Segregation-of-duties on overrides |

---

## 5. Deployment

- **Customer-tenant BTP install** — clean-core, SAP-managed.
- **Single-tenant audit DB** — runs in customer subaccount; Sedna audit practice has read-only attestation access.
- **CI/CD** — gitOps; signed releases; SBOM published per release.
- **Observability** — OpenTelemetry → SAP Cloud ALM + customer SIEM.
- **DR** — 99.95% target; cross-region replicas for audit log.

---

## 6. Open architectural decisions

1. Bias-audit module — tightly coupled to TalentMesh, or shipped as a separable "AuditReady" SKU that can audit Workday/Greenhouse/Eightfold? (Recommend: separable, sold standalone too.)
2. Where does `DemographicSelf` live — customer SF tenant only, or a dedicated bias-audit subaccount with extra access controls? (Recommend: dedicated subaccount.)
3. Model strategy — single SAP-blessed foundation model, or customer-choice via AI Core? (Recommend: customer-choice; simplifies regulated-industry sales.)
4. White-label — can a customer rebrand TalentMesh? (Recommend: yes; Sedna brand stays on the audit report only.)
