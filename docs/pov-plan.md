# TSA Aviation (Joint EA 23-01) — CSW Proof-of-Value Plan

Phased plan for a CSW proof of value with a TSA-regulated aircraft operator (49 CFR part 1544) or airport operator (part 1542) covered by Joint Emergency Amendment 23-01.

> **Two framing constraints before you start.**
>
> **The EA is SSI.** You will not be shown the requirement text, and you should not ask for it. Scope the PoV against the **four publicly described measures** and the customer's own Cybersecurity Implementation Plan structure, which the customer maps internally. Build the mapping step into the plan (Phase 0) rather than discovering it at the evidence review.
>
> **The CIP is part of an approved security program.** Enforcement changes may be change-controlled (see §8.3 of the design). Confirm in Phase 0 whether the PoV can enforce at all, or whether it must stay in simulation — this single question determines what the PoV can prove.

---

## Phase 0 — Qualification and framing (week 0)

Do this before any technical work.

- [ ] Confirm the customer's security program is **designated as covered** by the EA. This comes from their TSA principal security inspector, not from us
- [ ] Confirm whether a **revision or successor** to EA 23-01 applies — not publicly answerable, so ask
- [ ] Identify which part the assets fall under: **1544** (aircraft operator), **1542** (airport operator), or both
- [ ] Name the customer-side person with **authorized EA access** who will map our capability rows to real provisions and to their CIP
- [ ] **Change-control determination:** can the PoV enforce policy, or must it remain in simulation? Get this in writing from the compliance owner
- [ ] Set the boundary explicitly in the kickoff: **no aircraft, no airport OT field devices, no endpoint fleets** (§1.3 of the design). Do this in the first meeting, not the last
- [ ] Agree the success criteria below

**Qualification signal.** If the customer cannot name who holds the EA and the CIP, the engagement is not ready — the evidence will have nothing to map to.

---

## Phase 1 — Coverage (weeks 1–2)

**Goal:** every in-scope ground IT workload visible in CSW.

- [ ] Agents deployed to the pilot population; cloud connectors for cloud-resident systems
- [ ] Labels applied: `compliance:tsa-aviation`, `ccs_id`, `ccs_function`, `zone`, `ops_disruption_impact`, `tsa_designated`, `managed_by`, `security_program`, `station`
- [ ] Scope tree built to mirror the zone model in the customer's CIP — **not** this design's default tree, if the two differ
- [ ] Reconcile CSW scope membership against the customer's submitted critical-systems list; export the delta

**Deliverable:** inventory export, agent coverage report, and the scope-membership delta.

**The delta is the headline.** Given that TSA may designate systems the operator did not identify, a reconciliation showing workloads present in the estate but absent from the submitted list is immediately valuable — and it is usually the moment the customer understands what discovery-driven scoping buys them.

**Pilot selection.** Start with **flight operations** for an airline (dispatch, flight following, planning, crew): highest inspection salience, clearest operational-disruption story, and a population small enough to instrument in two weeks. For an airport operator, start with the **server tier** behind baggage handling or access control management — and be explicit that the field devices are out of reach.

---

## Phase 2 — Baseline (weeks 3–5)

**Goal:** a machine-generated dependency map the customer trusts.

- [ ] ADM running across the pilot tier for **at least 30 days** — see the note below
- [ ] Interdependencies enumerated from observed flows
- [ ] External connections enumerated, with particular attention to **SITA / ARINC messaging, GDS, interline and codeshare** paths
- [ ] `Plaintext-Crossing-Zones` run, including legacy aviation messaging
- [ ] System and application owners sign the cluster-to-system mapping

**Deliverable:** ADM topology, interdependency list, external-connection list, cleartext findings.

**Why 30 days, not two weeks.** Airline traffic is schedule-driven and seasonal, and **irregular operations generate flows that never appear in a normal week** — recovery tooling, crew re-assignment, re-accommodation, diversion handling. A baseline built on two clean weeks will produce false positives the first time weather disrupts the network, which is the worst possible moment to be tuning policy. Where possible, run the window across a peak period or a known IROP event.

**Expect the industry-network finding.** The external-connection list almost always surfaces SITA, ARINC, GDS, interline or codeshare connectivity that the customer's documentation treats as internal or does not mention. This is frequently the single most valuable output of the PoV, and it maps directly to the external-connection enumeration under Measure 1.

---

## Phase 3 — Policy (weeks 6–8)

**Goal:** designed isolation, validated before anything blocks.

- [ ] Default-deny posture defined between zones, **in both directions**
- [ ] ADM-imported rules refined; every rule carries a business justification written to be read by an inspector
- [ ] Simulation run for the full window; false positives triaged with change tickets
- [ ] Exception register populated with owner and review date
- [ ] **Change-control classification** recorded for the proposed policy, per the Phase 0 determination

**Deliverable:** policy workspace export, simulation report, exception register.

**Write rules for the inspector, not just the firewall.** The policy export is a compliance artifact in this framework. A rule whose justification reads "required by app team" is weaker than one reading "departure control queries weight and balance at check-in; TLS only."

---

## Phase 4 — Prove it operates (weeks 9–12)

**Goal:** evidence that measures work, not just exist.

- [ ] Enforcement enabled on the pilot zone — **if** Phase 0 permitted it
- [ ] **Bidirectional negative test:** a blocked attempt into the operational core and a blocked attempt out of it, both recorded with timestamps
- [ ] Pre-staged isolation workspace built and tested in a maintenance window; record the time taken to apply
- [ ] `KEV-Exposed-CCS` export produced with reachability context
- [ ] SIEM integration verified with sample events
- [ ] Quarterly evidence binder assembled per [the evidence checklist](./evidence-checklist.md)

**Deliverable:** the binder, plus the effectiveness artifacts called out separately.

**If enforcement was not permitted,** the simulation report plus the denied-connections equivalent from simulation still demonstrate the control's effect, and the isolation-workspace test can still run in a window. Say plainly in the report that enforcement was out of scope for change-control reasons — an honest limitation documented is far better than an implied capability.

---

## Success criteria

| Criterion | Evidence | Measure |
|---|---|---|
| Critical-systems list is complete and continuously reconciled | Inventory + scope-membership delta | Identification obligation |
| Dependency and external-connection documentation generated, not drawn | ADM topology + external-connection list | Measure 1 |
| Previously unknown external connectivity surfaced | `Industry-Network-Connections` export | Measure 1 |
| Inter-zone isolation demonstrated **in both directions** | Bidirectional negative-test record | Measure 1, "and vice versa" |
| Continuous monitoring and baseline deviation demonstrated | Policy-violation history + drift records | Measure 3 |
| Patch prioritization is demonstrably risk-based | `KEV-Exposed-CCS` with reachability | Measure 4 |
| Containment is a decision, not a design exercise | Isolation workspace test with elapsed time | CIRP support |
| Effectiveness evidence exists, distinct from implementation | Simulation + denies + negative test + drift | Annual assessment |

---

## Scoping guardrails

**Do not promise** coverage of aircraft or avionics, airport OT field devices (baggage conveyors, access control and camera field devices, airfield lighting, boarding bridges, fuel systems), endpoint or EFB device fleets, MFA or identity, patch deployment, encryption, or clause-level EA traceability. Each of these is a boundary, not a roadmap item.

**Do not key the deliverable to the four public measures alone.** The customer's CIP numbering is what TSA inspects against; the final report should carry both.

**Treat every artifact as SSI** once it is incorporated into the customer's plan, assessment, or submission, and agree handling with the customer before the first export leaves the platform.
