# Product Requirements Document — TalentMesh by Sedna

**Version:** 0.1 (Prototype Draft) · **Owner:** Sedna Consulting Group · **Date:** April 2026

---

## 1. Executive summary

**TalentMesh by Sedna** is an agentic hiring product for enterprises on SAP SuccessFactors. It bundles a 5-agent recruiting crew with the **independent NYC Local Law 144 bias audit** every employer using AI in hiring is now legally required to commission annually.

We are uniquely positioned to win this category because Sedna is:
- A **certified MWBE** (independent of any AI tool vendor — exactly what LL144 requires of the auditor),
- A **20-year SAP implementation partner** with deep SuccessFactors muscle (Time, Payroll, Attendance, Onboarding, EC),
- An **AI Governance practice** already on the services menu.

We are riding three concurrent tailwinds:

| Tailwind | Source | Why it matters |
|---|---|---|
| SAP Joule HR agents go GA **May 2026** | SAP Sapphire 2025; SAP News, Mar 2026 | Customers will need certified implementers immediately. |
| NYC Local Law 144 enforcement is ramping | NY State Comptroller, Dec 2025 audit | DCWP told to enforce; $500–$1,500/day per violation. |
| Cross-jurisdiction expansion: IL AIVIA, CO AI Act, EU AI Act | Active 2025–2026 | Audit demand becomes recurring across the US. |

---

## 2. Problem statement

### 2.1 The hiring problem (why customers buy)
Enterprises on SuccessFactors typically take 45–90 days to fill a role at a fully-loaded cost of $4,700–$8,500 per hire. The bottleneck is not lack of applicants — it is **manual triage**: recruiters spend ~70% of their time on resume review, scheduling, and screening, not on the human judgment work that matters.

### 2.2 The compliance problem (why customers must buy)
NYC Local Law 144 prohibits using any **Automated Employment Decision Tool (AEDT)** on NYC-based roles unless the employer:
1. Commissions an **independent bias audit** within the last year,
2. Publishes a public summary on the company website,
3. Provides candidates with **10 business days' notice** before assessment.

Violations: **$500–$1,500 per violation per day**. The NY State Comptroller's December 2025 audit found NYC DCWP enforcement "ineffective" and ordered a ramp-up. Illinois AIVIA, Colorado AI Act, and the EU AI Act add overlapping obligations.

The market reality: **almost every Fortune 500 in NYC is non-compliant or under-compliant today.**

### 2.3 Why Sedna specifically
| Requirement | Sedna fit |
|---|---|
| Auditor must be independent of the tool vendor | ✅ Sedna is not an AI tool vendor |
| MWBE/diverse-supplier preference in many RFPs | ✅ Certified MWBE |
| SuccessFactors implementation depth | ✅ 20+ years; certified module leads |
| AI Governance practice | ✅ Already a stated Sedna service line |
| US + India 24×7 delivery | ✅ Existing GCC model |

---

## 3. Goals & non-goals

### 3.1 Goals (what this product is)
- **G1.** Reduce time-to-fill by ≥ 50% for SuccessFactors customers.
- **G2.** Reduce cost-per-hire by ≥ 40%.
- **G3.** Generate audit-ready LL144 evidence on every hiring decision automatically — no separate tooling.
- **G4.** Deliver an **annual independent bias audit** as a recurring SKU, valid for NYC LL144, IL AIVIA, CO AI Act, and EEOC alignment.
- **G5.** Become the default Sedna offering for SuccessFactors + Joule customers in regulated industries.

### 3.2 Non-goals (what this product is *not*)
- Not a standalone ATS — we sit on top of SAP SuccessFactors / SmartRecruiters.
- Not a recruiting agency for non-SAP startups (that is a separate Sedna offering — "FoundersDesk", see `ideas-summary.md` Idea 2).
- Not a model-training platform — we use SAP AI Core + customer-approved foundation models.

---

## 4. Target users & buyers

| Persona | What they care about | How TalentMesh helps |
|---|---|---|
| **Chief Human Resources Officer (CHRO)** | Time-to-fill, cost-per-hire, compliance risk, employer brand | Automates 70% of the funnel; ships LL144 audit for free |
| **Head of Talent Acquisition** | Recruiter productivity, candidate experience | Recruiters move from data-entry to relationship work |
| **General Counsel / Chief Compliance Officer** | EEOC, LL144, AIVIA, EU AI Act exposure | Independent third-party audit; immutable evidence pack |
| **CIO / SAP Lead** | Clean-core SAP, BTP-native, no shadow IT | Deployed in SAP BTP + AI Core; uses Joule's agentic runtime |
| **CFO** | ROI, recurring spend justification | Subscription + per-hire; audit retainer is annual |

---

## 5. The product (5 modules)

### 5.1 Module A — The 5-Agent Hiring Crew (TalentMesh)
A multi-agent system orchestrated on SAP BTP + AI Core, surfaced through SAP Joule. All five agents write back to SuccessFactors Recruiting / Employee Central / Onboarding 2.0.

| # | Agent | What it does | SAP touchpoint |
|---|---|---|---|
| 1 | **Sourcer** | LinkedIn / GitHub / alumni DB; skills-graph match (not keyword) | SuccessFactors Recruiting; SAP Knowledge Graph |
| 2 | **Screener** | Reviews resume + responses; produces **explainable** score with citations | SF Recruiting; AI Core; full provenance log |
| 3 | **Interviewer** | First-round structured interview (text or video, optional); rubric-scored | Joule chat surface; can join Google Meet |
| 4 | **Scheduler** | Books panel interviews across time zones | SF + Outlook/Google Calendar |
| 5 | **Offer Drafter** | Pulls comp band from S/4HANA HR + SF Compensation; drafts letter; routes for approval | S/4 HR, SF Compensation, DocuSign |

### 5.2 Module B — Bias Audit Engine (AuditReady AEDT)
The compliance core. Continuously logs every agent decision into a tamper-evident store, computes:
- **Selection rate** by sex, race/ethnicity, and intersectional combinations.
- **Impact ratios** vs. the most-selected group.
- **Four-fifths rule** pass/fail per LL144 (impact ratio < 0.80 = adverse-impact flag).
- **Scoring rate** for screeners that produce continuous scores.

Output artifacts (auto-generated, downloadable):
- **Public Summary** (the file LL144 requires posted on the employer's website).
- **Independent Auditor's Report** (Sedna-signed PDF).
- **Candidate Notice template** (10-business-day pre-assessment notice).
- **Cross-jurisdiction crosswalk**: NYC LL144, IL AIVIA, CO AI Act, EU AI Act, EEOC Title VII.

### 5.3 Module C — Compliance Cockpit
Operations view for legal / compliance teams:
- Real-time AEDT inventory across the company,
- Audit cadence tracker (which tools are due for re-audit),
- Candidate notice delivery log (10-day rule evidence),
- SAP integration health (SuccessFactors, S/4, BTP, Joule, AI Core).

### 5.4 Module D — Recruiter Workspace
Day-to-day surface for TA team:
- Candidate list with explainable AI score,
- "Why this score?" drawer (top matched skills, gaps, agent reasoning trace),
- Manual override (override is also logged for audit).

### 5.5 Module E — Executive Dashboard
KPI strip + funnel + agent productivity + compliance health for CHROs / CIOs.

---

## 6. Compliance design (the moat)

LL144 is unforgiving on auditor independence. We design for it:

1. **Auditor independence wall** — the bias-audit module is delivered by **Sedna's Audit Practice**, organizationally separated from Sedna's Implementation Practice (mirrors Big-4 audit/consulting separation).
2. **Tamper-evident logs** — every agent decision is hashed and chain-linked (no LLM gets to overwrite history).
3. **Reproducibility** — all audits are reproducible from raw logs to public summary, end-to-end.
4. **Notice automation** — 10-business-day pre-assessment candidate notice is sent by the system, not the recruiter.
5. **Override accountability** — recruiter overrides are logged with reason; auditor sees override rate as a fairness signal.
6. **Cross-jurisdiction templates** — one audit package satisfies NYC LL144 + EEOC alignment, with optional IL AIVIA and CO AI Act add-ons.

---

## 7. Key user journeys

### 7.1 Journey 1 — "Open a requisition, fill it in 14 days"
1. Hiring manager opens a req in SuccessFactors.
2. **Sourcer agent** delivers 50 candidates within 2 hours.
3. **Screener agent** produces ranked shortlist with explainable scores.
4. Recruiter reviews top 10 in the Recruiter Workspace; approves 5.
5. **Scheduler agent** books panel interviews.
6. **Interviewer agent** runs first-round screening.
7. **Offer Drafter agent** drafts offer; recruiter sends.
8. Onboarding 2.0 takes over.

Every step is logged into the bias-audit store automatically.

### 7.2 Journey 2 — "Annual LL144 audit"
1. Compliance lead opens the Bias Audit page.
2. Selects audit period (rolling 12 months) and AEDT (the Screener agent).
3. System computes selection rates + impact ratios + four-fifths rule across protected categories and intersectional combinations.
4. Auditor's report and Public Summary are generated.
5. Sedna's Audit Practice signs the report (independent).
6. Compliance lead publishes the Public Summary to the employer's website.
7. Candidate notices are auto-issued going forward (10-day rule).

### 7.3 Journey 3 — "Candidate exercises rights"
1. NYC-based candidate receives 10-day pre-assessment notice via email.
2. Notice includes: AEDT in use, qualifications evaluated, data collected, retention period, link to Public Summary, opt-out path.
3. Candidate may request alternative selection process.
4. Choice is logged. No retaliation possible — system enforces alternative path.

---

## 8. Metrics & success criteria

### 8.1 Customer-facing KPIs
- **Time-to-fill** ↓ ≥ 50%
- **Cost-per-hire** ↓ ≥ 40%
- **Recruiter productivity** (reqs per recruiter) ↑ ≥ 2×
- **Candidate NPS** ≥ 60
- **LL144 compliance** = 100% of in-scope NYC roles

### 8.2 Sedna business KPIs
- 10 SAP SuccessFactors customers signed in FY27,
- $4M ARR from audit retainers by end of FY27,
- 25% attach rate from SF implementations to TalentMesh.

---

## 9. Pricing (working hypothesis)

| SKU | Price | Notes |
|---|---|---|
| **TalentMesh Platform** | $50–$150 per agent-hire | Volume-tiered |
| **Implementation** | $200K–$1.5M | Sedna SF/BTP services |
| **AuditReady Annual Bias Audit** | **$25K–$150K** per AEDT, per year | **Recurring revenue tollbooth** |
| **Cross-jurisdiction add-on** | +$10K–$40K | IL AIVIA, CO AI Act, EU AI Act |
| **Managed compliance ops** | $8K–$25K / mo | Notices + retainer audit |

---

## 10. Risks & mitigations

| Risk | Mitigation |
|---|---|
| SAP Joule changes APIs post-GA | Build BTP-native; abstraction layer; SAP partner status |
| Customer wants Workday, not SAP | Phase 2 connector; bias-audit module is platform-agnostic |
| Big-4 enters audit market | Compete on MWBE, NYC presence, vertical depth (SLED, life sciences, insurance) |
| LL144 amended | Audit engine is rules-as-config; legal counsel on retainer |
| LLM hallucination in screener | Explainability + citations + provenance; recruiter override is a feature, not a bug |
| EEOC challenge on a hire | Tamper-evident log + Sedna-signed independent audit = strongest defensible evidence |

---

## 11. Roadmap (90 / 180 / 365)

### 11.1 First 90 days — Beachhead
- Lock SAP partner status updates for Joule + AI Core,
- Recruit launch design partners: 2 NYC insurers, 1 NYC hospital, 1 NYC city agency,
- Ship audit engine (LL144 only) + Recruiter Workspace MVP,
- Sedna dogfoods the audit on its own staff aug pipeline (proof point).

### 11.2 180 days — Production GA
- Joule integration GA path,
- Full 5-agent crew (Sourcer + Screener + Interviewer + Scheduler + Offer Drafter),
- Cross-jurisdiction module: IL AIVIA, CO AI Act,
- 5 paying customers,
- White-label audit report.

### 11.3 365 days — Expansion
- EU AI Act conformity package,
- Workday / Greenhouse / Eightfold / Paradox / HireVue connectors (audit-only),
- "Audit-as-a-Service" sold standalone (without TalentMesh) to non-SAP shops,
- Multi-tenant SaaS option for mid-market.

---

## 12. Open questions

1. Does Sedna stand up a separate "Sedna Audit Services" legal entity to harden auditor independence?
2. Do we co-market with SAP as a Joule partner from day 1 or stay neutral?
3. Which design partner do we approach first — public sector (highest moat) or insurance (highest volume)?
4. Do we offer the audit module to non-Sedna-implemented SuccessFactors customers (channel risk vs. revenue)?
5. Pricing: per-AEDT or per-employee-band — which do customers actually buy?

---

## 13. References

- SAP. *Joule Agents | AI Use Cases for Every Business Function.* sap.com/products/artificial-intelligence/ai-agents
- SAP News. *SmartRecruiters for SAP SuccessFactors: AI-Driven Hiring.* Mar 2026
- NYC DCWP. *Local Law 144 — Automated Employment Decision Tools.*
- NY State Comptroller. *Enforcement of Local Law 144.* Dec 2025
- EEOC. *Algorithmic Fairness Under Title VII.* 2023
- Y Combinator W26 batch — Agentin AI, Ressl AI, ERPure.AI, Pollinate, FullSeam
- Gartner. *Top Trends for Chief Procurement Officers, 2025.* — agentic AI #1
