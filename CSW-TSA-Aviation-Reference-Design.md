# Cisco Secure Workload — TSA Aviation Cybersecurity Compliance Framework
## Reference Design | Aircraft Operators (Airlines) & Airport Operators

**Version:** 1.0 | **Standard:** TSA **Joint Emergency Amendment (EA) 23-01**, issued March 7, 2023 to TSA-approved aircraft operator security programs (49 CFR part 1544) and airport operator security programs (49 CFR part 1542)

---

> **⚠️ Read this before anything else — the EA text is Sensitive Security Information.**
>
> **Joint EA 23-01 is SSI** under [49 CFR 1520.5(b)](https://www.ecfr.gov/current/title-49/section-1520.5), a status DHS confirmed in the Federal Register ([89 FR 28569](https://www.govinfo.gov/content/pkg/FR-2024-04-19/html/2024-08394.htm), n.1). Its requirement text is **not public and is not reproduced here.**
>
> This is the structural difference from the rail and pipeline designs in this series. Those map to a published Security Directive clause by clause. **This document cannot, and does not.** It maps CSW capability to the requirements TSA has described **publicly** — the four performance-based measures in TSA's [March 7, 2023 press release](https://www.tsa.gov/news/press/releases/2023/03/07/tsa-issues-new-cybersecurity-requirements-for-airport-and-aircraft) and the plan and assessment obligations recited in the public appellate record of *Spokane Airport Board v. TSA*.
>
> **Your obligations are defined by your TSA-approved security program and Cybersecurity Implementation Plan, not by this document.** Validate every mapping here against your own SSI-controlled copy of the EA, with people cleared to read it.

---

> **Coverage legend** — this reference design and its evidence pack use three words:
> - 🟢 **Direct** — CSW produces the primary evidence artifact.
> - 🟠 **Supporting** — CSW produces an input that feeds or complements another control.
> - ⚪ **Evidence Required** *(supplied outside CSW)* — CSW produces nothing here; the item is in scope for compliance but out of scope for CSW, so the customer evidences it via another control, tool, or process. A scope boundary, not a gap or "unsupported."

---

## Reader's Guide

**Who this is for.** TSA-regulated **aircraft operators** (airlines)
holding security programs under 49 CFR part 1544 and **airport
operators** under part 1542 whose programs TSA has designated as
covered by Joint EA 23-01 — plus the cybersecurity, IT, flight
operations, and compliance teams supporting them.

**Why this is a separate repo from TSA Rail.** Airlines are not
covered by Security Directive 1580/82-2022-01E. That SD applies to
freight railroad carriers identified in 49 CFR 1580.101 and other
TSA-designated freight and passenger railroads, and it never mentions
aviation. Aviation cyber requirements arrived through a **different
legal instrument** (a security program amendment, not a security
directive), under **different authority** (49 CFR 1542.105(d) and
1544.105(d)), with **different durability rules** and a **different
disclosure status**. §1.1 sets out exactly how they differ, because
treating them as interchangeable in front of a customer or an
inspector is a credibility problem.

**Questions this reference design helps you answer:**

- *Critical systems identification — do I have a current, defensible
  inventory, and can I show it is complete enough that TSA will not
  have to designate systems I missed?*
- *Measure 1 — can I prove that IT compromise cannot disrupt flight
  operations, **and the reverse**, rather than asserting it from a
  network diagram?*
- *Measure 3 — where does continuous monitoring and detection evidence
  for critical cyber systems actually come from?*
- *Measure 4 — which unpatched critical systems are genuinely
  reachable, so patching is prioritized by exposure and not just by
  CVSS?*
- *Annual effectiveness assessment — I have to assess whether my
  measures work, not just that they exist. What produces that?*
- *Plan change control — my CIP is part of my TSA-approved security
  program. What happens to my segmentation rollout when changing it
  needs TSA approval?*

**What you'll need.** Your SSI-controlled copy of **Joint EA 23-01**,
your **TSA-approved Cybersecurity Implementation Plan**, your critical
cyber systems list as submitted, your most recent annual effectiveness
assessment, your Cybersecurity Incident Response Plan, and your
cybersecurity coordinator designation.

**Where to start.** Read §1.2 — the SSI constraint governs how this
document can honestly be used — then §1.3 for the scope boundary,
which for an airline audience is unusually important because **CSW has
no reach into aircraft.** §2 maps the publicly described requirements.
§3–4 build the scope tree and the segmentation policy set. §7 is the
honest boundary. §8 is the inspection-response guide, including the
change-control trap in §8.3.

---

## CSW primer — if you are new to Cisco Secure Workload

Cisco Secure Workload (CSW) is a **workload protection platform**. A lightweight **agent** on each server/VM/container observes processes and network flows; **cloud connectors** add AWS/Azure/GCP inventory where agents are not deployed.

| CSW term | Meaning | Why compliance teams care |
|----------|---------|---------------------------|
| **Scope** | Logical boundary (flight ops tier, PSS, CDE) | Defines the systems you must prove are isolated |
| **Label / filter** | Tag or query assigning workloads to scopes | Automates scope membership — reduces drift |
| **ADM** | Application Dependency Mapping from observed traffic | **Live** network/data-flow diagram for inspectors |
| **Workspace** | Policy container for one scope or application | Where allow/deny rules are authored |
| **Monitor → Simulation → Enforce** | Safe rollout sequence | Simulation = change-board evidence before blocking traffic |
| **Denied Connections** | Log of flows blocked by policy | Primary proof that enforcement **operates** |

**Console areas:** Investigate (inventory, flows, vulns) · Defend/Segmentation (policy) · Manage (agents) · Platform (connectors) · Administration (audit log)

**Read next:** [Compliance evidence playbook](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/docs/compliance-evidence-playbook.md) (full step-by-step) · [About CSW](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/docs/about-csw.md) (platform intro)

---

## Universal evidence workflow

Execute these phases for **this framework's** compliance boundary. Map exports to the measures in **your approved CIP** — see the **Evidence Package** section below.

| Phase | Goal | Key CSW actions | Typical duration |
|-------|------|-----------------|------------------|
| **1 — Coverage** | Every in-scope workload in CSW | Install agents/connectors; apply compliance labels; create scope | Days 1–10 |
| **2 — Baseline** | Machine-generated flow map | Run ADM ≥2 weeks; export clusters; app-owner signoff | Days 11–28 |
| **3 — Policy** | Designed isolation before enforce | Build workspace; Simulation mode; fix false positives | Days 29–45 |
| **4 — Operate** | Continuous proof between inspections | Enforce; quarterly export pack; ADM refresh every 90 days | Ongoing |

### Phase 1 checklist (coverage)

- [ ] IT workloads supporting critical cyber systems reconciled to CSW Inventory (100% or documented exceptions)
- [ ] Labels applied: `compliance:tsa-aviation`, `ccs_id`, `ccs_function`, `zone`, `tsa_designated`, `security_program`
- [ ] CSW scope created matching the zone model in your approved CIP
- [ ] **Export:** inventory CSV + agent status screenshot

### Phase 2 checklist (baseline)

- [ ] ADM running on the flight-operations and PSS tiers for a full operating cycle (≥2 weeks; extend across an IROP or peak-season window)
- [ ] Unexpected flows documented (shadow IT, ground-handler egress, legacy industry-network feeds, scope creep)
- [ ] Interdependencies and external connections enumerated, including SITA/ARINC, GDS, interline and codeshare paths
- [ ] App and system owners signed the cluster-to-system mapping
- [ ] **Export:** ADM diagram + flow samples with process context

### Phase 3 checklist (policy)

- [ ] Default-deny posture defined between zones
- [ ] ADM-imported rules refined; Simulation run ≥30 days for flight-operations tiers
- [ ] Change tickets for false-positive fixes; exception register updated
- [ ] **CIP change-control check performed** — see §8.3 before enforcing
- [ ] **Export:** policy export + simulation report

### Phase 4 checklist (operate)

- [ ] Enforcement enabled on pilot zone; negative test recorded in Denied Connections
- [ ] Quarterly pack: inventory, policy, denies, vulns, audit log (see playbook)
- [ ] SIEM integration verified (sample events)
- [ ] Evidence set assembled for the **annual effectiveness assessment**, not just for implementation
- [ ] **Export:** enforcement screenshot + quarterly binder

### What CSW evidence does not replace

Multi-factor authentication, shared-account management, domain trust
review, patch deployment, encryption, email and web filtering,
personnel and insider-threat programmes, physical security, CISA
incident reporting, the cybersecurity coordinator designation, the
Cybersecurity Incident Response Plan, and the Cybersecurity
Implementation Plan itself all require separate programmes. CSW
addresses the **workload-resident** slice of the operator's **ground
IT estate**: segmentation, flows, process context, vulnerability
reachability, and change drift. §7 enumerates the boundary in full.

---

## CSW effectiveness for this framework

- Measure 1 segmentation between IT and operational systems, with a denied-connections log proving the control operates **in both directions**
- A continuously reconciled critical-systems inventory that reduces the risk of TSA designating systems the operator failed to identify
- Measure 3 continuous monitoring and baseline-deviation detection for critical cyber systems
- Measure 4 exposure-based patch prioritization using reachability plus the CISA KEV catalog
- **Effectiveness** evidence — simulation reports, denied connections, and drift history show whether measures *work*, which is what the annual assessment obligation actually asks

**Compared to manual programmes:** an airline's application
dependency documentation is usually accurate for the systems that were
last migrated and stale everywhere else, while the annual
effectiveness assessment requires a current answer across the whole
critical-systems population. ADM regenerates that map from observed
behaviour on a schedule, which turns an annual documentation scramble
into an export.

---

## 1. Overview

On **March 7, 2023**, TSA issued **Joint Emergency Amendment 23-01**
to the TSA-approved security programs of certain regulated **airport
and aircraft operators**, extending to aviation the performance-based
cybersecurity model it had already applied to pipeline and rail. TSA
issued it without notice and comment, on a finding that "there is an
emergency requiring immediate action" to protect national and
transportation security.

The amendment requires covered operators to **identify critical
systems**, submit a **Cybersecurity Implementation Plan** describing
the measures and controls protecting those systems, and **annually
assess the effectiveness** of those plans. As recited in the public
appellate record, airport operators had **30 days** from the effective
date to identify critical systems and **90 days** to submit the CIP.

As with rail and pipeline, the EA does not prescribe controls
directly. **The TSA-approved plan — not the amendment text — is what
TSA inspects against.** Every CSW artifact in this design should
therefore be mapped to a measure in your plan.

### 1.1 Why this is not the rail Security Directive

Operators with both surface and aviation businesses, and account teams
covering both, need to keep these straight:

| | **Aviation** | **Rail** |
|---|---|---|
| Instrument | Joint Emergency Amendment **23-01** | Security Directive **1580/82-2022-01E** |
| Mechanism | Amends the TSA-approved **security program** | Standalone **security directive** |
| Authority | 49 CFR **1542.105(d)**, **1544.105(d)** | 49 U.S.C. **114(l)(2)** |
| Covered parties | Certain airport operators (part 1542) and aircraft operators (part 1544) | Freight carriers per 49 CFR 1580.101 + TSA-designated freight/passenger railroads |
| TSOB ratification | **Not required** — different authority | **Required** to remain effective beyond 90 days |
| Expiry / renewal | **No fixed expiry**; no annual revision letter | Annual renewal; revision letter advances (01 → 01E) |
| Public disclosure | **SSI** — text not public | TSA determined the SD text is **not** SSI |
| Clause-level mapping possible? | **No** | Yes |

The last two rows are the ones that change how you work. For rail you
can hand a customer a provision-by-provision map. For aviation you
cannot, and any document that claims to is either working from SSI it
should not be redistributing or inventing provision numbers.

### 1.2 The SSI constraint — what this document can and cannot do

**What this design is built from (all public):**

| Source | What it supplies |
|---|---|
| TSA press release, March 7, 2023 | The **four performance-based measures**, verbatim |
| *Spokane Airport Board v. TSA*, No. 23-1155 (D.C. Cir. Jan. 20, 2026) | The plan and assessment obligations, the 30/90-day deadlines, TSA's authority to designate critical systems, and the change-control consequence |
| 89 FR 28569 (Apr. 19, 2024) | SSI status, the authorities relied on, TSOB recommendation, confirmation that the requirements parallel pipeline and rail |
| 49 CFR parts 1542, 1544, 1520 | Security program structure, emergency amendment mechanics, SSI handling |

**What this design does *not* do:**

- It does not reproduce, paraphrase at clause level, or cite internal
  provision numbers from EA 23-01.
- It does not assert that the four public measures are the *complete*
  set of EA requirements. They are what TSA described publicly.
- It does not assert the EA's internal structure, defined terms, or
  deadlines beyond those in the public record above.

**How to use it honestly.** Treat the mapping in §2 as a **structural
analog**: the measures TSA described publicly for aviation are
materially parallel to pipeline and rail, DHS said so in the Federal
Register, and CSW's contribution against that shape is well
understood. Then have someone with authorized access to your EA copy
and your approved CIP confirm each row. Where this document says
"Measure 1," your CIP will have its own numbering — **use your CIP's
numbering in your evidence pack.**

### 1.3 Scope boundary — read this before claiming anything

**CSW is a workload protection platform for IT estate** — servers,
virtual machines, containers, and cloud workloads. Three exclusions
matter enormously for an aviation audience, and the first one is
non-negotiable:

**CSW has no reach into aircraft.** Not avionics, not onboard networks,
not in-flight entertainment or connectivity, not flight-deck systems,
not the aircraft end of a datalink. Onboard systems are governed
principally through FAA airworthiness design and certification
processes, and no CSW agent is involved at any point. If a conversation
drifts toward aircraft systems, say so plainly — this is the single
fastest way to lose an aviation customer's technical confidence.

**CSW does not reach the airport OT layer** — baggage handling
controls, access control and alarm monitoring field devices, airfield
lighting, passenger boarding bridges, CCTV cameras, fuel farm
controls, de-icing systems, or the PLCs behind any of them. For an
airport operator (part 1542) this is a large share of the interesting
estate, so set expectations early: CSW's airport contribution is the
**server and management tier** behind those systems, not the systems
themselves.

**CSW does not reach endpoint fleets** — crew tablets and EFB devices,
gate agent workstations in the general case, kiosks, or handhelds. The
EFB *content distribution and management servers* are in reach; the
tablets are not.

What remains is substantial, and for an airline it is where
operational disruption actually originates:

| In CSW's reach (ground IT) | Out of CSW's reach |
|---|---|
| Flight dispatch, flight following, movement control servers | Aircraft avionics and onboard networks |
| Flight planning, weight and balance, performance systems | Flight-deck and cabin systems |
| Crew scheduling and crew tracking | Pilot and crew EFB tablets |
| Datalink / ACARS **ground** gateways and AOC messaging hosts | The aircraft end of any datalink |
| Reservations, inventory, ticketing | Baggage handling conveyor controls and PLCs |
| Departure control, check-in, boarding, bag reconciliation | Airfield lighting, boarding bridges, fuel controls |
| Maintenance, engineering, MRO and airworthiness systems | Access control and CCTV field devices |
| EFB content distribution and management servers | Kiosks, handhelds, gate workstations |
| Cargo management and air waybill systems | Ground support equipment telematics endpoints |
| Station and common-use **back-end** servers | — |
| Identity, PKI, logging, and patch infrastructure | — |
| Ground handler and vendor remote-access hosts | — |

Your OT-aware monitoring stack (Cisco Cyber Vision, Claroty, Nozomi,
Dragos, or equivalent), your IT/OT boundary firewalls, and your
endpoint platform remain the controlling artifacts outside that left
column. CSW complements them and does not replace them.

### 1.4 Durability and version discipline

Unlike the rail SD, there is **no annual revision letter to chase**:

- EA 23-01 was **immediately effective** on issuance and, under
  1542.105(d), **is not stayed** by a petition for reconsideration.
- It required **no TSOB ratification**, because it was issued under
  part 1542/1544 regulatory authority rather than the 49 U.S.C.
  114(l)(2) emergency authority used for the surface directives. The
  TSOB nonetheless reviewed the matter and, on **April 20, 2023**,
  recommended that a cybersecurity emergency existed warranting the
  action.
- Its authority was **upheld** in *Spokane Airport Board v. TSA*, No.
  23-1155 (D.C. Cir. **Jan. 20, 2026**), which rejected challenges to
  TSA's statutory authority, to consistency with part 1542, and to the
  amendment as arbitrary and capricious, and held the TSOB-ratification
  argument jurisdictionally barred for failure to exhaust.
- TSA has signalled an intent to move aviation cybersecurity to
  **notice-and-comment rulemaking**, on no fixed public timeline. Note
  that TSA's November 2024 surface cyber risk management NPRM covers
  **surface** modes and is not the aviation vehicle.

**Two things to confirm before customer delivery**, neither of which is
publicly answerable: whether TSA has issued a **revision or successor**
to EA 23-01 since March 2023, and whether the customer's specific
security program is **designated as covered**. Both come from the
customer's TSA principal security inspector — not from this document.

**SSI handling.** The amendment is SSI, and everything the operator
submits under it is SSI. Treat CSW evidence exports as SSI from the
moment they are incorporated into a plan, assessment, or submission,
and handle them under 49 CFR part 1520. This is stricter than rail,
where the SD text itself is openly discussable.

---

## 2. Requirement Mapping

Each row carries a **Coverage** verdict from the legend at the top of
this document.

**On the row labels in this section:** the first column describes a
**capability the publicly stated measure implies**. These are *not* EA
provision numbers, and no EA numbering is used anywhere in this
document — see §1.2. Replace them with your CIP's own measure
references when you build the evidence pack.

### 2.1 Measure 1 — Network segmentation

> "Develop network segmentation policies and controls to ensure that
> operational technology systems can continue to safely operate in the
> event that an information technology system has been compromised,
> **and vice versa**"
> — TSA press release, March 7, 2023

The bidirectional phrasing is explicit in the aviation measure and
worth dwelling on. It is not enough to show that an IT compromise
cannot reach operational systems; you also have to show that a
compromise on the operational side cannot disrupt the IT systems that
flight operations depend on. For an airline, where "operational"
systems are themselves largely ground IT, this collapses into a
question CSW answers directly: **can you demonstrate enforced
isolation between tiers, in both directions, from observed behaviour?**

| Capability the measure implies | Coverage | CSW Implementation |
|---|---|---|
| Zone model for critical vs. non-critical systems | 🟢 Direct | Scope tree (§3.1) implements the zone model as queryable scope membership rather than a diagram |
| Enumerate interdependencies between critical systems | 🟢 Direct | ADM generates the dependency map from observed flows, with process context, refreshed on a schedule |
| Enumerate external connections | 🟢 Direct | `Industry-Network-Connections` and `Ground-Handler-Access` filters (§3.2) surface SITA/ARINC, GDS, interline, codeshare and handler paths |
| Prevent unauthorized communication between zones | 🟢 Direct | Allowlist workspace with default-deny between zones (§4.1); Denied Connections log proves it operates |
| Demonstrate isolation holds **in both directions** | 🟢 Direct | Paired deny rules and a bidirectional negative test (§4.2) — the asymmetric test is the common gap |
| Verify traffic crossing zones is protected | 🟠 Supporting | `Plaintext-Crossing-Zones` filter finds cleartext crossings; CSW detects, it does not encrypt |
| Firewall / network device configuration at the boundary | ⚪ Evidence Required | Boundary firewall and network device configs come from the network team |
| Physical and logical isolation of OT field networks | ⚪ Evidence Required | Out of CSW's reach entirely (§1.3) |

### 2.2 Measure 2 — Access control

> "Create access control measures to secure and prevent unauthorized
> access to critical cyber systems"

This is the measure where CSW contributes least and where overclaiming
is most tempting. CSW governs **network reachability** — which
workloads may talk to which, on what ports, from which processes. It
does not authenticate users, issue credentials, or manage accounts.

| Capability the measure implies | Coverage | CSW Implementation |
|---|---|---|
| Restrict which systems can reach critical systems | 🟢 Direct | `Privileged-Access-Paths` scope plus allowlist rules constrain administrative reachability to named sources and ports |
| Evidence that unauthorized access paths are blocked | 🟢 Direct | Denied Connections log for attempts against critical-system scopes |
| Identify undocumented administrative paths | 🟠 Supporting | ADM surfaces SSH/RDP/WinRM reachability the access model does not acknowledge |
| Third-party and ground-handler access scoping | 🟠 Supporting | `managed_by` label and `Ground-Handler-Access` filter isolate externally managed workloads |
| Multi-factor authentication | ⚪ Evidence Required | Identity provider / MFA platform |
| Least privilege and separation of duties for user accounts | ⚪ Evidence Required | IAM and governance tooling |
| Shared account management, password handling | ⚪ Evidence Required | PAM / credential vault |
| Domain trust relationship review | ⚪ Evidence Required | Directory services |
| Physical access controls | ⚪ Evidence Required | Facility security programme |

### 2.3 Measure 3 — Continuous monitoring and detection

> "Implement continuous monitoring and detection policies and
> procedures to defend against, detect, and respond to cybersecurity
> threats and anomalies that affect critical cyber system operations"

| Capability the measure implies | Coverage | CSW Implementation |
|---|---|---|
| Continuous visibility of critical system communications | 🟢 Direct | Flow telemetry with process attribution, retained and exportable |
| Detect deviation from an established baseline | 🟢 Direct | ADM baseline plus policy-violation and unmatched-flow logging (§4.1 catch-all) |
| Detect unauthorized communication attempts | 🟢 Direct | Denied Connections log |
| Detect configuration and software drift on critical systems | 🟢 Direct | Process and package inventory change history per workload |
| Forward security-relevant events to central analysis | 🟠 Supporting | SIEM/SOAR integration; CSW is a feed, not the detection platform of record |
| Detect anomalies on OT field devices and networks | ⚪ Evidence Required | OT-aware monitoring platform |
| Endpoint and user behaviour detection | ⚪ Evidence Required | EDR / UEBA |
| Email and web filtering, domain blocking | ⚪ Evidence Required | Secure email and web gateways |
| Incident response execution and reporting to CISA | ⚪ Evidence Required | CIRP and SOC process |

### 2.4 Measure 4 — Risk of exploitation of unpatched systems

> "Reduce the risk of exploitation of unpatched systems through the
> application of security patches and updates for operating systems,
> applications, drivers and firmware on critical cyber systems in a
> timely manner using a **risk-based methodology**"

"Risk-based methodology" is the operative phrase, and reachability is
the part of risk that most vulnerability programmes cannot show. A
critical CVE on a workload that nothing can reach is a different
exposure from a moderate CVE on a workload reachable from a ground
handler's network.

| Capability the measure implies | Coverage | CSW Implementation |
|---|---|---|
| Vulnerability inventory for critical systems | 🟢 Direct | Per-workload CVE inventory from installed package data, scoped to `ccs_id` |
| Risk-based prioritization | 🟢 Direct | Reachability plus exposure plus CISA KEV presence — `KEV-Exposed-CCS` filter (§3.2) |
| Compensating controls where patching is not feasible | 🟢 Direct | Targeted segmentation around the unpatchable workload, with the policy export as the compensating-control evidence |
| Firmware and driver currency | 🟠 Supporting | Partial at the OS/driver package layer; device firmware generally outside |
| Patch deployment and verification | ⚪ Evidence Required | Patch management platform |
| Patch testing and change approval | ⚪ Evidence Required | Change management process |
| OT device patching | ⚪ Evidence Required | Vendor-coordinated OT maintenance |

### 2.5 Plan, identification, and assessment obligations

These come from the public appellate record rather than the press
release.

| Obligation | Coverage | CSW Implementation |
|---|---|---|
| Identify the list of critical systems | 🟠 Supporting | CSW hosts the inventory and labels that make the list operational and continuously reconciled; the **designation itself is an operational risk decision** your accountable officer signs |
| Keep that list complete as the estate changes | 🟢 Direct | New workloads appear in inventory on agent install; scope-membership deltas are exportable as a reconciliation record |
| Submit a Cybersecurity Implementation Plan | ⚪ Evidence Required | The plan is yours to author; CSW supplies the segmentation and monitoring measures it describes |
| **Annually assess the effectiveness** of the plan | 🟢 Direct | Simulation reports, Denied Connections, policy-violation history and drift records show whether measures *work* — see §6 |
| Report assessment results to TSA | ⚪ Evidence Required | Your submission process, under SSI handling |
| Architecture / design assessment input | 🟠 Supporting | Current ADM topology and enforced policy state as the as-built input |

**The sharpest point in this table is the second row.** The public
record of *Spokane* records TSA's position that it may **designate
systems as critical even when the operator has not identified them**,
because that authority is "necessary to prevent gaps." Under-scoping
is therefore not a quiet saving — it is an invitation for TSA to scope
for you. A discovery-driven inventory, where membership follows
observed behaviour rather than memory, is the direct hedge, and §3.3
includes a `tsa_designated` label so operator-identified and
TSA-designated entries stay distinguishable in your own records.

### 2.6 Foundational predecessor requirements

TSA's press release notes that requirements already in place for
regulated airport and aircraft operators before EA 23-01 included the
following. They remain live obligations and CSW touches them only at
the edges.

| Requirement | Coverage | CSW Implementation |
|---|---|---|
| Designate a cybersecurity point of contact / coordinator | ⚪ Evidence Required | Organizational designation |
| Report significant cybersecurity incidents to CISA | ⚪ Evidence Required | Incident reporting process |
| Develop and adopt a Cybersecurity Incident Response Plan | 🟠 Supporting | Pre-staged isolation workspace (§4.3) is a containment capability the CIRP can reference and test |
| Complete a cybersecurity vulnerability assessment | 🟠 Supporting | Workload vulnerability and reachability data as an input; the assessment itself is broader |

**Coverage summary:** 16 🟢 Direct · 9 🟠 Supporting · 18 ⚪ Evidence
Required, across 43 mapped capabilities.

That ⚪ count is higher than any other design in this series, and the
reason is structural rather than a shortcoming: two of the four
measures (access control, patching) are predominantly identity and
endpoint work, and the aviation estate excluded in §1.3 — aircraft,
airport OT, endpoint fleets — is larger than rail's. Lead with the
🟢 column and name the ⚪ column before a customer discovers it.

---

## 3. Scope Architecture and Labeling

Build the scope tree so that the tree *is* the zone model in your
Cybersecurity Implementation Plan. If the two diverge, the CSW export
stops being evidence and becomes a contradiction an inspector will
pursue — and because your CIP is part of your approved security
program, reconciling them later is a change-control event rather than
a quick edit (§8.3).

### 3.1 Suggested Scope Architecture

Centred on an **aircraft operator** (part 1544). Airport operators
should read §3.4.

```
Root Scope
└── Aviation-Critical-Cyber-Systems
    ├── Flight-Operations                     (operational core)
    │   ├── Dispatch-and-Flight-Following
    │   ├── Flight-Planning-and-Weight-Balance
    │   ├── Crew-Scheduling-and-Tracking
    │   └── Datalink-Ground-Gateway            (ACARS / AOC messaging — ground side only)
    ├── Passenger-Service-Systems              (business services; disruption-causing)
    │   ├── Reservations-and-Inventory
    │   ├── Departure-Control-and-Checkin
    │   └── Baggage-Reconciliation
    ├── Maintenance-and-Engineering
    │   ├── MRO-and-Airworthiness
    │   └── EFB-Content-Distribution           (servers only — not the tablets)
    ├── Cargo-Operations
    ├── CCS-Supporting-IT
    │   ├── Identity-and-PKI
    │   ├── Logging-and-Monitoring
    │   └── Patch-Repositories
    ├── Station-and-Airport-Facing             (common-use back end, gate/ramp servers)
    ├── Privileged-Access-Paths
    ├── Corporate-IT                           (default-deny source)
    └── External
        ├── Internet-Edge
        ├── Industry-Networks                  (SITA / ARINC, GDS, interline, codeshare)
        └── Vendor-and-Ground-Handler-Access
```

Four branches are deliberate. **`Flight-Operations`** is separated
because it is the population whose disruption is operationally
unambiguous, and the one an inspector will probe first.
**`Passenger-Service-Systems`** exists because reservations and
departure control are *business* systems whose loss grounds an
airline — this is where under-scoping usually hides, exactly as crew
scheduling does in rail. **`Industry-Networks`** has no analog in the
surface designs and is the branch most often missing from an airline's
documentation: SITA and ARINC messaging, GDS connectivity, interline
and codeshare feeds are external connections into operational systems,
frequently legacy, and frequently not firewalled like internet traffic.
**`Datalink-Ground-Gateway`** is named separately so the ground/air
split is explicit in the tree itself, which keeps the §1.3 boundary
visible to anyone reading the export.

### 3.2 Inventory Filters

```
Filter: Flight-Operations-Core
  - Tag: ccs_function = dispatch | flight-planning | crew | datalink-gw
  - Tag: ops_disruption_impact = high

Filter: TSA-Designated-Critical
  - Tag: tsa_designated = true
  - Tracks systems TSA designated rather than the operator identified

Filter: Industry-Network-Connections
  - Source or destination in documented SITA / ARINC / GDS ranges
  - Supports the external-connection enumeration under Measure 1

Filter: Ground-Handler-Access
  - Tag: managed_by = ground-handler | mssp | gds
  - Observed inbound on tcp/22, tcp/3389, tcp/443 from outside operator ranges

Filter: Plaintext-Crossing-Zones
  - Source zone != destination zone
  - Protocol / port: tcp/80, tcp/21, tcp/23, tcp/389, tcp/1433, udp/161
  - Include legacy aviation messaging ports carrying Type B / teletype
    traffic in cleartext

Filter: KEV-Exposed-CCS
  - Tag: ccs_id is set
  - Vulnerability present in the CISA Known Exploited Vulnerabilities Catalog
  - Reachable from a non-critical or external zone
```

Three of these exist to answer a specific question before someone else
asks it. `TSA-Designated-Critical` keeps your scoping judgment and
TSA's separable, which matters when you are defending the
completeness of your list. `Plaintext-Crossing-Zones` finds cleartext
crossings yourself; the legacy-messaging line is there because
aviation industry messaging is an unusually rich source of unencrypted
traffic into operational systems. `KEV-Exposed-CCS` is the Measure 4
prioritization list, and the reachability clause is what makes it
risk-based rather than a CVE dump.

### 3.3 Labeling Strategy

| Label key | Example values | Why it matters |
|---|---|---|
| `ccs_id` | <CIP register entry> | The join key between CSW and your TSA-approved plan — the single most important label here, because TSA inspects against the plan |
| `ccs_function` | dispatch, flight-planning, crew, datalink-gw, reservations, dcs, bag-recon, mro, efb-dist, cargo, identity, patch-repo, logging, station-it, vendor-access | Drives zone assignment and patch prioritization |
| `zone` | flight-ops, pss, maint, cargo, ccs-supporting, station, corporate, external | Makes the CIP's logical zones a queryable attribute instead of a diagram |
| `ops_disruption_impact` | high, moderate, low | The criticality judgment; record it where the evidence lives |
| `tsa_designated` | true, false | Distinguishes systems **TSA** designated as critical from those the operator identified — see §2.5 |
| `security_program` | 1544, 1542, both | Carriers that also operate facilities hold obligations under both parts; keep the exports separable |
| `interdependency_group` | <named group> | Supports the interdependency enumeration under Measure 1 |
| `managed_by` | internal, ground-handler, mssp, gds, authorized-rep | Know which workloads a third party touches before an inspector asks |
| `station` | <IATA code> | Airline estates are station-distributed and inspections are often station-scoped |
| `compliance` | tsa-aviation | Filters every CSW export to the EA boundary |

`ccs_id`, `tsa_designated`, and `managed_by` are the three worth
enforcing at onboarding. The first makes every export reconcilable to
the approved plan; the second preserves the provenance of your
critical-systems list; the third answers the ground-handler and MSSP
question in advance.

### 3.4 Airport operators (part 1542)

An airport operator's tree keeps the same shape but repopulates the
critical branch, and the §1.3 boundary bites much harder because more
of the interesting estate is OT:

```
└── Aviation-Critical-Cyber-Systems
    ├── Airport-Operations-IT
    │   ├── Baggage-Handling-Servers          (server tier only — not conveyor PLCs)
    │   ├── Access-Control-Management          (ACAMS head end — not field devices)
    │   ├── Video-Management-Servers           (VMS — not cameras)
    │   ├── Common-Use-Backend                 (CUPPS / CUSS servers)
    │   └── Flight-Information-Display-Backend
    ├── Airfield-Systems-Management            (management tier only)
    ├── CCS-Supporting-IT
    ├── Tenant-and-Airline-Interconnect        (each carrier is an external connection)
    ├── Corporate-IT
    └── External
```

Every branch above is deliberately named for the **server or
management tier**. An airport reference design that implies CSW
secures the baggage system or the access control system itself is
wrong, and `Tenant-and-Airline-Interconnect` exists because an
airport's tenant carriers are external connections that airport
documentation often treats as internal.

---

## 4. Policy Design — Measure 1 Zone Enforcement

Measure 1 asks for controls ensuring operations continue when the
other side is compromised, in **both** directions. That makes an
allowlist with documented justifications the natural implementation,
and it makes the policy export a compliance artifact rather than an
operational one. Write each rule to be read by an inspector.

### 4.1 Measure-Aligned Policy Framework

**Absolute policies:**

```
DENY  Corporate-IT                        → Flight-Operations                    (no unauthorized path into the operational core)
DENY  Internet-Edge                       → Aviation-Critical-Cyber-Systems      (external connections are enumerated, never implicit)
DENY  Industry-Networks                   → Flight-Operations                    (SITA / ARINC / GDS stop short of the operational core)
DENY  Vendor-and-Ground-Handler-Access    → Flight-Operations                    (third-party paths stop short of the operational core)
DENY  Flight-Operations                   → Internet-Edge                        (no unvalidated egress from the operational core)
DENY  Flight-Operations                   → Corporate-IT                         (the reverse direction — "and vice versa")
DENY  Flight-Operations                   → Flight-Operations                    (no implicit east-west inside the operational core)
```

Two of these rules are the ones that get dropped. **`Flight-Operations
→ Corporate-IT`** is the literal "and vice versa" clause: without it
you have demonstrated one direction of a bidirectional requirement.
**`Flight-Operations → Flight-Operations`** denies implicit
intra-tier traffic; "it is all inside one zone" is not a segmentation
answer, and allowlisting the justified intra-tier paths is what
produces a defensible east-west record.

**Allowlist policies (least privilege):**

```
ALLOW Departure-Control-and-Checkin       → Flight-Planning-and-Weight-Balance   tcp/<wb-port-tls>
ALLOW Dispatch-and-Flight-Following       → Datalink-Ground-Gateway              tcp/<acars-gw-tls>
ALLOW Dispatch-and-Flight-Following       → Flight-Planning-and-Weight-Balance   tcp/<ops-port-tls>
ALLOW Reservations-and-Inventory          → Industry-Networks                    tcp/443
ALLOW Aviation-Critical-Cyber-Systems     → Identity-and-PKI                     tcp/636, tcp/88
ALLOW Privileged-Access-Paths             → Flight-Operations                    tcp/22, tcp/3389
ALLOW Aviation-Critical-Cyber-Systems     → Logging-and-Monitoring               tcp/443, udp/514
ALLOW Patch-Repositories                  → Aviation-Critical-Cyber-Systems      tcp/443
```

Every port is specified in its TLS-bearing form deliberately. If the
only rule that makes a system work is the cleartext port — common with
legacy Type B messaging and older interline feeds — you have
documented a protection gap rather than closed one. That is still
useful, but record it as a gap with a compensating control, not as a
satisfied requirement.

**Catch-all:**

```
LOG   Any                                 → Flight-Operations                    (unmatched inbound)
LOG   Flight-Operations                   → Any                                  (unmatched outbound — baseline deviation)
LOG   Any                                 → Any                                  (plaintext crossing zones: tcp/80, tcp/21, tcp/23, tcp/389, udp/161)
```

### 4.2 Policy Workspace Lifecycle

| Phase | Mode | Duration | Purpose |
|---|---|---|---|
| 1 | Simulation | 30 days | Validate against a full operating cycle including an IROP or peak-season window — longer than this series' usual 2 weeks, because airline traffic is schedule-driven and seasonal, and irregular operations generate flows that never appear in normal weeks |
| 2 | Enforcement (absolute denies only) | 2 weeks | Enforce the inter-zone deny rules first |
| 3 | Full Enforcement | Ongoing | Zone allowlist enforced; monthly exception review |

Workspace snapshots are the Measure 1 implementation evidence; the
simulation report shows the policy was assessed before it was
enforced; and the Denied Connections log is the proof the control
**operates** rather than merely exists.

> **Run the negative test in both directions.** Measure 1 is
> bidirectional, so a containment test that only proves
> `Corporate-IT → Flight-Operations` is blocked evidences half the
> requirement. Record a blocked attempt in each direction, with
> timestamps, and keep both in the pack. This is the most common
> gap in aviation evidence sets and it is trivial to close once named.

### 4.3 Pre-Staged Isolation Workspace

Build a standing, unapplied workspace so containment is a decision
rather than a design exercise during an incident. Your Cybersecurity
Incident Response Plan can reference it, which is also how it earns
the 🟠 in §2.6:

```
Workspace: tsa-aviation-emergency-isolation   (staged, not enforced)
  DENY  Corporate-IT                        → Flight-Operations
  DENY  Industry-Networks                   → Aviation-Critical-Cyber-Systems
  DENY  Vendor-and-Ground-Handler-Access    → Aviation-Critical-Cyber-Systems
  DENY  Station-and-Airport-Facing          → Flight-Operations
  ALLOW Privileged-Access-Paths             → Flight-Operations                 tcp/22, tcp/3389
```

Test it during a planned maintenance window, record the test, and keep
the record. The evidence worth having is not that you *could* isolate —
it is that you have, and that you know how long it took.

---

## 5. Rollout Guidance by Operator Profile

| Profile | Where to start | Watch for |
|---|---|---|
| **Mainline network carrier** | Flight operations tier first — dispatch, flight following, planning, crew. Highest inspection salience and clearest disruption story | Hub-and-spoke station sprawl; decades of accumulated interline and GDS connectivity; mainframe-era PSS components that resist agent deployment |
| **Regional / feeder carrier** | PSS and the capacity-purchase interconnect to the mainline partner | The mainline partner's systems are an **external connection** even when the relationship is exclusive; codeshare paths often undocumented |
| **All-cargo operator** | Cargo management, air waybill, and ground handling interconnect | Customs and trade data flows cross borders and jurisdictions; handler networks are numerous and loosely governed |
| **Airport operator (part 1542)** | Server and management tier behind BHS, ACAMS, VMS, common-use | §1.3 and §3.4 — most of the interesting estate is OT and out of reach; set expectations before the first workshop |
| **Dual-obligation operator** | Keep exports separable from day one | Use `security_program` to tag 1544 vs 1542 assets; the two programmes are amended separately |

For every profile, the **30-day critical-systems and 90-day plan
cadence in the public record applies to new designations**, not just
to the original 2023 effective date. An operator newly designated as
covered is on a short clock, and a discovery-driven inventory is the
only way to meet a 30-day identification deadline with any confidence.

---

## 6. Evidence Package

Map every artifact to a measure in **your approved CIP**, using your
CIP's numbering rather than this document's labels (§1.2).

| CSW artifact | Export path | Evidences |
|---|---|---|
| Critical-systems inventory with labels | Investigate → Inventory → export CSV | Critical systems identification; completeness of the list |
| Scope-membership delta report | Inventory → scope reconciliation export | That the list stays current as the estate changes |
| ADM dependency map | Defend → Segmentation → ADM → export | Interdependency enumeration; as-built topology |
| External-connection list | `Industry-Network-Connections` + `Ground-Handler-Access` filter exports | External connection enumeration under Measure 1 |
| Policy workspace snapshot | Defend → Segmentation → workspace → export | Segmentation controls as designed |
| Simulation report | Workspace → Simulation → report | That the policy was assessed before enforcement |
| Denied Connections log | Investigate → Flows → filter Denied | That segmentation and access restriction **operate** |
| Bidirectional negative-test record | Denied Connections, filtered to the test window | The "and vice versa" half of Measure 1 (§4.2) |
| Policy-violation and unmatched-flow history | Flows → policy violation filter | Continuous monitoring; baseline deviation |
| Workload drift history | Inventory → workload → process/package history | Configuration and software drift detection |
| Vulnerability inventory, scoped | Investigate → Vulnerabilities, filtered to `ccs_id` | Vulnerability posture of critical systems |
| `KEV-Exposed-CCS` export | Filter export | Risk-based patch prioritization under Measure 4 |
| `Plaintext-Crossing-Zones` export | Filter export | Protection of cross-zone traffic — and honest gap disclosure |
| Pre-staged isolation workspace + test record | Workspace export + test log | Containment capability referenced by the CIRP |
| Administration audit log | Administration → Audit Log | Who changed policy, when — change-control evidence |

**For the annual effectiveness assessment specifically**, the
distinction that matters is between artifacts proving a measure
*exists* and artifacts proving it *works*. The first group is the
policy snapshot and the inventory. The second group — and this is what
the assessment obligation actually asks for — is the **simulation
report, the Denied Connections log, the bidirectional negative test,
and the drift history**. Build the assessment pack from the second
group and cite the first as context.

Cadence: quarterly export into a dated binder, ADM refreshed every 90
days, assessment pack assembled annually. **Treat each binder as SSI**
once it is incorporated into a submission (§1.4).

---

## 7. Evidence Boundary — What You Must Supply Outside CSW

### 7.1 Where CSW produces nothing

Multi-factor authentication, account and credential management, shared
accounts, domain trust review, patch deployment and verification,
encryption, email and web filtering, endpoint and user-behaviour
detection, physical security, personnel and insider-threat
programmes, CISA incident reporting, the cybersecurity coordinator
designation, the Cybersecurity Incident Response Plan, the
Cybersecurity Implementation Plan, and the submission process itself.
CSW contributes nothing to any of these. Each needs a named owner and
a named artifact in your plan.

### 7.2 The three exclusions that matter most here

**Aircraft.** CSW has no reach into avionics, onboard networks,
flight-deck or cabin systems, or the aircraft end of a datalink. There
is no partial answer and no roadmap answer. Say so early (§1.3).

**The airport OT layer.** Baggage conveyor controls, access control and
camera field devices, airfield lighting, boarding bridges, fuel
systems, and their PLCs. CSW reaches the server and management tier
behind them and nothing below it.

**Endpoints.** Crew EFB tablets, kiosks, handhelds, and gate
workstations in the general case. EFB *distribution servers* are in
reach; the devices are not.

### 7.3 Encryption — the most commonly misread boundary

CSW **detects** cleartext traffic crossing zone boundaries and can
block it by policy. CSW does **not** encrypt traffic, terminate TLS,
manage certificates, or validate cipher strength. Where a measure
conditions cross-zone traffic on the content being protected, CSW
evidences *which flows are unprotected*; your TLS, VPN, and key
management programmes evidence *that the rest are protected*. The
`Plaintext-Crossing-Zones` filter is a gap-finding tool, and finding
your own gaps is materially better than having an inspector find them.

### 7.4 The requirement text itself

This is the boundary unique to aviation. Because EA 23-01 is SSI, **no
vendor document can give you clause-level traceability**, and this one
does not pretend to. The gap is closed only inside the customer, by
someone with authorized access, mapping the §2 capability rows to the
real provisions and to the approved CIP. Plan for that step in the
engagement rather than discovering it at the evidence review.

### 7.5 Plan-relative evidence and SSI handling

TSA inspects against the **approved plan**. An evidence pack keyed only
to the four public measures will not survive an inspection that is
working from the operator's CIP — the mapping has to be re-expressed
in the customer's own measure numbering. And once CSW exports are
incorporated into a plan, assessment, or submission, they are SSI
under 49 CFR part 1520 and must be handled, marked, stored, and
transmitted accordingly.

---

## 8. TSA Inspection Response Guide

### 8.1 Likely requests and where the answer lives

| If an inspector asks… | Produce | Section |
|---|---|---|
| "Show me your critical systems list and how you know it is complete." | Inventory export + scope-membership delta report + `TSA-Designated-Critical` filter | §2.5, §6 |
| "Show me the segmentation between your IT and operational systems." | Policy workspace snapshot + ADM topology | §4.1, §6 |
| "Prove it holds if the IT side is compromised. Now prove the reverse." | Denied Connections log, both directions, with the negative-test record | §4.2 |
| "What external connections touch these systems?" | `Industry-Network-Connections` + `Ground-Handler-Access` exports | §3.2 |
| "How do you monitor these systems continuously?" | Flow telemetry sample + policy-violation history + SIEM integration evidence | §2.3 |
| "How did you prioritize patching on critical systems?" | `KEV-Exposed-CCS` export + reachability context | §2.4 |
| "How did you assess effectiveness this year?" | Simulation report + denies + negative test + drift history | §6 |
| "Who outside your organization can reach these systems?" | `managed_by` label export + `Ground-Handler-Access` filter | §3.3 |

### 8.2 Three answers to get right

**On completeness of the critical-systems list** — lead with the
discovery mechanism, not the list. "Membership follows observed
behaviour and is reconciled on a schedule; here is the delta report"
is a much stronger answer than a spreadsheet, given TSA's position
that it may designate systems you did not identify.

**On the IT/OT boundary** — state the limit before you are asked. An
operator who volunteers that CSW covers the ground IT tier and names
what covers the rest reads as competent. An operator whose vendor
document implied more reads as poorly advised.

**On effectiveness versus implementation** — answer the question that
was asked. "Here is the policy" answers implementation. "Here is the
simulation report, the blocked attempts in both directions, and the
drift history" answers effectiveness.

### 8.3 The change-control trap

This is the aviation-specific operational constraint, and it has no
exact rail equivalent.

Because EA 23-01 **amends the security program**, the Cybersecurity
Implementation Plan becomes part of that TSA-approved program — and
under 49 CFR 1542.105(b) changes to an approved program require TSA
approval. The *Spokane* court addressed this directly: the amendment
"requires operators to obtain TSA approval for changes to those
plans," while noting the limit — operators "need not secure TSA
approval for improvements that do not conflict with their existing
security programs."

The practical consequence for a CSW rollout:

- **Write the CIP at the level of capability and process, not brittle
  specifics.** A plan that says "inter-zone communication is
  default-deny, allowlisted with documented business justification,
  reviewed monthly" accommodates policy evolution. A plan that
  enumerates individual rules, ports, or scope names converts routine
  tuning into a change-approval queue.
- **Classify changes before making them.** Tightening a rule or adding
  a monitored zone is usually an improvement that does not conflict
  with the approved program. Removing an enforcement boundary the plan
  claims, or re-scoping a critical system out, is a different animal.
- **Wire CSW change history into the change-control process.** The
  Administration audit log is your record of what changed and when,
  which is what you will need if the classification is ever
  questioned.
- **Confirm the current mechanics with your TSA principal security
  inspector.** The court noted TSA "indicated that, to the extent the
  process for securing TSA approval impedes necessary cybersecurity
  improvements, it would consider changes to the amendment process in
  the future." Whether it has is not publicly answerable.

---

## Related Frameworks

| Framework | Relationship |
|---|---|
| [TSA Rail Cybersecurity](https://github.com/chandrapati/CSW-TSA-Rail-Reference-Design) | Sibling surface-mode design. DHS stated the aviation requirements parallel the pipeline and rail directives, so the rail design is the closest clause-level analog — with the caveats in §1.1 |
| [TSA Pipeline Security Directive](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/TSA-Pipeline/CSW-TSA-Pipeline-Technical-Runbook.md) | The original performance-based model this series extends |
| [NIST 800-53](https://github.com/chandrapati/CSW-NIST-800-53-Reference-Design) | AC-4, SC-7, CA-7, RA-5, SI-4 underpin the four measures; TSA's framing aligns to the NIST Cybersecurity Framework |
| [IEC 62443](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/IEC-62443/CSW-IEC62443-Technical-Runbook.md) | Zones and conduits — the engineering vocabulary behind the segmentation measure, relevant for airport OT |
| [NIST 800-207 (Zero Trust)](https://github.com/chandrapati/CSW-Compliance-Reference-Designs/blob/main/NIST-800-207/CSW-NIST-800-207-Technical-Runbook.md) | Default-deny and per-flow authorization as the architectural direction |

---

## References & official sources

- TSA, [*TSA issues new cybersecurity requirements for airport and aircraft operators*](https://www.tsa.gov/news/press/releases/2023/03/07/tsa-issues-new-cybersecurity-requirements-for-airport-and-aircraft), press release, March 7, 2023 — **source of the four measures quoted in §2**
- DHS, [*Recommendation Regarding Emergency Action in Aviation*](https://www.govinfo.gov/content/pkg/FR-2024-04-19/html/2024-08394.htm), 89 FR 28569, April 19, 2024 — SSI status, authorities, TSOB recommendation
- *Spokane Airport Board v. TSA*, [No. 23-1155 (D.C. Cir. Jan. 20, 2026)](https://media.cadc.uscourts.gov/opinions/docs/2026/01/23-1155-2154795.pdf) — plan obligations, deadlines, critical-system designation authority, change-control holding
- [49 CFR part 1542](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-XII/subchapter-C/part-1542) — Airport security; [1542.105](https://www.ecfr.gov/current/title-49/section-1542.105) amendment procedures
- [49 CFR part 1544](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-XII/subchapter-C/part-1544) — Aircraft operator security
- [49 CFR part 1520](https://www.ecfr.gov/current/title-49/subtitle-B/chapter-XII/subchapter-B/part-1520) — Protection of Sensitive Security Information
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- TSA, [Surface Transportation Cybersecurity Toolkit](https://www.tsa.gov/for-industry/surface-transportation-cybersecurity-toolkit)

---

## Disclaimer

**Draft v1 — pending SME review on both regulatory accuracy and
current Cisco product capability.**

This reference design is an **independent engineering work product**.
It is not a Cisco product document, not legal advice, and not a
compliance certification. It is **not endorsed by or affiliated with
TSA, DHS, or FAA.**

**Joint EA 23-01 is Sensitive Security Information under 49 CFR
1520.5(b).** This document is built exclusively from public sources —
TSA's March 2023 press release, the Federal Register, the public
appellate record, and the Code of Federal Regulations — all cited
above. It does **not** reproduce, paraphrase at clause level, or cite
internal provisions of the amendment, and it makes **no claim** that
the four publicly described measures are the complete set of EA
requirements. The capability labels in §2 are this document's own
descriptive headings, **not EA provision numbers.**

**Your obligations are determined by your TSA-approved security
program and Cybersecurity Implementation Plan**, read by people
authorized to access them. Validate every mapping here against those
documents before relying on it. Whether a given operator is covered,
and whether a revision or successor to EA 23-01 has been issued, are
questions for your TSA principal security inspector.

CSW capabilities described here reflect the author's field
understanding and require confirmation against current product
documentation and your licensed feature set. Nothing here guarantees a
particular inspection outcome.

---

*Part of the [CSW Compliance Reference Designs](https://github.com/chandrapati/CSW-Compliance-Reference-Designs) series.*
