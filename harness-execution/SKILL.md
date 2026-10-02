---
name: "harness-execution"
description: "Use instead of general vendor-neutral routing for this project's Codex 95% share and stop rule, Astra allocation, modelUsage and Codex log billing, codex-wait.sh background chains, DetIO store delivery, Tiller/router real acceptance, Makoto hook configuration, or Countdown skill repairs, alongside cheap-execution for cost and verdict reading and adversarial-review for independent checks."
---

# Harness Execution

## Terms

The clause records define the project adapter contract; general decisions retain their own owners.

## Rules

<!-- rule_id: H17 -->
**1. Bind Astra plans to Codex workers.**
<!-- contract: {"clause_id":"H17.Needs","role":"Needs","classes":["harness_launch"]} -->
Needs: this harness apportioning a Codex task list
<!-- contract: {"clause_id":"H17.Default","role":"Default","forbidden":["unbound_codex_plan"]} -->
Default: A vendor-neutral allocation never becomes a launchable Codex plan.
<!-- contract: {"clause_id":"H17.Do1","role":"Do","actions":["astra_codex_plan"]} -->
Do: Use Astra, the top Codex planner, to write each task model, effort, dependencies, return format and maximum length.
<!-- contract: {"clause_id":"H17.Do2","role":"Do","actions":["codex_checked_leaf"]} -->
Do: Bind checked leaves to the cheapest capable available Codex model at low effort; follow the general check-driven escalation rule.
<!-- contract: {"clause_id":"H17.Evidence","role":"Evidence","refs":["late:25"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: LATE-EVENTS records an 8,435-cache-write worker unable to call the required history tool; record re-checked, new allocation efficacy unmeasured.

<!-- rule_id: H19 -->
**2. Bind authorized Codex successors to the background runner.**
<!-- contract: {"clause_id":"H19.Needs","role":"Needs","classes":["harness_chain"]} -->
Needs: an authorized dependent Codex run in this harness
<!-- contract: {"clause_id":"H19.Default","role":"Default","forbidden":["shell_chain_failed_parent"]} -->
Default: A coordinator reread sits between successful background runs.
<!-- contract: {"clause_id":"H19.Do1","role":"Do","actions":["codex_wait_dependency"]} -->
Do: In one background shell, use codex-wait.sh to settle the predecessor before starting the already-authorized Codex successor.
<!-- contract: {"clause_id":"H19.Do2","role":"Do","actions":["shell_exit_receipts"]} -->
Do: Persist the predecessor exit, successor exit and verdict paths; a wait failure must prevent successor launch.
<!-- contract: {"clause_id":"H19.Evidence","role":"Evidence","refs":["late:11"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: LATE-EVENTS line 11 records run 6 chained after run 5 through codex-wait.sh; source re-checked, general savings unmeasured.

<!-- rule_id: H9 -->
**3. Read the harness usage schema.**
<!-- contract: {"clause_id":"H9.Needs","role":"Needs","classes":["harness_bill"]} -->
Needs: a Claude or Codex result in this harness
<!-- contract: {"clause_id":"H9.Default","role":"Default","forbidden":["schema_last_segment"]} -->
Default: Top-level or last-segment usage stands in for the completed step.
<!-- contract: {"clause_id":"H9.Do1","role":"Do","actions":["harness_usage_fields"]} -->
Do: For Claude JSON, read aggregate modelUsage and inputTokens, outputTokens, cacheReadInputTokens and cacheCreationInputTokens; normalize to the general bill.
<!-- contract: {"clause_id":"H9.Do2","role":"Do","actions":["codex_log_footer"]} -->
Do: For Codex logs, read the settled tokens-used footer; absent or unfinished logs are unknown, never zero.
<!-- contract: {"clause_id":"H9.Evidence","role":"Evidence","refs":["L1746","L1732"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: The re-checked ledger records 279,993 versus aggregate 3,956,759; Codex RUNS.tsv distinguishes logs with no footer.

<!-- rule_id: H2 -->
**4. Verify DetIO delivery from its store.**
<!-- contract: {"clause_id":"H2.Needs","role":"Needs","classes":["detio_store"]} -->
Needs: a DetIO store-backed handoff or probe result
<!-- contract: {"clause_id":"H2.Default","role":"Default","forbidden":["missing_store_object"]} -->
Default: A kept key with no stored object appears delivered.
<!-- contract: {"clause_id":"H2.Do1","role":"Do","actions":["detio_store_objects"]} -->
Do: Check that every delivered kept key resolves to its stored object in the actual DETIO_STORE_DIR; skip project stores containing keys but no objects.
<!-- contract: {"clause_id":"H2.Do2","role":"Do","actions":["detio_delivery_receipts"]} -->
Do: Attach out.json, err.log, check.log and the store identity to the probe receipt; let the general verdict cross-check decide reliance.
<!-- contract: {"clause_id":"H2.Evidence","role":"Evidence","refs":["detio:brief9","detio:brief10b"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: DetIO BRIEF9 names the two missing-object fixes; BRIEF10B names out.json, err.log, check.log and store/; source records re-checked, fixes not re-executed here.

<!-- rule_id: H3 -->
**5. Bind Tiller acceptance to the real run.**
<!-- contract: {"clause_id":"H3.Needs","role":"Needs","classes":["router_run"]} -->
Needs: a Tiller/router plan or live-run result
<!-- contract: {"clause_id":"H3.Default","role":"Default","forbidden":["fixture_as_live"]} -->
Default: A fixture run is reported as live validation.
<!-- contract: {"clause_id":"H3.Do1","role":"Do","actions":["tiller_launch_owner"]} -->
Do: Tiller outside the Codex sandbox launches the workers; astra.py writes and validates PLAN.json, with each rung recorded in RUN.json.
<!-- contract: {"clause_id":"H3.Do2","role":"Do","actions":["router_real_acceptance"]} -->
Do: Validate the actual real-run directory with check.sh --real and its windowed count; keep dry-run acceptance distinct.
<!-- contract: {"clause_id":"H3.Evidence","role":"Evidence","refs":["router:brief4","router:brief3"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: Router BRIEF4 assigns launch to Tiller and plan validation to astra.py; BRIEF3 requires the windowed real count; source records re-checked, no live run repeated.

<!-- rule_id: H4 -->
**6. Check Makoto configuration before relying on its hooks.**
<!-- contract: {"clause_id":"H4.Needs","role":"Needs","classes":["makoto_hook"]} -->
Needs: this harness relying on Makoto dispatch or verdict hooks
<!-- contract: {"clause_id":"H4.Default","role":"Default","forbidden":["uninstalled_hook_as_guard"]} -->
Default: A named hook is treated as an installed independent guard.
<!-- contract: {"clause_id":"H4.Do1","role":"Do","actions":["makoto_observed_enabled"]} -->
Do: Confirm the plugin exists, hooks are enabled and dispatch configuration applies; otherwise record that guard as unavailable.
<!-- contract: {"clause_id":"H4.Do2","role":"Do","actions":["makoto_dispatch_surface"]} -->
Do: When Makoto dispatch is enabled, provide READ entries pinned by digest, WRITE scope and ACCEPTANCE; its I3 and C4 hooks need their own observed deciding exits.
<!-- contract: {"clause_id":"H4.Evidence","role":"Evidence","refs":["makoto:I1","makoto:I2","makoto:I3","makoto:C4","makoto:E12"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: The re-checked registry rows I1-I3, C4 and E12 name the dispatch shape, observed acceptance exits and enabled-plugin dependency; no installation assumed.

<!-- rule_id: H5 -->
**7. Run this skill repair list as a Countdown task list.**
<!-- contract: {"clause_id":"H5.Needs","role":"Needs","classes":["countdown_repairs"]} -->
Needs: the skill mesh repair list in this project
<!-- contract: {"clause_id":"H5.Default","role":"Default","forbidden":["countdown_only_zero"]} -->
Default: A Countdown zero is claimed without checking the delivered skills.
<!-- contract: {"clause_id":"H5.Do1","role":"Do","actions":["countdown_repair_list"]} -->
Do: Use seed/SEED.tsv as the finite Countdown task list: exactly one repair per unmet hole, transitive dependencies before consumers, remaining count decreases by one. For formal COUNTDOWN-SEED tuning, use its mesh/code-equivalence checker; this task-list count is not a proof of kernel equivalence.
<!-- contract: {"clause_id":"H5.Do2","role":"Do","actions":["countdown_delivered_gate"]} -->
Do: A zero repair count licenses closure only when check/gate.sh on the delivered three-skill package is green and every non-equivalent plant is red.
<!-- contract: {"clause_id":"H5.Evidence","role":"Evidence","refs":["L807","brief2:countdown"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: Ledger L807 records deletion of 5,994 of 6,422 lines while Countdown still claimed met; source record re-checked, this run uses a task-list countdown.

<!-- rule_id: C18 -->
**8. Stop when the Codex share cannot be established.**
<!-- contract: {"clause_id":"C18.Needs","role":"Needs","classes":["budget"]} -->
Needs: a launch or completed step in this harness with token accounting
<!-- contract: {"clause_id":"C18.Default","role":"Default","forbidden":["unknown_as_pass","token_padding"]} -->
Default: A cheap-looking worker conceals coordinator rereads.
<!-- contract: {"clause_id":"C18.Do1","role":"Do","actions":["reserve_read"]} -->
Do: Reserve the result-reading turn before dispatch.
<!-- contract: {"clause_id":"C18.Do2","role":"Do","actions":["share_95"]} -->
Do: Require Codex to carry at least 95% of the whole step bill.
<!-- contract: {"clause_id":"C18.Do3","role":"Do","actions":["stop_low_or_unknown"]} -->
Do: Stop dispatch when that share is below 95% or unknown.
<!-- contract: {"clause_id":"C18.Do4","role":"Do","actions":["replan_codex"]} -->
Do: Move the needed work into Codex before resuming.
<!-- contract: {"clause_id":"C18.Do5","role":"Do","actions":["settle_actual"]} -->
Do: Settle actual totals before claiming the share passes.
<!-- contract: {"clause_id":"C18.Do6","role":"Do","actions":["no_padding"]} -->
Do: Do no extra work merely to pad Codex tokens.
<!-- contract: {"clause_id":"C18.Evidence","role":"Evidence","refs":["late:22"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: The late router summary reports 81,429 Codex versus approximately 4.47M Claude tokens; the recomputed share is 1.7891%, and 95% requires Codex at least 19 times Claude.