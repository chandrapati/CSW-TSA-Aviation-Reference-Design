"""TSA Aviation diagram content.

Every string below is lifted from CSW-TSA-Aviation-Reference-Design.md
(Universal evidence workflow and section 1.2) so the diagrams and the prose
cannot drift apart.
"""

EVIDENCE_WORKFLOW = {
    "kicker": "Joint EA 23-01",
    "title": "CSW Evidence Workflow",
    "title_tail": "&mdash; TSA Aviation",
    "sub": "From agent coverage to continuous proof between inspections &mdash; "
           "mapped to the measures in your approved Cybersecurity Implementation Plan.",
    "phases": [
        {
            "name": "Coverage",
            "goal": "Every in-scope workload visible in CSW",
            "when": "Days 1&ndash;10",
            "actions": [
                "Install agents and connectors across the ground IT estate",
                "Apply <b>compliance</b>, <b>ccs_id</b>, <b>ccs_function</b>, "
                "<b>zone</b> and <b>tsa_designated</b> labels",
                "Create the scope matching the zone model in your approved CIP",
                "Reconcile to inventory at 100% or document exceptions",
            ],
            "export": "Inventory CSV and agent status screenshot",
        },
        {
            "name": "Baseline",
            "goal": "Machine-generated flow map, owner-signed",
            "when": "Days 11&ndash;28",
            "actions": [
                "Run ADM on flight operations and PSS tiers for a full operating cycle",
                "Extend across an IROP or peak-season window",
                "Enumerate SITA / ARINC, GDS, interline and codeshare paths",
                "App and system owners sign the cluster-to-system mapping",
            ],
            "export": "ADM diagram and flow samples with process context",
        },
        {
            "name": "Policy",
            "goal": "Isolation designed and proven before enforcement",
            "when": "Days 29&ndash;45",
            "actions": [
                "Define the default-deny posture between zones",
                "Refine ADM-imported rules; run <b>Simulation</b> 30 days or more",
                "Raise change tickets for false positives; update the exception register",
                "Perform the <b>CIP change-control check</b> before enforcing",
            ],
            "export": "Policy export and simulation report",
        },
        {
            "name": "Operate",
            "goal": "Continuous proof between inspections",
            "when": "Ongoing",
            "actions": [
                "Enable enforcement on the pilot zone; record the negative test",
                "Assemble the quarterly pack: inventory, policy, denies, vulns, audit log",
                "Verify SIEM integration with sample events",
                "Build the set for the <b>annual effectiveness assessment</b>",
            ],
            "export": "Enforcement screenshot and quarterly binder",
        },
    ],
    "caution_label": "Change control &rsaquo;",
    "caution": "Your Cybersecurity Implementation Plan becomes part of your "
               "TSA-approved security program, so changes to it need TSA approval under "
               "49 CFR 1542.105(b). <b>Nothing is enforced until that check is complete</b> "
               "&mdash; simulation carries the proof in the meantime.",
    "takeaway_tag": "Key Takeaway",
    "takeaway": "CSW turns observed traffic into designed isolation and keeps producing "
                "evidence after the project ends. <b>TSA inspects against your approved "
                "plan, not against this workflow</b> &mdash; so map every export to your "
                "CIP's own measure numbering.",
    "rail": [
        "Machine-generated flow evidence, not hand-drawn diagrams",
        "Simulation proves the policy before anything is enforced",
        "Quarterly packs carry the annual effectiveness assessment",
    ],
}


SCOPE_BOUNDARY = {
    "kicker": "Section 1.2",
    "title": "What CSW Reaches",
    "title_tail": "&mdash; TSA Aviation Scope Boundary",
    "sub": "CSW is a workload protection platform for the operator's ground IT estate. "
           "Three exclusions matter enormously for an aviation audience.",
    "exclusions": [
        {
            "head": "No reach into aircraft",
            "body": "Not avionics, onboard networks, in-flight entertainment or "
                    "connectivity, flight-deck systems, or the aircraft end of a datalink. "
                    "Onboard systems are governed principally through FAA airworthiness "
                    "design and certification processes.",
        },
        {
            "head": "No reach into the airport OT layer",
            "body": "Baggage handling controls, access control and alarm field devices, "
                    "airfield lighting, boarding bridges, CCTV, fuel farm and de-icing "
                    "controls, or the PLCs behind them. CSW's airport contribution is the "
                    "server and management tier behind those systems.",
        },
        {
            "head": "No reach into endpoint fleets",
            "body": "Crew tablets and EFB devices, gate agent workstations in the general "
                    "case, kiosks, or handhelds. The EFB content distribution and "
                    "management servers are in reach; the tablets are not.",
        },
    ],
    "in_head": "In CSW's reach",
    "in_tag": "Ground IT estate",
    "in_reach": [
        "Flight dispatch, flight following, movement control servers",
        "Flight planning, weight and balance, performance systems",
        "Crew scheduling and crew tracking",
        "Datalink / ACARS <b>ground</b> gateways and AOC messaging hosts",
        "Reservations, inventory, ticketing",
        "Departure control, check-in, boarding, bag reconciliation",
        "Maintenance, engineering, MRO and airworthiness systems",
        "EFB content distribution and management servers",
        "Cargo management and air waybill systems",
        "Station and common-use <b>back-end</b> servers",
        "Identity, PKI, logging and patch infrastructure",
        "Ground handler and vendor remote-access hosts",
    ],
    "out_head": "Supplied outside CSW",
    "out_tag": "Evidence required",
    "out_reach": [
        "Aircraft avionics and onboard networks",
        "Flight-deck and cabin systems",
        "Pilot and crew EFB tablets",
        "The aircraft end of any datalink",
        "Baggage handling conveyor controls and PLCs",
        "Airfield lighting, boarding bridges, fuel controls",
        "Access control and CCTV field devices",
        "Kiosks, handhelds, gate workstations",
        "Ground support equipment telematics endpoints",
    ],
    "takeaway_tag": "Key Takeaway",
    "takeaway": "What remains is substantial, and for an airline it is where operational "
                "disruption actually originates. <b>Say the exclusions early</b> &mdash; "
                "naming them is the fastest way to hold an aviation customer's technical "
                "confidence.",
    "rail": [
        "OT-aware monitoring stays the controlling artifact for the field layer",
        "IT/OT boundary firewalls and the endpoint platform remain in place",
        "CSW complements those controls rather than replacing them",
    ],
}
