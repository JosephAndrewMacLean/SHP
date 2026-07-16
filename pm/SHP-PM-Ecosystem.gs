/**
 * SYNERGY HEALTH PARTNERS - SPINE GROWTH OPERATING SYSTEM (Google Sheets)
 * ----------------------------------------------------------------------
 * Setup: Extensions > Apps Script > paste ALL of this > Save > run buildEcosystem() > authorize.
 * Reload the sheet; use the "SHP PM" menu. Rebuild preserves your Status/%/Actual edits (by ID).
 *
 * Tabs: README, Dashboard (process tracker), Master Tasks (hierarchy + auto-rollups),
 *       Ideas Bank (impact/effort/cost), Weekly Spine Scorecard, Decisions & Blockers, By Owner.
 */
var DATA = {"headers": ["ID", "Level", "Parent ID", "Workstream (Category)", "Task / Subtask", "Needle-Mover", "Owner (Responsible)", "Authorizer", "Est. Hours", "Priority", "Start", "Due", "Depends On", "KPI / Definition of Done", "Status", "% Done", "Actual Hours", "Health", "Last Update", "Notes"], "rows": [["SP-A", "Task", "SPINE", "Spine Growth", "Qualification & Routing engine (send the RIGHT patient to the RIGHT surgeon)", "Yes", "Joe", "Gautam", "", "P1", "2026-07-16", "2026-07-31", "", "Every spine lead qualified + routed; qualified-% audited weekly", "Not Started", "", "", "", "", ""], ["SP-A.1", "Subtask", "SP-A", "Spine Growth", "Define 'qualified spine patient' rubric (insurance accepted + imaging-appropriate + pathway)", "Yes", "Joe", "Katie", 6, "P1", "2026-07-16", "2026-07-21", "", "1-page rubric approved by clinical", "Not Started", 0, 0, "", "", ""], ["SP-A.2", "Subtask", "SP-A", "Spine Growth", "Build surgical vs conservative/interventional decision tree", "Yes", "Joe", "Katie", 8, "P1", "2026-07-18", "2026-07-25", "SP-A.1", "Decision tree signed off by clinical", "Not Started", 0, 0, "", "", ""], ["SP-A.3", "Subtask", "SP-A", "Spine Growth", "Physician routing table - route surgical candidates to higher-converting surgeons", "Yes", "Joe", "Katie", 6, "P1", "2026-07-22", "2026-07-28", "SP-A.2", "Routing table approved (McCarty/Maslak/Varghese priority)", "Not Started", 0, 0, "", "", ""], ["SP-A.4", "Subtask", "SP-A", "Spine Growth", "Train call center + PL team on the rubric & routing", "Yes", "Kristen", "Joe", 8, "P1", "2026-07-26", "2026-07-31", "SP-A.3", "100% of reps + PLs trained", "Not Started", 0, 0, "", "", ""], ["SP-A.5", "Subtask", "SP-A", "Spine Growth", "Go-live + weekly qualified-% audit", "Yes", "Joe", "Gautam", 4, "P1", "2026-07-31", "2026-09-30", "SP-A.4", "Qualified-% reported on scorecard weekly", "Not Started", 0, 0, "", "", ""], ["SP-B", "Task", "SPINE", "Spine Growth", "Spine command center (target, scorecard, cadence)", "Yes", "Joe", "Gautam", "", "P1", "2026-07-16", "2026-07-22", "", "Scorecard live; target locked; war-room running", "Not Started", "", "", "", "", ""], ["SP-B.1", "Subtask", "SP-B", "Spine Growth", "Reconcile spine target (317 vs 321) & lock 47->65->72 ramp", "Yes", "Joe", "Gautam", 3, "P1", "2026-07-16", "2026-07-22", "", "One target confirmed", "Not Started", 0, 0, "", "", ""], ["SP-B.2", "Subtask", "SP-B", "Spine Growth", "Build & wire the Weekly Spine Scorecard", "Yes", "Joe", "Joe", 4, "P1", "2026-07-16", "2026-07-20", "", "Scorecard filled every Friday", "Not Started", 0, 0, "", "", ""], ["SP-B.3", "Subtask", "SP-B", "Spine Growth", "Establish Mon/Wed/Fri war-room + daily 4pm access check-in", "Yes", "Joe", "Gautam", 2, "P1", "2026-07-16", "2026-07-18", "", "Cadence on calendars", "Not Started", 0, 0, "", "", ""], ["SP-B.4", "Subtask", "SP-B", "Spine Growth", "Present surgical-conversion dependency to leadership (Salar routing / orders)", "Yes", "Joe", "Gautam", 4, "P1", "2026-07-20", "2026-07-24", "", "Leadership owns conversion workstream", "Not Started", 0, 0, "", "", ""], ["CC-A", "Task", "CC", "Call Center", "Spine intake script & qualification (the conversion hinge)", "Yes", "Kelly", "Joe", "", "P1", "2026-07-16", "2026-08-05", "", "Qualified-booking rate on dashboard and rising", "Not Started", "", "", "", "", ""], ["CC-A.1", "Subtask", "CC-A", "Call Center", "Draft qualify->route->capture spine script", "Yes", "Kelly", "Joe", 6, "P1", "2026-07-18", "2026-07-24", "SP-A.1", "Script live for spine calls", "Not Started", 0, 0, "", "", ""], ["CC-A.2", "Subtask", "CC-A", "Call Center", "Add insurance pre-screen step (no Medicaid -> Harmony Direct Pay)", "Yes", "Kelly", "Greg", 5, "P1", "2026-07-20", "2026-07-28", "CC-A.1", "Every spine call insurance-screened", "Not Started", 0, 0, "", "", ""], ["CC-A.3", "Subtask", "CC-A", "Call Center", "Make 'How did you hear' a required field", "Yes", "Kelly", "Joe", 3, "P1", "2026-07-20", "2026-07-25", "", "Source-capture 100%", "Not Started", 0, 0, "", "", ""], ["CC-A.4", "Subtask", "CC-A", "Call Center", "Same-week spine slot booking rule", "Yes", "Kelly", "Katie", 4, "P1", "2026-07-28", "2026-08-05", "", "Same-week spine fill tracked", "Not Started", 0, 0, "", "", ""], ["CC-A.5", "Subtask", "CC-A", "Call Center", "Train reps + go-live", "Yes", "Kelly", "Joe", 8, "P1", "2026-07-28", "2026-08-04", "CC-A.1;CC-A.2;CC-A.3", "All reps trained; script live", "Not Started", 0, 0, "", "", ""], ["CC-A.6", "Subtask", "CC-A", "Call Center", "Qualified-booking-rate metric live", "Yes", "Kelly", "Santosh", 4, "P1", "2026-08-01", "2026-08-10", "CC-A.5;ATTR-A", "Metric on dashboard", "Not Started", 0, 0, "", "", ""], ["CC-B", "Task", "CC", "Call Center", "Access & lost-patient recovery", "Yes", "Kelly", "Joe", "", "P1", "2026-07-22", "2026-08-22", "", "Access SLAs met; recovery queue running", "Not Started", "", "", "", "", ""], ["CC-B.1", "Subtask", "CC-B", "Call Center", "Self-reschedule recovery queue (166-patient signal)", "Yes", "Kelly", "Joe", 5, "P1", "2026-07-22", "2026-07-27", "", "Daily queue; recaptured count tracked", "Not Started", 0, 0, "", "", ""], ["CC-B.2", "Subtask", "CC-B", "Call Center", "Set access SLAs + dashboard (answer<30s, abandon<5%, callback<1hr)", "No", "Kelly", "Joe", 6, "P1", "2026-07-28", "2026-08-05", "", "SLAs monitored weekly", "Not Started", 0, 0, "", "", ""], ["CC-B.3", "Subtask", "CC-B", "Call Center", "After-hours / overflow coverage", "No", "Kelly", "Joe", 6, "P2", "2026-08-12", "2026-08-22", "", "No qualified call to voicemail", "Not Started", 0, 0, "", "", ""], ["CC-B.4", "Subtask", "CC-B", "Call Center", "Call QA scoring + weekly coaching", "No", "Kelly", "Joe", 8, "P2", "2026-08-05", "2026-08-15", "CC-A.5", "QA scored weekly", "Not Started", 0, 0, "", "", ""], ["CC-C", "Task", "CC", "Call Center", "AI call-center rollout (after foundations)", "No", "Kelly", "Gautam", "", "P2", "2026-09-01", "2026-09-20", "", "AI live; manual call-listening retired", "Not Started", "", "", "", "", ""], ["CC-C.1", "Subtask", "CC-C", "Call Center", "Scope AI (summarization + source detection + after-hours)", "No", "Kelly", "Gautam", 6, "P2", "2026-09-01", "2026-09-08", "CC-A.5", "Scope + vendor confirmed", "Not Started", 0, 0, "", "", ""], ["CC-C.2", "Subtask", "CC-C", "Call Center", "Pilot + go-live", "No", "Kelly", "Gautam", 12, "P2", "2026-09-08", "2026-09-20", "CC-C.1", "AI handling after-hours + QA", "Not Started", 0, 0, "", "", ""], ["PL-A", "Task", "PL", "Physician Liaison", "Tiered spine target-account universe (currently empty)", "Yes", "Kristen", "Kristen", "", "P1", "2026-07-16", "2026-08-03", "", "2x active spine accounts, all tiered with owner+cadence", "Not Started", "", "", "", "", ""], ["PL-A.1", "Subtask", "PL-A", "Physician Liaison", "Export current accounts from Map My Customer", "Yes", "Kristen", "Kristen", 3, "P1", "2026-07-16", "2026-07-19", "", "Account universe exported", "Not Started", 0, 0, "", "", ""], ["PL-A.2", "Subtask", "PL-A", "Physician Liaison", "Build feeder crosswalk (ortho, chiro, pain, urgent care, PCP, PT, PM&R, ER, WC/PI attorneys)", "Yes", "Kristen", "Kristen", 8, "P1", "2026-07-18", "2026-07-24", "PL-A.1", "Feeder list complete", "Not Started", 0, 0, "", "", ""], ["PL-A.3", "Subtask", "PL-A", "Physician Liaison", "Tier accounts 1/2/3 by qualified spine yield", "Yes", "Kristen", "Kristen", 6, "P1", "2026-07-23", "2026-07-29", "PL-A.2", "Every account tiered", "Not Started", 0, 0, "", "", ""], ["PL-A.4", "Subtask", "PL-A", "Physician Liaison", "Assign territory ownership; remove overlap across 5 hubs", "Yes", "Kristen", "Kristen", 5, "P1", "2026-07-28", "2026-08-03", "PL-A.3", "Zero overlap; owners assigned", "Not Started", 0, 0, "", "", ""], ["PL-A.5", "Subtask", "PL-A", "Physician Liaison", "Set visit cadence per tier", "Yes", "Kristen", "Kristen", 3, "P1", "2026-07-30", "2026-08-03", "PL-A.4", "Cadence documented per account", "Not Started", 0, 0, "", "", ""], ["PL-B", "Task", "PL", "Physician Liaison", "Recover & expand spine referrals (realistic lift, not 150)", "Yes", "Kristen", "Kristen", "", "P1", "2026-07-16", "2026-08-15", "", "Sean loss recovered; 2x spine field time", "Not Started", "", "", "", "", ""], ["PL-B.1", "Subtask", "PL-B", "Physician Liaison", "Recover Sean's lost referral accounts", "Yes", "Kristen", "Kristen", 8, "P1", "2026-07-16", "2026-07-24", "", "Lost accounts re-owned + re-visited", "Not Started", 0, 0, "", "", ""], ["PL-B.2", "Subtask", "PL-B", "Physician Liaison", "Double active spine accounts", "Yes", "Kristen", "Kristen", 20, "P1", "2026-07-29", "2026-08-15", "PL-A.3", "2x active spine accounts live", "Not Started", 0, 0, "", "", ""], ["PL-B.3", "Subtask", "PL-B", "Physician Liaison", "Double spine field time (accept lower ortho-account effort)", "Yes", "Kristen", "Joe", 6, "P1", "2026-07-29", "2026-08-15", "PL-A.4", "Spine visits doubled", "Not Started", 0, 0, "", "", ""], ["PL-C", "Task", "PL", "Physician Liaison", "Coaching to top-producer yield", "Yes", "Kristen", "Kristen", "", "P2", "2026-07-28", "2026-09-15", "", "Team NP/100 visits trending up", "Not Started", "", "", "", "", ""], ["PL-C.1", "Subtask", "PL-C", "Physician Liaison", "Capture Kristen's playbook (~70 NP/100 visits) into a script", "Yes", "Kristen", "Joe", 8, "P2", "2026-07-28", "2026-08-08", "", "Playbook written", "Not Started", 0, 0, "", "", ""], ["PL-C.2", "Subtask", "PL-C", "Physician Liaison", "Ride-along coaching program", "Yes", "Kristen", "Kristen", 20, "P2", "2026-08-01", "2026-09-15", "PL-C.1", "Coaching cadence running", "Not Started", 0, 0, "", "", ""], ["PL-C.3", "Subtask", "PL-C", "Physician Liaison", "Qualified-yield KPI replaces activity metrics", "Yes", "Kristen", "Santosh", 4, "P1", "2026-08-05", "2026-08-12", "ATTR-B", "KPI on scorecard", "Not Started", 0, 0, "", "", ""], ["PL-C.4", "Subtask", "PL-C", "Physician Liaison", "4th PL hire decision (trigger: Cody sustains 15 NP/wk)", "No", "Kristen", "Gautam", 4, "P2", "2026-09-01", "2026-09-15", "PL-B.2", "Hire/hold decided with data", "Not Started", 0, 0, "", "", ""], ["PL-D", "Task", "PL", "Physician Liaison", "Referral loop (what makes referrers keep sending)", "Yes", "Kristen", "Joe", "", "P1", "2026-07-22", "2026-08-18", "", "Same-week + closed-loop running", "Not Started", "", "", "", "", ""], ["PL-D.1", "Subtask", "PL-D", "Physician Liaison", "Referrer one-pager (deep spine bench, pathway, how to refer)", "Yes", "Randall", "Joe", 6, "P1", "2026-07-22", "2026-07-31", "", "One-pager printed + digital", "Not Started", 0, 0, "", "", ""], ["PL-D.2", "Subtask", "PL-D", "Physician Liaison", "Same-week access reserved for referrals", "Yes", "Kristen", "Katie", 3, "P1", "2026-08-01", "2026-08-08", "CC-A.4", "Referral same-week fill tracked", "Not Started", 0, 0, "", "", ""], ["PL-D.3", "Subtask", "PL-D", "Physician Liaison", "Closed-loop report-back to referrers", "Yes", "Kristen", "Joe", 8, "P1", "2026-08-08", "2026-08-18", "", "Report-back rate tracked", "Not Started", 0, 0, "", "", ""], ["B2C-A", "Task", "B2C", "B2C / Organic", "Spine organic demand rebuild (fix the -71 B2C hole)", "Yes", "Randall", "Joe", "", "P1", "2026-07-16", "2026-09-20", "", "Non-branded spine impressions + NPs recovering", "Not Started", "", "", "", "", ""], ["B2C-A.1", "Subtask", "B2C-A", "B2C / Organic", "SEMrush spine keyword-gap vs MOS/St Clair/MI Head&Spine", "Yes", "Randall", "Joe", 6, "P1", "2026-07-18", "2026-07-23", "", "Gap list -> page plan", "Not Started", 0, 0, "", "", ""], ["B2C-A.2", "Subtask", "B2C-A", "B2C / Organic", "Shift 80% SEO to spine; ship 2-3 spine pages/week", "Yes", "Randall", "Joe", 30, "P1", "2026-07-16", "2026-08-30", "B2C-A.1", "2-3 spine pages/wk shipped", "Not Started", 0, 0, "", "", ""], ["B2C-A.3", "Subtask", "B2C-A", "B2C / Organic", "Publish 5 spine condition hubs (MD-reviewed)", "Yes", "Randall", "Clinical", 24, "P2", "2026-07-25", "2026-09-20", "B2C-A.2", "5 hubs live + indexed", "Not Started", 0, 0, "", "", ""], ["B2C-A.4", "Subtask", "B2C-A", "B2C / Organic", "Spine differentiation messaging (deep bench) on spine pages", "Yes", "Randall", "Joe", 6, "P1", "2026-07-28", "2026-08-05", "", "Differentiation live", "Not Started", 0, 0, "", "", ""], ["B2C-A.5", "Subtask", "B2C-A", "B2C / Organic", "FAQ / schema on spine pages", "No", "Randall", "Joe", 10, "P2", "2026-08-20", "2026-09-10", "B2C-A.3", "Schema valid in GSC", "Not Started", 0, 0, "", "", ""], ["B2C-B", "Task", "B2C", "B2C / Organic", "Paid efficiency & booking capture", "Yes", "Paul", "Joe", "", "P1", "2026-07-16", "2026-08-31", "", "Spine CPA to target; more free website booking", "Not Started", "", "", "", "", ""], ["B2C-B.1", "Subtask", "B2C-B", "B2C / Organic", "Optimize free website spine booking path", "Yes", "Paul", "Joe", 8, "P2", "2026-08-01", "2026-08-15", "", "Website spine booking share up", "Not Started", 0, 0, "", "", ""], ["B2C-B.2", "Subtask", "B2C-B", "B2C / Organic", "Trim least-efficient paid Zocdoc spine spend", "Yes", "Paul", "Joe", 4, "P1", "2026-08-10", "2026-08-20", "ATTR-A", "Cost/captured down", "Not Started", 0, 0, "", "", ""], ["B2C-B.3", "Subtask", "B2C-B", "B2C / Organic", "Rein in spine CPA toward target (was $200->$2,000)", "Yes", "Paul", "Joe", 10, "P1", "2026-08-01", "2026-08-31", "ATTR-A", "CPA trending to target", "Not Started", 0, 0, "", "", ""], ["B2C-B.4", "Subtask", "B2C-B", "B2C / Organic", "Fix CWV / mobile perf regression (agency)", "No", "Cardinal", "Paul", 16, "P1", "2026-07-25", "2026-08-15", "", "Good URLs recovering in GSC", "Not Started", 0, 0, "", "", ""], ["ATTR-A", "Task", "ATTR", "Attribution / Systems", "Line conversion tracking fix (WEEK-1 BLOCKER)", "Yes", "Joe", "Gautam", "", "P1", "2026-07-16", "2026-07-23", "", "Booked-patient tracking validated; unblocks paid changes", "Not Started", "", "", "", "", ""], ["ATTR-A.1", "Subtask", "ATTR-A", "Attribution / Systems", "Diagnose the compliance issue with Line", "Yes", "Joe", "Gautam", 4, "P1", "2026-07-16", "2026-07-18", "", "Root cause identified", "Not Started", 0, 0, "", "", ""], ["ATTR-A.2", "Subtask", "ATTR-A", "Attribution / Systems", "Implement fix with Line + Paul", "Yes", "Paul", "Joe", 8, "P1", "2026-07-18", "2026-07-22", "ATTR-A.1", "Fix deployed", "Not Started", 0, 0, "", "", ""], ["ATTR-A.3", "Subtask", "ATTR-A", "Attribution / Systems", "Validate booked-patient tracking end-to-end", "Yes", "Santosh", "Joe", 4, "P1", "2026-07-22", "2026-07-23", "ATTR-A.2", "Tracking validated", "Not Started", 0, 0, "", "", ""], ["ATTR-B", "Task", "ATTR", "Attribution / Systems", "Attribution integrity (stop 'spray and pray')", "Yes", "Santosh", "Joe", "", "P1", "2026-07-20", "2026-08-12", "", "Referrals + NPs correctly attributed", "Not Started", "", "", "", "", ""], ["ATTR-B.1", "Subtask", "ATTR-B", "Attribution / Systems", "Map My Customer <-> NextGen crosswalk", "Yes", "Santosh", "Joe", 12, "P1", "2026-07-28", "2026-08-10", "", "Referrals source-attributed", "Not Started", 0, 0, "", "", ""], ["ATTR-B.2", "Subtask", "ATTR-B", "Attribution / Systems", "Stop referring-physician field overwrite + add change log", "Yes", "Santosh", "Joe", 8, "P1", "2026-08-01", "2026-08-12", "ATTR-B.1", "Source field preserved", "Not Started", 0, 0, "", "", ""], ["ATTR-B.3", "Subtask", "ATTR-B", "Attribution / Systems", "Validate B2C vs B2B spine NP split", "Yes", "Santosh", "Joe", 6, "P1", "2026-07-20", "2026-07-28", "", "Validated split + match-rate", "Not Started", 0, 0, "", "", ""], ["ATTR-B.4", "Subtask", "ATTR-B", "Attribution / Systems", "Build 3-layer wedding-cake funnel (visits->scheduled->NP)", "Yes", "Joe", "Joe", 8, "P1", "2026-07-22", "2026-07-30", "", "Funnel published", "Not Started", 0, 0, "", "", ""], ["ATTR-B.5", "Subtask", "ATTR-B", "Attribution / Systems", "Root-cause visits-up-NPs-flat gap", "Yes", "Joe", "Joe", 6, "P1", "2026-07-28", "2026-08-05", "ATTR-B.3;ATTR-B.4", "Root cause + fixes assigned", "Not Started", 0, 0, "", "", ""], ["ATTR-C", "Task", "ATTR", "Attribution / Systems", "Reporting & systems foundation", "No", "Santosh", "Gautam", "", "P2", "2026-07-18", "2026-09-05", "", "Single reporting layer; scheduling recommendation", "Not Started", "", "", "", "", ""], ["ATTR-C.1", "Subtask", "ATTR-C", "Attribution / Systems", "Scheduling systems recommendation to EMT (OrthoPlex/NextGen/hybrid)", "No", "Santosh", "Gautam", 12, "P2", "2026-07-18", "2026-08-01", "", "Recommendation delivered", "Not Started", 0, 0, "", "", ""], ["ATTR-C.2", "Subtask", "ATTR-C", "Attribution / Systems", "Select reporting tool (e.g. Pulse Insights)", "No", "Joe", "Gautam", 6, "P2", "2026-08-01", "2026-08-15", "", "Tool chosen + piloted", "Not Started", 0, 0, "", "", ""], ["ATTR-C.3", "Subtask", "ATTR-C", "Attribution / Systems", "Automate weekly scorecard reporting", "No", "Santosh", "Joe", 10, "P2", "2026-08-25", "2026-09-05", "ATTR-C.2", "Auto-report running", "Not Started", 0, 0, "", "", ""], ["GOV-A", "Task", "GOV", "Governance / Brand", "Brand consistency & rebrand cleanup", "No", "Randall", "Joe", "", "P2", "2026-07-18", "2026-08-20", "", "One brand standard; legacy migrated", "Not Started", "", "", "", "", ""], ["GOV-A.1", "Subtask", "GOV-A", "Governance / Brand", "Fix Troy Maps/GBP + kill 'Oakland MRI' misdirect", "Yes", "Paul", "Joe", 6, "P1", "2026-07-18", "2026-07-26", "", "Troy listings correct", "Not Started", 0, 0, "", "", ""], ["GOV-A.2", "Subtask", "GOV-A", "Governance / Brand", "Apply brand standards (Scrubs #49A698, Goldplay, voice) to assets", "No", "Randall", "Joe", 10, "P2", "2026-07-28", "2026-08-10", "", "Brand standard held", "Not Started", 0, 0, "", "", ""], ["GOV-A.3", "Subtask", "GOV-A", "Governance / Brand", "Finish Mendelson->Synergy migration (bill-pay, YouTube, LinkedIn)", "No", "Paul", "Joe", 8, "P2", "2026-08-01", "2026-08-20", "", "Legacy properties migrated", "Not Started", 0, 0, "", "", ""], ["GOV-A.4", "Subtask", "GOV-A", "Governance / Brand", "Harmony Health Direct Pay rebrand rollout", "No", "Greg", "Gautam", 10, "P2", "2026-07-28", "2026-08-15", "", "Rebrand live across channels", "Not Started", 0, 0, "", "", ""], ["GOV-B", "Task", "GOV", "Governance / Brand", "Governance & compliance", "No", "Joe", "Gautam", "", "P1", "2026-07-16", "2026-09-30", "", "Decisions tracked; ortho standard held; compliance gate on", "Not Started", "", "", "", "", ""], ["GOV-B.1", "Subtask", "GOV-B", "Governance / Brand", "Maintain leadership decisions log (4 open decisions)", "No", "Joe", "Gautam", 4, "P1", "2026-07-16", "2026-09-30", "", "Decisions log current weekly", "Not Started", 0, 0, "", "", ""], ["GOV-B.2", "Subtask", "GOV-B", "Governance / Brand", "Hold ortho over-delivery standard (130-140 NP/wk)", "Yes", "Katie", "Gautam", 8, "P1", "2026-07-16", "2026-09-30", "", "Ortho >=130/wk sustained", "Not Started", 0, 0, "", "", ""], ["GOV-B.3", "Subtask", "GOV-B", "Governance / Brand", "Compliance review gate for all clinical content", "No", "Clinical", "Joe", 6, "P1", "2026-07-16", "2026-09-30", "", "No clinical content ships unreviewed", "Not Started", 0, 0, "", "", ""]], "owners": ["Joe", "Kristen", "Cody", "Jasmine", "Kelly", "Randall", "Paul", "Santosh", "Katie", "Greg", "Cardinal", "Line", "Clinical", "Gautam"], "authorizers": ["Gautam", "Joe", "Kristen", "Katie", "Clinical", "Greg", "Santosh"], "statuses": ["Not Started", "In Progress", "Blocked", "Done", "Deferred"], "priorities": ["P1", "P2", "P3"], "levels": ["Task", "Subtask"], "needle": ["Yes", "No"], "scoreWeeks": [["2026-07-20", 51], ["2026-07-27", 54], ["2026-08-03", 57], ["2026-08-10", 59], ["2026-08-17", 62], ["2026-08-24", 65], ["2026-08-31", 66], ["2026-09-07", 68], ["2026-09-14", 70], ["2026-09-21", 71], ["2026-09-28", 72]], "decisions": [["D-1", "Confirm spine target: 317/mo vs 321/mo", "Gautam; Joe; Santosh", "Open", "2026-07-22"], ["D-2", "Approve routing surgical candidates to higher-converting surgeons", "Gautam; Katie; Physicians", "Open", "2026-07-29"], ["D-3", "Green-light 4th PL hire trigger + AI call-center timing", "Gautam; Joe; Kristen", "Open", "2026-09-15"], ["D-4", "Leadership owns surgical-conversion (orders) workstream", "Gautam; Katie; Physicians", "Open", "2026-07-24"], ["B-1", "BLOCKER: Line conversion tracking non-functional (compliance)", "Joe; Santosh; Paul; Line", "Open", "2026-07-23"], ["B-2", "Structural: no Medicaid / no hospital affiliation / no portal", "Gautam; Santosh", "Monitoring", "2026-09-30"]], "ideaHdr": ["Idea ID", "Idea (human-executable)", "Category", "Evidence - what works / has worked", "Impact", "Effort", "Cost", "Quadrant", "Owner", "Linked Task", "Status"], "ideas": [["I-01", "Shift spine booking to the free website path; steer reps to it", "Booking", "Website captures 74.7% of booked NPs at $0 vs paid Zocdoc 52-57%", "High", "Low", "$", "", "Paul", "B2C-B.1", "Not Started"], ["I-02", "Make 'how did you hear' + insurance pre-screen mandatory at intake", "Call Center", "Source asked only 60-70%; no-Medicaid mismatch drops patients post-click", "High", "Low", "$", "", "Kelly", "CC-A", "Not Started"], ["I-03", "Recover the 166 self-reschedulers with a daily re-book queue", "Call Center", "166 canceled/no-show patients self-rescheduled online and KEPT - pure recapture", "Medium", "Low", "$", "", "Kelly", "CC-B.1", "Not Started"], ["I-04", "Recover Sean's lost referral accounts first", "Physician Liaison", "Sean's departure dented spine ~2-3 NP/week - fastest referral win", "Medium", "Low", "$", "", "Kristen", "PL-B.1", "Not Started"], ["I-05", "Route surgical candidates to higher-converting surgeons", "Spine", "Salar absorbs ~21% of spine NPs (303) at ~3% conversion; McCarty/Maslak convert", "High", "Medium", "$", "", "Joe", "SP-A.3", "Not Started"], ["I-06", "Replicate Kristen's PL playbook via ride-alongs", "Physician Liaison", "Kristen ~70 NP/100 visits vs team 6-40 - spread the method", "High", "Medium", "$", "", "Kristen", "PL-C.1", "Not Started"], ["I-07", "Reserve + market same-week spine access", "Spine", "Same-week access is the verified differentiator; drives conversion", "High", "Medium", "$", "", "Kelly", "CC-A.4", "Not Started"], ["I-08", "Scale PT-led, UGC-style athlete video storytelling", "Content/Social", "Flagged in creative audit as the strongest, most authentic asset type", "High", "Medium", "$$", "", "Randall", "B2C-A", "Not Started"], ["I-09", "Interventional pain as the 'front door' to keep patients in-system", "Spine", "Deep bench (4 interventional MDs); conservative-first keeps patients until surgical", "High", "Medium", "$", "", "Joe", "SP-A.2", "Not Started"], ["I-10", "Closed-loop report-back to referrers after each visit", "Physician Liaison", "Best practice - referrers keep sending when kept informed", "High", "Medium", "$", "", "Kristen", "PL-D.3", "Not Started"], ["I-11", "Tier spine feeder accounts like the attorney-referral model", "Physician Liaison", "The tiered attorney-referral model already works internally", "High", "Medium", "$", "", "Kristen", "PL-A.3", "Not Started"], ["I-12", "Fix Troy Maps/GBP + kill the 'Oakland MRI' misdirect", "Local/Brand", "Local 'near me' intent is highest-converting; Troy pin/calls currently misdirect", "High", "Low", "$", "", "Paul", "GOV-A.1", "Not Started"], ["I-13", "Review-velocity program (BirdEye/Podium)", "Reputation", "96% recommend / 82 sentiment; reviews drive local rankings + trust", "Medium", "Low", "$", "", "Randall", "", "Not Started"], ["I-14", "Physician-authored spine condition hubs (5)", "Content/SEO", "Provider section already ranks (182K impressions); E-E-A-T wins YMYL", "High", "High", "$$", "", "Randall", "B2C-A.3", "Not Started"], ["I-15", "Kill worst-CPA paid Zocdoc 'Sponsored' spine spend", "Paid", "Zocdoc Sponsored ~52% capture, ~$136/captured - the worst efficiency", "Medium", "Low", "$", "", "Paul", "B2C-B.2", "Not Started"], ["I-16", "Apply the ortho promo playbook to spine (Tue-Thu pushes)", "Demand", "Ortho turned 75%->125% of plan in ~60 days using promos + ops", "Medium", "Low", "$", "", "Joe", "", "Not Started"], ["I-17", "Ship spine differentiation messaging (MIS, neurosurgeon, younger surgeons)", "Messaging", "Creative audit: spine has NO differentiation anywhere today", "Medium", "Low", "$", "", "Randall", "B2C-A.4", "Not Started"], ["I-18", "Provider-to-provider lunch-and-learns with spine surgeons", "Physician Liaison", "Standard high-yield PL tactic; warm ortho relationships convert to spine", "Medium", "Medium", "$$", "", "Kristen", "PL-B.2", "Not Started"], ["I-19", "Referrer one-pager leave-behind (deep bench + how to refer)", "Physician Liaison", "PL best practice; makes referring frictionless", "Medium", "Low", "$", "", "Randall", "PL-D.1", "Not Started"], ["I-20", "Direct-pay + financing path for non-covered spine candidates", "Access/Revenue", "Harmony Direct Pay exists; recovers otherwise-lost non-covered patients", "Medium", "Medium", "$$", "", "Greg", "SP-A.9", "Not Started"], ["I-21", "Weekly OODA scorecard review (2-3 problems/wk, measure, stack)", "Operating", "This is leadership's own proven method behind the ortho turnaround", "High", "Low", "$", "", "Joe", "SP-B.2", "Not Started"], ["I-22", "FAQ + schema on spine pages for AI-Overview citations", "SEO/AIO", "AI answers on 40%+ healthcare SERPs; SHP has zero FAQ schema", "Medium", "Medium", "$", "", "Randall", "B2C-A.5", "Not Started"], ["I-23", "Community events (Blue Water Festival tent, chambers) + screening booth", "Community", "Local presence builds trust; Haley/Mary already running events", "Medium", "Medium", "$$", "", "Haley", "", "Not Started"], ["I-24", "Provider-spotlight campaigns featuring spine surgeons", "Content", "Physician authority already indexed; humanizes the bench", "Medium", "Medium", "$", "", "Haley", "", "Not Started"], ["I-25", "Fix CWV / mobile performance regression", "Technical", "0 Good URLs since ~May 1; 70%+ of healthcare search is mobile", "Medium", "Medium", "$", "", "Cardinal", "B2C-B.4", "Not Started"], ["I-26", "Hospital-system / medical-association link building", "Authority/PR", "0 such links since 2012; strong competitors have 400+ referring domains", "Medium", "High", "$", "", "Randall", "", "Not Started"], ["I-27", "AI call-center for after-hours + source detection", "Call Center", "Phone-driven; 6-8 hrs/wk manual call-listening today", "Medium", "High", "$$", "", "Kelly", "CC-C", "Not Started"], ["I-28", "GLP-1 / ancillary email cadence (Dr. Abood)", "Email/Ancillary", "Ancillary grew +22%; existing content to repurpose", "Low", "Low", "$", "", "Randall", "", "Not Started"]], "_last": 80};
var LAST = DATA._last;
var S = {README:'README',DASH:'Dashboard',TASKS:'Master Tasks',IDEAS:'Ideas Bank',
         SCORE:'Weekly Spine Scorecard',DEC:'Decisions & Blockers',OWNER:'By Owner'};
// Master Tasks columns (1-based): A..T
var C={ID:1,LEVEL:2,PARENT:3,WS:4,NAME:5,NEEDLE:6,OWNER:7,AUTH:8,EST:9,PRIO:10,START:11,
       DUE:12,DEP:13,KPI:14,STATUS:15,PCT:16,ACT:17,HEALTH:18,UPD:19,NOTES:20};

function onOpen(){
  SpreadsheetApp.getUi().createMenu('SHP PM')
    .addItem('Build / Rebuild ecosystem','buildEcosystem')
    .addItem('Refresh dashboard','refreshDashboard')
    .addItem('Generate owner tabs','generateOwnerTabs')
    .addSeparator().addItem('About','aboutBox').addToUi();
}
function aboutBox(){SpreadsheetApp.getUi().alert('SHP Spine Growth Operating System\n'+
  (LAST-1)+' rows ('+countLevel_('Task')+' tasks / '+countLevel_('Subtask')+' subtasks), '+
  DATA.ideas.length+' ideas.\nGates: 65/wk by Aug 30, 72/wk by Sept 30.');}
function countLevel_(l){var n=0;DATA.rows.forEach(function(r){if(r[1]===l)n++;});return n;}

function buildEcosystem(){
  var ss=SpreadsheetApp.getActiveSpreadsheet();
  var prior=readPrior_(ss);
  buildTasks_(ss,prior); buildIdeas_(ss); buildDashboard_(ss);
  buildScore_(ss); buildDec_(ss); buildOwner_(ss); buildReadme_(ss);
  order_(ss,[S.README,S.DASH,S.TASKS,S.IDEAS,S.SCORE,S.DEC,S.OWNER]);
  var d=ss.getSheetByName('Sheet1'); if(d&&ss.getSheets().length>1){try{ss.deleteSheet(d);}catch(e){}}
  ss.setActiveSheet(gc_(ss,S.DASH));
  SpreadsheetApp.getUi().alert('Operating system built. Use the "SHP PM" menu to refresh or generate owner tabs.');
}
function gc_(ss,n){return ss.getSheetByName(n)||ss.insertSheet(n);}
function d_(s){if(!s)return '';var p=String(s).split('-');return p.length===3?new Date(+p[0],+p[1]-1,+p[2]):s;}
function readPrior_(ss){var sh=ss.getSheetByName(S.TASKS),m={};if(!sh)return m;var n=sh.getLastRow();if(n<2)return m;
  var v=sh.getRange(2,1,n-1,C.NOTES).getValues();v.forEach(function(r){if(r[0])m[r[0]]={st:r[C.STATUS-1],pct:r[C.PCT-1],act:r[C.ACT-1],upd:r[C.UPD-1],notes:r[C.NOTES-1]};});return m;}

/* ---------------- MASTER TASKS ---------------- */
function buildTasks_(ss,prior){
  var sh=gc_(ss,S.TASKS);sh.clear();sh.getRange(1,1,1,DATA.headers.length).setValues([DATA.headers])
    .setFontWeight('bold').setFontColor('#ffffff').setBackground('#363C40');
  var rows=DATA.rows.map(function(t){var r=t.slice();r[C.START-1]=d_(r[C.START-1]);r[C.DUE-1]=d_(r[C.DUE-1]);
    var pr=prior[r[0]];if(pr){if(pr.st)r[C.STATUS-1]=pr.st;if(pr.pct!=='' && pr.pct!=null)r[C.PCT-1]=pr.pct;
      if(pr.act!=='' && pr.act!=null)r[C.ACT-1]=pr.act;if(pr.upd)r[C.UPD-1]=pr.upd;if(pr.notes)r[C.NOTES-1]=pr.notes;}
    return r;});
  sh.getRange(2,1,rows.length,DATA.headers.length).setValues(rows);
  sh.setFrozenRows(1);sh.setFrozenColumns(1);
  sh.getRange(2,C.START,rows.length,1).setNumberFormat('yyyy-mm-dd');
  sh.getRange(2,C.DUE,rows.length,1).setNumberFormat('yyyy-mm-dd');
  // rollup formulas on Task rows; Health on every row
  for(var i=0;i<rows.length;i++){var r=2+i;var lvl=rows[i][C.LEVEL-1];
    if(lvl==='Task'){
      sh.getRange(r,C.EST).setFormula('=SUMIF($C$2:$C$'+LAST+',$A'+r+',$I$2:$I$'+LAST+')');
      sh.getRange(r,C.PCT).setFormula('=IFERROR(ROUND(SUMPRODUCT(($C$2:$C$'+LAST+'=$A'+r+')*$I$2:$I$'+LAST+'*$P$2:$P$'+LAST+')/SUMIF($C$2:$C$'+LAST+',$A'+r+',$I$2:$I$'+LAST+'),0),0)');
      sh.getRange(r,C.ACT).setFormula('=SUMIF($C$2:$C$'+LAST+',$A'+r+',$Q$2:$Q$'+LAST+')');
    }
    sh.getRange(r,C.HEALTH).setFormula('=IF($P'+r+'="","",IF($P'+r+'>=100,"Done",IF(AND($L'+r+'<>"",$L'+r+'<TODAY()),"Behind",IF(OR(AND($I'+r+'>0,$Q'+r+'>$I'+r+'*1.1),AND($L'+r+'<>"",($L'+r+'-TODAY())<=3,$P'+r+'<50)),"At Risk","On Track"))))');
  }
  var w={1:78,2:70,3:78,4:130,5:340,6:60,7:95,8:90,9:60,10:60,11:88,12:88,13:110,14:250,15:105,16:60,17:60,18:80,19:90,20:150};
  Object.keys(w).forEach(function(k){sh.setColumnWidth(+k,w[k]);});
  sh.getRange(2,1,rows.length,DATA.headers.length).setVerticalAlignment('top').setWrap(true);
  dv_(sh,C.STATUS,rows.length,DATA.statuses);dv_(sh,C.PRIO,rows.length,DATA.priorities);
  dv_(sh,C.OWNER,rows.length,DATA.owners);dv_(sh,C.AUTH,rows.length,DATA.authorizers);
  dv_(sh,C.NEEDLE,rows.length,DATA.needle);
  var R=[];
  R.push(rule_(sh,'=$B2="Task"',C.ID,C.NOTES,rows.length,'#e8edf0',true));
  R.push(rule_(sh,'=$F2="Yes"',C.NEEDLE,C.NEEDLE,rows.length,'#fde2b3',false));
  R.push(cell_(sh,C.STATUS,rows.length,'Done','#b7e1cd'));
  R.push(cell_(sh,C.STATUS,rows.length,'In Progress','#fce8b2'));
  R.push(cell_(sh,C.STATUS,rows.length,'Blocked','#f4c7c3'));
  R.push(cell_(sh,C.HEALTH,rows.length,'Behind','#ea4335',true));
  R.push(cell_(sh,C.HEALTH,rows.length,'At Risk','#fce8b2'));
  R.push(cell_(sh,C.HEALTH,rows.length,'On Track','#d9ead3'));
  R.push(cell_(sh,C.HEALTH,rows.length,'Done','#b7e1cd'));
  sh.setConditionalFormatRules(R);
}
function dv_(sh,col,n,list){sh.getRange(2,col,n,1).setDataValidation(
  SpreadsheetApp.newDataValidation().requireValueInList(list,true).setAllowInvalid(false).build());}
function cell_(sh,col,n,val,color,white){var L=colL_(col);var b=SpreadsheetApp.newConditionalFormatRule()
  .whenFormulaSatisfied('=$'+L+'2="'+val+'"').setBackground(color).setRanges([sh.getRange(2,col,n,1)]);
  if(white)b.setFontColor('#ffffff');return b.build();}
function rule_(sh,formula,c1,c2,n,color,bold){var b=SpreadsheetApp.newConditionalFormatRule()
  .whenFormulaSatisfied(formula).setBackground(color).setRanges([sh.getRange(2,c1,n,c2-c1+1)]);
  if(bold)b.setBold(true);return b.build();}
function colL_(c){var s='';while(c>0){var m=(c-1)%26;s=String.fromCharCode(65+m)+s;c=(c-m-1)/26;}return s;}

/* ---------------- IDEAS BANK ---------------- */
function buildIdeas_(ss){
  var sh=gc_(ss,S.IDEAS);sh.clear();
  sh.getRange('A1').setValue('IDEAS BANK - evidence-based, scored by Impact / Effort / Cost. Promote winners to Master Tasks.')
    .setFontWeight('bold').setFontColor('#363C40').setFontSize(12);
  sh.getRange(3,1,1,DATA.ideaHdr.length).setValues([DATA.ideaHdr])
    .setFontWeight('bold').setFontColor('#ffffff').setBackground('#54819B');
  sh.getRange(4,1,DATA.ideas.length,DATA.ideaHdr.length).setValues(DATA.ideas);
  // Quadrant formula (col H=8) from Impact(E=5) & Effort(F=6)
  for(var i=0;i<DATA.ideas.length;i++){var r=4+i;
    sh.getRange(r,8).setFormula('=IFS(AND(OR($E'+r+'="High",$E'+r+'="Medium"),$F'+r+'="Low"),"Quick Win",AND($E'+r+'="High",OR($F'+r+'="Medium",$F'+r+'="High")),"Big Bet",AND($E'+r+'="Medium",$F'+r+'="Medium"),"Incremental",AND($E'+r+'="Medium",$F'+r+'="High"),"Reconsider",AND($E'+r+'="Low",$F'+r+'="Low"),"Fill-in",TRUE,"Avoid")');
  }
  sh.setFrozenRows(3);
  var w={1:60,2:300,3:130,4:300,5:75,6:70,7:55,8:110,9:90,10:100,11:100};
  Object.keys(w).forEach(function(k){sh.setColumnWidth(+k,w[k]);});
  sh.getRange(4,1,DATA.ideas.length,DATA.ideaHdr.length).setVerticalAlignment('top').setWrap(true);
  dvR_(sh,4,5,DATA.ideas.length,['High','Medium','Low']);
  dvR_(sh,4,6,DATA.ideas.length,['High','Medium','Low']);
  dvR_(sh,4,7,DATA.ideas.length,['$','$$','$$$']);
  dvR_(sh,4,11,DATA.ideas.length,DATA.statuses);
  var n=DATA.ideas.length;var R=[];
  R.push(qc_(sh,8,n,'Quick Win','#b7e1cd'));R.push(qc_(sh,8,n,'Big Bet','#9fc5e8'));
  R.push(qc_(sh,8,n,'Incremental','#fce8b2'));R.push(qc_(sh,8,n,'Fill-in','#efefef'));
  R.push(qc_(sh,8,n,'Reconsider','#f9cb9c'));R.push(qc_(sh,8,n,'Avoid','#f4c7c3'));
  R.push(qc2_(sh,5,n,'High','#d9ead3'));R.push(qc2_(sh,6,n,'Low','#d9ead3'));R.push(qc2_(sh,6,n,'High','#f4c7c3'));
  sh.setConditionalFormatRules(R);
  // quadrant summary
  var base=6+n;
  sh.getRange(base,1).setValue('QUADRANT SUMMARY').setFontWeight('bold');
  var quads=['Quick Win','Big Bet','Incremental','Fill-in','Reconsider','Avoid'];
  sh.getRange(base+1,1,1,2).setValues([['Quadrant','Count']]).setFontWeight('bold');
  quads.forEach(function(q,i){sh.getRange(base+2+i,1).setValue(q);
    sh.getRange(base+2+i,2).setFormula('=COUNTIF($H$4:$H$'+(3+n)+',"'+q+'")');});
  sh.getRange(base,4).setValue('Do the Quick Wins first; schedule Big Bets; ignore Avoid. Set Linked Task when promoted.').setFontColor('#888888');
}
function dvR_(sh,row,col,n,list){sh.getRange(row,col,n,1).setDataValidation(
  SpreadsheetApp.newDataValidation().requireValueInList(list,true).setAllowInvalid(false).build());}
function qc_(sh,col,n,val,color){return SpreadsheetApp.newConditionalFormatRule()
  .whenFormulaSatisfied('=$'+colL_(col)+'4="'+val+'"').setBackground(color).setRanges([sh.getRange(4,col,n,1)]).build();}
function qc2_(sh,col,n,val,color){return SpreadsheetApp.newConditionalFormatRule()
  .whenFormulaSatisfied('=$'+colL_(col)+'4="'+val+'"').setBackground(color).setRanges([sh.getRange(4,col,n,1)]).build();}

/* ---------------- DASHBOARD (process tracker) ---------------- */
function buildDashboard_(ss){
  var sh=gc_(ss,S.DASH);sh.clear();var T="'"+S.TASKS+"'";var lo=2,hi=LAST;
  var subF="("+T+"!$B$"+lo+":$B$"+hi+'="Subtask")';
  var est=T+"!$I$"+lo+":$I$"+hi, pct=T+"!$P$"+lo+":$P$"+hi, act=T+"!$Q$"+lo+":$Q$"+hi,
      need=T+"!$F$"+lo+":$F$"+hi, hea=T+"!$R$"+lo+":$R$"+hi, own=T+"!$G$"+lo+":$G$"+hi, st=T+"!$O$"+lo+":$O$"+hi;
  sh.getRange('A1').setValue('SPINE GROWTH - PROCESS TRACKER').setFontSize(16).setFontWeight('bold').setFontColor('#363C40');
  sh.getRange('A2').setValue('Gates: clear 65/wk by Aug 30  |  operate at 72/wk by Sept 30    (auto from Master Tasks - SHP PM > Refresh dashboard)').setFontColor('#54819B');
  var tiles=[
    ['Overall % done (effort-weighted)','=IFERROR(ROUND(SUMPRODUCT('+subF+'*'+est+'*'+pct+')/SUMPRODUCT('+subF+'*'+est+'),0)&"%","0%")'],
    ['Needle-mover % done','=IFERROR(ROUND(SUMPRODUCT('+subF+'*('+need+'="Yes")*'+est+'*'+pct+')/SUMPRODUCT('+subF+'*('+need+'="Yes")*'+est+'),0)&"%","0%")'],
    ['Est. hours (subtasks)','=ROUND(SUMPRODUCT('+subF+'*'+est+'),0)'],
    ['Actual hours logged','=ROUND(SUMPRODUCT('+subF+'*'+act+'),0)'],
    ['Effort burn (actual/est)','=IFERROR(ROUND(SUMPRODUCT('+subF+'*'+act+')/SUMPRODUCT('+subF+'*'+est+')*100,0)&"%","0%")'],
    ['Subtasks total','=SUMPRODUCT('+subF+'*1)']
  ];
  sh.getRange(4,1).setValue('PROGRESS').setFontWeight('bold');
  for(var i=0;i<tiles.length;i++){var r=5+i;sh.getRange(r,1).setValue(tiles[i][0]);
    sh.getRange(r,2).setFormula(tiles[i][1]).setFontWeight('bold').setFontColor('#49A698');}
  // Health
  sh.getRange(4,4).setValue('HEALTH (subtasks)').setFontWeight('bold');
  var hs=[['On Track','#d9ead3'],['At Risk','#fce8b2'],['Behind','#f4c7c3'],['Done','#b7e1cd']];
  hs.forEach(function(h,i){var r=5+i;sh.getRange(r,4).setValue(h[0]).setBackground(h[1]);
    sh.getRange(r,5).setFormula('=SUMPRODUCT('+subF+'*('+hea+'="'+h[0]+'"))').setFontWeight('bold');});
  sh.getRange(9,4).setValue('Blocked').setBackground('#f4c7c3');
  sh.getRange(9,5).setFormula('=SUMPRODUCT('+subF+'*('+st+'="Blocked"))').setFontWeight('bold');
  sh.getRange(10,4).setValue('Overdue (open, past due)');
  sh.getRange(10,5).setFormula('=SUMPRODUCT('+subF+'*('+T+"!$L$"+lo+':$L$'+hi+'<TODAY())*('+T+"!$L$"+lo+':$L$'+hi+'<>"")*('+pct+'<100))').setFontWeight('bold').setFontColor('#CE4A57');
  // By workstream
  var ws=[];DATA.rows.forEach(function(t){if(ws.indexOf(t[3])<0)ws.push(t[3]);});
  sh.getRange(4,7).setValue('BY WORKSTREAM').setFontWeight('bold');
  sh.getRange(5,7,1,3).setValues([['Workstream','% done','Open']]).setFontWeight('bold');
  ws.forEach(function(w,i){var r=6+i;var wf="("+T+"!$D$"+lo+":$D$"+hi+'="'+w+'")';
    sh.getRange(r,7).setValue(w);
    sh.getRange(r,8).setFormula('=IFERROR(ROUND(SUMPRODUCT('+subF+'*'+wf+'*'+est+'*'+pct+')/SUMPRODUCT('+subF+'*'+wf+'*'+est+'),0)&"%","0%")');
    sh.getRange(r,9).setFormula('=SUMPRODUCT('+subF+'*'+wf+'*('+st+'<>"Done"))');});
  // By owner load
  sh.getRange(4,11).setValue('OWNER LOAD (open est hrs)').setFontWeight('bold');
  sh.getRange(5,11,1,2).setValues([['Owner','Open Est Hrs']]).setFontWeight('bold');
  DATA.owners.forEach(function(o,i){var r=6+i;sh.getRange(r,11).setValue(o);
    sh.getRange(r,12).setFormula('=SUMPRODUCT('+subF+'*('+own+'="'+o+'")*('+st+'<>"Done")*'+est+')');});
  sh.setColumnWidth(1,230);sh.setColumnWidth(4,150);sh.setColumnWidth(7,150);sh.setColumnWidth(11,110);
}
function refreshDashboard(){buildDashboard_(SpreadsheetApp.getActiveSpreadsheet());SpreadsheetApp.getActiveSpreadsheet().toast('Dashboard refreshed');}

/* ---------------- SCORECARD ---------------- */
function buildScore_(ss){var sh=gc_(ss,S.SCORE);sh.clear();
  sh.getRange('A1').setValue('WEEKLY SPINE SCORECARD  (yellow = weekly inputs)').setFontWeight('bold').setFontSize(13).setFontColor('#363C40');
  var h=['Week Start','Weekly Target','Total Spine NPs','Attainment %','B2B/PL Spine NPs','Qualified-Booking %','Active Spine Accounts','NP / 100 Visits','SEO Pages Updated','Line Tracking OK?','Notes'];
  sh.getRange(3,1,1,h.length).setValues([h]).setFontWeight('bold').setFontColor('#ffffff').setBackground('#54819B');
  var rows=DATA.scoreWeeks.map(function(w){return [d_(w[0]),w[1],'','','','','','','','',''];});
  sh.getRange(4,1,rows.length,h.length).setValues(rows);
  sh.getRange(4,1,rows.length,1).setNumberFormat('yyyy-mm-dd');
  for(var i=0;i<rows.length;i++){var r=4+i;sh.getRange(r,4).setFormula('=IFERROR(ROUND(C'+r+'/B'+r+'*100,0)&"%","")');}
  sh.getRange(4,3,rows.length,1).setBackground('#fff7d6');sh.getRange(4,5,rows.length,7).setBackground('#fff7d6');
  sh.setFrozenRows(3);for(var c=1;c<=h.length;c++)sh.setColumnWidth(c,c===11?240:120);
  sh.getRange('A'+(5+rows.length)).setValue('Floor = 65/wk. Goal = 72/wk by Sept 30. Separate activity (accounts/visits) from output (NPs) from efficiency (NP/100).').setFontColor('#888888');}

/* ---------------- DECISIONS ---------------- */
function buildDec_(ss){var sh=gc_(ss,S.DEC);sh.clear();
  sh.getRange('A1').setValue('OPEN DECISIONS & BLOCKERS').setFontWeight('bold').setFontSize(13).setFontColor('#CE4A57');
  var h=['ID','Item','Owner(s)','Status','Target Date'];
  sh.getRange(3,1,1,h.length).setValues([h]).setFontWeight('bold').setFontColor('#ffffff').setBackground('#CE4A57');
  var rows=DATA.decisions.map(function(x){var r=x.slice();r[4]=d_(r[4]);return r;});
  sh.getRange(4,1,rows.length,h.length).setValues(rows);
  sh.getRange(4,5,rows.length,1).setNumberFormat('yyyy-mm-dd');
  dvR_(sh,4,4,rows.length,['Open','In Progress','Monitoring','Resolved']);
  sh.setColumnWidth(1,55);sh.setColumnWidth(2,430);sh.setColumnWidth(3,230);sh.setColumnWidth(4,120);sh.setColumnWidth(5,110);sh.setFrozenRows(3);}

/* ---------------- BY OWNER ---------------- */
function buildOwner_(ss){var sh=gc_(ss,S.OWNER);sh.clear();var T="'"+S.TASKS+"'";
  sh.getRange('A1').setValue('TASKS BY OWNER - pick an owner in B2').setFontWeight('bold').setFontSize(12).setFontColor('#363C40');
  sh.getRange('A2').setValue('Owner:').setFontWeight('bold');sh.getRange('B2').setValue(DATA.owners[0]);
  dvR_(sh,2,2,1,DATA.owners);
  sh.getRange('A3').setValue('ID / Level / Task / Priority / Due / Status / %Done / Health').setFontColor('#888888');
  sh.getRange('A4').setFormula('=QUERY('+T+'!A2:T, "select A,B,E,J,L,O,P,R where G = \'"&B2&"\' order by O, L", 0)');
  sh.setColumnWidth(1,78);sh.setColumnWidth(3,320);}

/* ---------------- OWNER TABS ---------------- */
function generateOwnerTabs(){var ss=SpreadsheetApp.getActiveSpreadsheet();var T="'"+S.TASKS+"'";
  DATA.owners.forEach(function(o){var nm='@ '+o;var sh=ss.getSheetByName(nm)||ss.insertSheet(nm);sh.clear();
    sh.getRange('A1').setValue('TASKS - '+o).setFontWeight('bold').setFontColor('#363C40');
    sh.getRange('A2').setValue('ID / WS / Task / Priority / Due / Status / %Done / Health / KPI').setFontColor('#888888');
    sh.getRange('A3').setFormula('=QUERY('+T+'!A2:T, "select A,D,E,J,L,O,P,R,N where G = \''+o.replace(/'/g,'')+'\' order by O, L", 0)');
    [78,130,320,60,90,105,60,80,240].forEach(function(x,i){sh.setColumnWidth(i+1,x);});sh.setFrozenRows(3);});
  SpreadsheetApp.getActiveSpreadsheet().toast('Owner tabs generated (prefixed "@").');}

/* ---------------- README ---------------- */
function buildReadme_(ss){var sh=gc_(ss,S.README);sh.clear();var L=[
 ['SYNERGY HEALTH PARTNERS - SPINE GROWTH OPERATING SYSTEM'],[''],
 ['GOAL: qualified spine patients - clear the 65/week floor by Aug 30, operate at 72/week by Sept 30.'],
 ['STRATEGY: qualified conversion + routing, not raw volume. Ortho over-delivers (130-140/wk) to carry the shortfall.'],[''],
 ['HOW THE MACHINE RUNS (weekly rhythm)'],
 ['  MON - Dashboard review: clear Blocked + Overdue first; confirm this week\'s owners/tasks.'],
 ['  WED - Mid-week check: unblock, re-route, adjust; promote 1-2 Ideas Bank Quick Wins into Master Tasks.'],
 ['  FRI - Fill the Weekly Spine Scorecard; run the OODA read (activity vs output vs efficiency).'],
 ['  Every task has an Owner (does it) and an Authorizer (approves it). Nothing ships without its authorizer.'],[''],
 ['TABS'],
 ['  Dashboard - process tracker: % done (effort-weighted), health (On Track/At Risk/Behind), owner load. Refresh via SHP PM menu.'],
 ['  Master Tasks - hierarchy: Task rows (shaded) auto-roll-up from their Subtasks. Edit Subtask Status, % Done, Actual Hours.'],
 ['  Ideas Bank - evidence-based ideas scored by Impact/Effort/Cost with an auto Quadrant. Do Quick Wins first; promote winners to tasks.'],
 ['  Weekly Spine Scorecard - enter weekly actuals in the yellow cells; attainment auto-calculates.'],
 ['  Decisions & Blockers - open leadership decisions + the Line-tracking blocker.'],
 ['  By Owner - filter tasks by owner. "Generate owner tabs" makes one tab each.'],[''],
 ['HOW TO UPDATE A TASK'],
 ['  1) On Master Tasks, edit the Subtask row: set Status, type % Done (0-100) and Actual Hours.'],
 ['  2) The parent Task row rolls up automatically (Est, % Done, Actual, Health).'],
 ['  3) Health flags itself: Behind (past due), At Risk (over-budget or due<=3d & <50%), On Track, Done.'],
 ['  4) SHP PM menu > Refresh dashboard to update rollups.'],[''],
 ['WORKSTREAMS: Spine Growth | Call Center | Physician Liaison | B2C/Organic | Attribution/Systems | Governance/Brand'],
 ['OWNERS: Joe, Kristen, Cody, Jasmine, Kelly, Randall, Paul, Santosh, Katie, Greg, Cardinal, Line, Clinical, Gautam'],
 ['AUTHORIZERS: Gautam (strategy/spend), Katie/Clinical (clinical routing), Joe (marketing exec), Kristen (PL)'],[''],
 ['Detail playbooks: repo /playbooks (master-game-plan, spine-90day-plan, call-center-strategy, b2b-physician-liaison-strategy, ideas-bank).']];
 sh.getRange(1,1,L.length,1).setValues(L);sh.getRange('A1').setFontSize(15).setFontWeight('bold').setFontColor('#49A698');
 ['A6','A11','A19','A25'].forEach(function(a){sh.getRange(a).setFontWeight('bold').setFontColor('#363C40');});
 sh.setColumnWidth(1,980);}

function order_(ss,names){names.forEach(function(n,i){var sh=ss.getSheetByName(n);if(sh){ss.setActiveSheet(sh);ss.moveActiveSheet(i+1);}});}
