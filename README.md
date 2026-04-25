# AuditReady — Working Demo

> **Agentic hiring on SAP SuccessFactors, with an independent NYC Local Law 144 bias audit built in.**

A working prototype + product brief that combines two high-conviction ideas:

| | Idea | What it is |
|---|---|---|
| **A** | **TalentMesh** | Multi-agent AI hiring stack (Sourcer → Screener → Interviewer → Scheduler → Offer Drafter) embedded in SAP SuccessFactors + Joule. |
| **B** | **AuditReady AEDT** | Independent NYC Local Law 144 bias-audit-as-a-service. Recurring annual revenue. Auditor-independence moat. |

**The product fuses the two:** every hiring decision the agents make is automatically captured into an audit-ready evidence pack — customers buy the hiring platform *and* the compliance tollbooth in one motion.

The Live Demo page lets a viewer **paste any job description and any resume**, then watch six AI agents execute the full screening pipeline in their browser, in real time, with every decision logged for audit. No backend. No build step. No setup.

---

## What's in this folder

```text
SAP/
├── README.md                  ← this file
├── docs/
│   ├── PRD.md                 ← full Product Requirements Document
│   ├── architecture.md        ← technical architecture + SAP integrations
│   ├── ideas-summary.md       ← 11 ideas across both research passes
│   ├── demo-script.md         ← 7-minute demo script
│   └── deployment.md          ← drag-and-drop deploy guide (Netlify, Vercel, GH Pages)
├── compliance/
│   └── ll144-public-summary-template.md   ← LL144-mandated public summary template
└── prototype/
    ├── index.html             ← THE deployable artifact (single file, ~125 KB, zero deps)
    └── start.sh               ← one-command launcher (python http.server)
```

The prototype is **one HTML file**. Drop it on any static host and you have a live demo URL.

---

## Run locally (60 seconds)

```bash
cd SAP/prototype
./start.sh           # or: python3 -m http.server 5173
```

Open <http://localhost:5173>. Done. No Node, no npm, no build step.

## Deploy live

Drag `prototype/` onto **<https://app.netlify.com/drop>** for a public HTTPS URL in 30 seconds. See `docs/deployment.md` for Vercel, GitHub Pages, and Cloudflare Pages walkthroughs.

---

## What to show, in what order

1. **Live Demo** (default landing) — paste sample JD + resume → run pipeline → six agents execute → score, citations, rubric, offer draft, audit log → productivity report shows time + cost saved.
2. **Bias Audit (LL144)** — independent third-party audit page; four-fifths rule; intersectional analysis; cross-jurisdiction crosswalk (NYC → IL → CO → EU).
3. **Why this fits** — strategic brief on which firm profile this product was built for. Use this to close the conversation.

---

## Why this product is the right shape for an SAP-anchored consultancy with an AI-governance practice

Five structural reasons (covered in detail on the Why-this-fits page in the demo):

1. **SuccessFactors implementation depth** — agents deploy on top of the stack you already deliver.
2. **AI-governance practice already on the menu** — turn advisory hours into a recurring product.
3. **MWBE / diverse-supplier status** — preferred procurement status for NYC, NYS, federal, and Fortune 500 RFPs.
4. **Independence from any AI tool vendor** — LL144 §20-870 requires the auditor to be structurally independent of the AEDT vendor. A consultancy that doesn't make its own AI hiring tool is, by definition, independent. That is the structural moat.
5. **Northeast presence + 20+ years of consulting credibility** — NYC/NJ tri-state has the densest concentration of LL144-affected employers in the country.

