# 7-Minute Demo Script — AuditReady

> Use this when walking a senior at the firm through the working demo. Total runtime: ~7 minutes. Each section has the **point to make** and the **click sequence**.

The product is generically branded as "AuditReady — Working Demo" so it can be shown to anyone (customers, partners, internal stakeholders) without revealing the firm-specific positioning. The "Why this fits" page is where the strategic argument for **why this firm specifically should own this category** is made.

---

## 0:00 — Frame the opportunity (45 sec, no clicks)

> *"Two things just happened in our market. SAP's Joule HR agents go GA in May. And NYC told the Department of Consumer & Worker Protection to actually start enforcing Local Law 144 — every NYC employer using AI in hiring needs an annual independent bias audit. Penalty is up to $1,500 per day per violation. Our firm is the rare shape that can sell **both** sides of this: we implement the SuccessFactors agents, and because we are MWBE-certified and not an AI vendor, we are the auditor that LL144 actually requires. I built a working prototype — let me show you."*

Open the browser at <http://localhost:5173> (or the live URL if you've deployed it).

---

## 0:45 — Live Demo (90 sec) — THE WOW MOMENT

**Point to make:** Six AI agents do four hours of recruiter work in seconds — and every decision is logged for a regulator.

**Click sequence:**
1. You land on **Live Demo** by default.
2. Click **Use sample** — this fills both textareas with a real Senior Backend Engineer JD and a matching resume.
3. Click **Run pipeline**.
4. Narrate as the steps light up:
   - **Sourcer** extracts skills from the JD and resume in real time
   - **Screener** computes the explainable score (87–100) with breakdown
   - **Interviewer Prep** generates a tailored interview rubric
   - **Scheduler** allocates a panel slot
   - **Offer Drafter** drafts a comp-band-compliant offer letter
   - **Audit Engine** writes a hash-chained event for LL144
5. Scroll to the **Productivity Report** at the bottom: ~6 seconds of AI work vs. 47 minutes of recruiter time, 99.x% speedup, ~$294 saved per candidate, $2.94M annual at 10K candidates/year.

> *"Notice three things. First, this isn't pre-recorded — open the browser console and you can read the parsing code. Second, every score has citations: which line in the resume matched which line in the JD. Third, the audit log entry at the bottom is what makes this defensible in front of a regulator. The same data the recruiter sees, the auditor sees."*

---

## 2:15 — Bias Audit (LL144) (75 sec) — THE MOAT

**Point to make:** This is the legally-required, recurring-revenue tollbooth nobody else can credibly bid against.

**Click sequence:**
1. Click **Bias Audit (LL144)** in the sidebar.
2. Read the green hero strip: *Independent third-party AEDT bias audit · Compliant · Audit ID · methodology · next due*.
3. Point at the blue callout: *"Why this audit qualifies as 'independent'"* — explain that the law forces structural separation between auditor and AEDT vendor.
4. Show the **Selection rates by sex / race** tables — every group passes the four-fifths rule.
5. Show the **Intersectional analysis** chart (Sex × Race).
6. Show the **Cross-jurisdiction crosswalk** at the bottom — NYC LL144, EEOC, IL AIVIA, CO AI Act, EU AI Act, GDPR.

> *"One audit, mapped to every jurisdiction the customer hires in. That's how a single $130K audit retainer turns into a $400K-$600K cross-jurisdiction package over three years. And the four-fifths rule, the explainability citations, the public summary — all of it is auto-generated. We are not selling auditor labor; we are selling auditor independence plus automation."*

---

## 3:30 — AI Agents (45 sec)

**Point to make:** This is the SuccessFactors Joule story made concrete — six agents on SAP BTP + AI Core.

**Click sequence:**
1. Click **AI Agents** in the sidebar.
2. Show the agent cards (Sourcer, Screener, Interviewer, Scheduler, Offer Drafter — Audit Engine is the sixth, lives in the audit module).
3. Click **Screener** → modal opens → point at: model version pinned, SAP touchpoint = SuccessFactors Recruiting + AI Core + Provenance Log, recent decisions logged.
4. Point at the live activity feed — new events appear every ~2.5 seconds, each with a hash.

> *"Joule is the surface, BTP + AI Core is the engine. We don't replace SAP — we ride it. And the customer's data never leaves their tenant."*

---

## 4:15 — Candidates (45 sec)

**Point to make:** Recruiter workspace where every score is defensible in front of a recruiter, a candidate, and a regulator.

**Click sequence:**
1. Click **Candidates**.
2. Filter by stage = **Screened**, click any row's "Why this score?" button.
3. Drawer opens: rationale, citations, top matched skills, gaps, audit trail (sourced → screened → 10-day notice sent).

> *"Every score is explainable. Every override is logged. The recruiter override is itself a fairness signal — if one recruiter overrides agents on demographic lines, that shows up in the audit."*

---

## 5:00 — Compliance Cockpit (30 sec)

**Point to make:** Operations view for the customer's legal team.

**Click sequence:**
1. Click **Compliance**.
2. Point at: SAP integrations all green, AEDT inventory (ours audited, legacy decommission, third-party HireVue still owes an audit), tamper-evident audit log, candidate-notice delivery.

---

## 5:30 — Why this fits (90 sec) — THE CLOSE

**Point to make:** This product was *literally designed* for this firm's shape. It's not a coincidence; it's a structural fit.

**Click sequence:**
1. Click **Why this fits** in the sidebar.
2. Walk through the six numbered cards: SuccessFactors depth, AI-governance practice, MWBE/diverse-supplier status, vendor independence, Northeast presence, hybrid revenue model.
3. Show the ROI cards: **$4M annual recurring audit revenue · 10–15 net-new SF implementations · 3–5× win-rate lift**.
4. Walk through the 90-day bills-of-materials: stand up audit-practice wall → recruit 2 design partners (one NYC insurer, one city agency) → productionize on BTP + AI Core → ship Screener GA on Joule HR May 2026 → dogfood the audit on our own staff aug → cross-jurisdiction crosswalk.

> *"Two design partners, ninety days, May launch. The window is now — once the West Coast SaaS players figure out the legal posture they cannot match, this category is uncontested. We are the only firm in NYC with all five characteristics on the slide."*

---

## 7:00 — Q&A — Likely questions and answers

**"Why won't SAP just build this themselves?"**
> SAP can build the agents — they are. SAP cannot be the auditor. LL144 §20-870 forces structural separation. SAP would be auditing its own product.

**"Won't Big-4 do this?"**
> They will try. Two reasons we beat them: (1) our average MSA is one-third their price for the same audit, and (2) our SuccessFactors implementation depth means we deliver in weeks, not quarters. Independence + speed + price.

**"How big is the market actually?"**
> NYC alone: ~50K LL144-affected employers. Even capturing 200 customers at ~$130K/year per AEDT, with 1.5 AEDTs average, is ~$39M annual recurring. Add IL/CO/EU and 10× the buyer pool.

**"What's the build cost to take this from prototype to production?"**
> ~$1.2M over six months: 3 senior engineers + 1 SAP architect + 1 compliance lawyer-in-residence on retainer. Two design partners co-fund roughly half. Net: ~$600K, against a Year-1 ARR plan of $4M.

**"Demo seems too smooth — what does the production version actually look like?"**
> The Live Demo runs real skill extraction in your browser — open dev tools, the code is readable. Production replaces the in-browser scorer with a multi-agent system on SAP AI Core, the audit log with a tamper-evident store on SAP BTP, and the candidate notices with a managed delivery service. The user-experience and the audit artifacts are the same.

---

## Reset before the demo

- Hard-refresh the page (Cmd+Shift+R) to reset state.
- The Live Demo page lands first; you don't have to click anything to start.
- If the live activity feed gets too noisy mid-demo, just navigate away and back — it reseeds.

## After the demo

- Send the live URL (Netlify/Vercel) plus the PRD PDF.
- Two follow-ups: (1) a 30-min architecture deep-dive, (2) a 60-min go-to-market session listing the first 10 NYC accounts to call.
