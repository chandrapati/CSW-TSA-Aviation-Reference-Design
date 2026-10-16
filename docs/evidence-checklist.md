# TSA Aviation (Joint EA 23-01) — CSW Evidence Checklist

Recurring evidence pack for TSA-regulated aircraft operators (49 CFR part 1544) and airport operators (part 1542) covered by Joint Emergency Amendment 23-01.

> **Re-key this to your own plan before use.** EA 23-01 is Sensitive Security Information (49 CFR 1520.5(b)); its provision numbering is not public and is not used here. The groupings below follow the **four measures TSA described publicly** plus the plan obligations in the public appellate record. **TSA inspects against your approved Cybersecurity Implementation Plan**, so replace these headings with your CIP's own measure references.
>
> **Treat every completed pack as SSI** once it is incorporated into a plan, assessment, or submission.

---

## Quarterly pack

### Critical systems identification

- [ ] **1.** Inventory export, filtered to `compliance:tsa-aviation`, with `ccs_id`, `ccs_function`, `zone`, `ops_disruption_impact`
- [ ] **2.** Agent coverage report — percentage of in-scope workloads instrumented, with documented exceptions
- [ ] **3.** Scope-membership delta report since the last pack — the record that the list stays current as the estate changes
- [ ] **4.** `TSA-Designated-Critical` filter export — keeps systems TSA designated separable from those you identified

### Measure 1 — Network segmentation

- [ ] **5.** ADM dependency map for the flight-operations and PSS tiers, refreshed within 90 days
- [ ] **6.** Interdependency enumeration, generated from observed flows rather than drawn by hand
- [ ] **7.** External-connection list: `Industry-Network-Connections` export (SITA / ARINC, GDS, interline, codeshare) plus `Ground-Handler-Access`
- [ ] **8.** Policy workspace snapshot showing default-deny between zones with per-rule business justification
- [ ] **9.** Denied Connections log for the quarter, scoped to critical-system zones
- [ ] **10.** **Bidirectional negative-test record** — a blocked attempt *into* the operational core and a blocked attempt *out of* it, both timestamped. The "and vice versa" half of Measure 1; the most commonly missing artifact
- [ ] **11.** `Plaintext-Crossing-Zones` export, with each finding either remediated or recorded as a gap with a compensating control

### Measure 2 — Access control

- [ ] **12.** `Privileged-Access-Paths` policy export — which sources may reach critical systems administratively, on which ports
- [ ] **13.** Denied Connections filtered to administrative protocols (tcp/22, tcp/3389, tcp/5985)
- [ ] **14.** `managed_by` label export — every workload a ground handler, MSSP, or GDS touches
- [ ] **15.** ADM review for undocumented administrative reachability

### Measure 3 — Continuous monitoring and detection

- [ ] **16.** Flow telemetry sample with process attribution, demonstrating continuous visibility
- [ ] **17.** Policy-violation and unmatched-flow history — the baseline-deviation record
- [ ] **18.** Workload drift history (process and package changes) for critical systems
- [ ] **19.** SIEM integration evidence — sample forwarded events with timestamps

### Measure 4 — Unpatched system risk

- [ ] **20.** Vulnerability inventory filtered to `ccs_id`
- [ ] **21.** `KEV-Exposed-CCS` export — CISA KEV presence **plus** reachability, which is what makes prioritization risk-based
- [ ] **22.** Compensating-control policy export for workloads that cannot be patched

### Change control and governance

- [ ] **23.** Administration audit log — who changed policy, when
- [ ] **24.** Exception register with owner and review date
- [ ] **25.** **CIP change-control classification** for any policy change this quarter: improvement that does not conflict with the approved program, or a change requiring TSA approval? Record the reasoning (see §8.3 of the design)

---

## Annual — effectiveness assessment pack

The annual obligation is to assess whether measures **work**, not that they exist. Build this pack from the effectiveness artifacts and cite the implementation artifacts as context.

**Effectiveness evidence (lead with these):**

- [ ] **26.** Simulation report from the most recent policy change — shows the measure was assessed before enforcement
- [ ] **27.** Full-year Denied Connections summary, by zone pair
- [ ] **28.** Bidirectional negative-test records for the year
- [ ] **29.** Pre-staged isolation workspace test record, with the time taken to apply
- [ ] **30.** Drift and deviation trend — is the baseline getting cleaner or noisier?
- [ ] **31.** Exception closure rate and ageing

**Implementation context (cite, don't lead):**

- [ ] **32.** Current policy workspace snapshot
- [ ] **33.** Current inventory and scope reconciliation
- [ ] **34.** Current ADM topology as the as-built architecture input

---

## Assembly notes

**Cadence.** Quarterly binder, dated. ADM refreshed every 90 days. Effectiveness pack assembled annually ahead of the assessment submission.

**Mapping.** Every artifact above should carry your CIP measure reference in the binder index. An evidence pack keyed only to the four public measures will not survive an inspection working from your plan.

**Scope the exports.** Filter everything to `compliance:tsa-aviation` so the pack covers the EA boundary and nothing else. For operators holding both part 1544 and part 1542 obligations, split by `security_program` — the two programmes are amended and inspected separately.

**Boundary statement.** Include a standing page naming what the pack does *not* evidence: MFA and identity, patch deployment, encryption, endpoint and user-behaviour detection, physical security, CISA incident reporting, the CIRP, aircraft systems, airport OT field devices, and endpoint fleets. Volunteering the boundary reads as competence; having an inspector discover it does not.

**SSI.** Mark, store, and transmit the completed pack under 49 CFR part 1520.
