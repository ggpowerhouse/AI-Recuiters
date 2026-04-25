# NYC Local Law 144 — Public Summary Template

> Per NYC Administrative Code §20-870 et seq. (AEDT). This is the document an employer is **required to publish on their website** in a clearly-labeled location prior to using an AEDT for any hiring or promotion decision involving an NYC-based role.

---

## [Employer Name] — AEDT Bias Audit Public Summary

**Employer:** [Legal Entity Name]
**AEDT Audited:** TalentMesh Screener Agent (model version `screener-v3.2`)
**AEDT Vendor:** Sedna Consulting Group (TalentMesh by Sedna)
**Independent Auditor:** Sedna Audit Practice (a separately-walled unit)
**Audit Methodology:** EEOC Title VII / Uniform Guidelines on Employee Selection Procedures (1978) — four-fifths rule
**Audit Period:** [YYYY-MM-DD] to [YYYY-MM-DD] (rolling 12 months)
**Audit Date:** [YYYY-MM-DD]
**Next Required Audit:** [YYYY-MM-DD] (within one year)
**Data Source:** Anonymized application + decision events from Employer's SAP SuccessFactors tenant

---

### 1. Categories evaluated

| Category | Source |
|---|---|
| Sex (Male / Female / Non-binary / Prefer not to say) | Self-reported, voluntary |
| Race / Ethnicity (EEOC standard categories) | Self-reported, voluntary |
| Intersectional combinations (Sex × Race/Ethnicity) | Computed |

---

### 2. Applicant counts

| | Applicants | Selected for next stage |
|---|---:|---:|
| Total | [N] | [n] |
| Male | [N] | [n] |
| Female | [N] | [n] |
| White | [N] | [n] |
| Black or African American | [N] | [n] |
| Hispanic or Latino | [N] | [n] |
| Asian | [N] | [n] |
| Native Hawaiian / Pacific Islander | [N] | [n] |
| American Indian / Alaska Native | [N] | [n] |
| Two or more races | [N] | [n] |
| Sex unknown | [N] | [n] |

*Categories with fewer than 2% of total applicants are flagged but not used for impact-ratio computation per EEOC guidance.*

---

### 3. Selection rates

```
selection_rate(group) = selected(group) / applicants(group)
```

| Group | Selection rate |
|---|---:|
| Male | [%] |
| Female | [%] |
| White | [%] |
| Black or African American | [%] |
| Hispanic or Latino | [%] |
| Asian | [%] |
| ... | ... |

---

### 4. Impact ratios (four-fifths rule)

```
impact_ratio(group) = selection_rate(group) / selection_rate(reference_group)
```

Reference group = the group with the **highest** selection rate.
**Adverse-impact threshold:** impact ratio < 0.80 indicates potential adverse impact.

| Group | Impact ratio | Status |
|---|---:|---|
| Male | [r] | ✅ / ⚠️ |
| Female | [r] | ✅ / ⚠️ |
| ... | ... | ... |

---

### 5. Intersectional analysis

Per LL144, selection rates and impact ratios are also computed for each Sex × Race/Ethnicity combination.

| Intersection | Selection rate | Impact ratio | Status |
|---|---:|---:|---|
| Female × Black | [%] | [r] | ✅ / ⚠️ |
| Male × Hispanic | [%] | [r] | ✅ / ⚠️ |
| ... | ... | ... | ... |

---

### 6. Auditor's conclusion

[One paragraph signed by the independent auditor stating whether the AEDT, on the audit data, meets the four-fifths rule and noting any flagged groups requiring monitoring.]

---

### 7. Candidate notice

NYC residents are notified at least **10 business days** before assessment that an AEDT will be used. The notice includes:
- The AEDT used and qualifications evaluated,
- Categories of data collected and retention period,
- A link to this Public Summary,
- Instructions to request an alternative selection process.

To request an alternative selection process, contact: [recruiting-accommodations@employer.example]

---

### 8. Document fingerprint

- **Audit ID:** `AEDT-AUDIT-[YYYY-MM]-[hash]`
- **SHA-256 of underlying log:** `[hex]`
- **Auditor signature:** Sedna Audit Practice — [Lead Auditor Name, credentials]

---

*This summary is provided in compliance with New York City Local Law 144 of 2021 (Int. 1894-2020). For full methodology, contact the auditor.*
