---
name: "adversarial-review"
description: "Use when choosing evaluation labels or exam cases, grading delivered model input or a fix on held-out cases, choosing a residual model reader, mapping audit seams or sealed plants, validating a check before relying on it, repeating or stopping an audit round, replaying gate or merge claims at the delivered revision, or adding a requirement, rule or deletion definition."
---

# Adversarial Review

## Terms

<!-- term: {"term_id":"plant","faults":1,"scripted":true} -->
- **Plant**: one scripted single-fault target copy; keys hidden from readers and check builders.
<!-- term: {"term_id":"cell","model_tokens":0} -->
- **Cell**: a deterministic check requiring no model tokens.
<!-- term: {"term_id":"seam","link":"producer_consumer","includes":["checker_internal","write"]} -->
- **Seam**: a producer-consumer link, including checker internals and writes.
<!-- term: {"term_id":"slot","product":["seam","fault_class"]} -->
- **Slot**: one seam and recorded fault-class pair.
<!-- term: {"term_id":"witness","target":"unchanged","executable":true} -->
- **Witness**: a command showing a finding on the unchanged target.
<!-- term: {"term_id":"sealed_set","independent":true,"reserved":"before_fix","grades":1} -->
- **Sealed set**: independently labelled cases reserved before the fix and graded once.

## Rules

<!-- rule_id: A4 -->
**1. Use one witnessed residual reader.**
<!-- contract: {"clause_id":"A4.Needs","role":"Needs","classes":["audit_reader"],"terms":["cell","witness"]} -->
Needs: deterministic results naming unchecked claims
<!-- contract: {"clause_id":"A4.Default","role":"Default","forbidden":["cheap_reader_team","unwitnessed_finding"]} -->
Default: Send everything to several cheaper readers.
<!-- contract: {"clause_id":"A4.Do1","role":"Do","actions":["one_residual_reader"]} -->
Do: Give only unchecked claims to one strongest available reader.
<!-- contract: {"clause_id":"A4.Do2","role":"Do","actions":["different_author_model"]} -->
Do: Use a different model from the author.
<!-- contract: {"clause_id":"A4.Do3","role":"Do","actions":["price_last_run"]} -->
Do: Price the reader from its last run.
<!-- contract: {"clause_id":"A4.Do4","role":"Do","actions":["witness"]} -->
Do: Count a finding only with a runnable witness on the unchanged target.
<!-- contract: {"clause_id":"A4.Do5","role":"Do","actions":["record_unresolved"]} -->
Do: Record unresolved claims if independence or budget is unavailable; external review needs authority and the execution budget.
<!-- contract: {"clause_id":"A4.Evidence","role":"Evidence","refs":["matrix:R1"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: The R1 matrix labels eight non-equivalent rows, flags six by cells and eight by the cell-reader union, with T1 caught for the wrong reason; reader costs sum to 371,958 tokens, and Codex efficacy is unmeasured.

<!-- rule_id: A6 -->
**2. Keep labels independent.**
<!-- contract: {"clause_id":"A6.Needs","role":"Needs","classes":["labels"]} -->
Needs: evaluation labels or exam cases
<!-- contract: {"clause_id":"A6.Default","role":"Default","forbidden":["self_labels","baseline_pass_as_gain"]} -->
Default: Let the tested model or implementation choose its own answers.
<!-- contract: {"clause_id":"A6.Do1","role":"Do","actions":["independent_labels"]} -->
Do: Choose expected answers independently of the implementation under test.
<!-- contract: {"clause_id":"A6.Do2","role":"Do","actions":["unchanged_baseline"]} -->
Do: Include the unchanged baseline.
<!-- contract: {"clause_id":"A6.Do3","role":"Do","actions":["discriminating_exam"]} -->
Do: Do not claim improvement from an exam every version passes.
<!-- contract: {"clause_id":"A6.Evidence","role":"Evidence","refs":["L1691"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L1691 records an exam passed 45 of 45 by baseline and skill versions; source record re-checked, trials not rerun.

<!-- rule_id: A8 -->
**3. Grade the delivered information.**
<!-- contract: {"clause_id":"A8.Needs","role":"Needs","classes":["delivered_input"]} -->
Needs: known information required by model answers
<!-- contract: {"clause_id":"A8.Default","role":"Default","forbidden":["single_noisy_answer"]} -->
Default: Score a single noisy answer as deterministic evidence.
<!-- contract: {"clause_id":"A8.Do1","role":"Do","actions":["grade_delivery"]} -->
Do: Grade whether delivered input carries each independently required answer fact.
<!-- contract: {"clause_id":"A8.Do2","role":"Do","actions":["separate_noise"]} -->
Do: Separate stochastic answer flips from input changes.
<!-- contract: {"clause_id":"A8.Evidence","role":"Evidence","refs":["L1735"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L1735 records five flips on 32 byte-identical contexts; source record re-checked, trials not rerun.

<!-- rule_id: A5 -->
**4. Limit repeat rounds to the changed surface.**
<!-- contract: {"clause_id":"A5.Needs","role":"Needs","classes":["audit_repeat"]} -->
Needs: a reviewed revision and regression checks for prior findings
<!-- contract: {"clause_id":"A5.Default","role":"Default","forbidden":["whole_tree_repeat"]} -->
Default: Reread the whole tree each round.
<!-- contract: {"clause_id":"A5.Do1","role":"Do","actions":["diff_from_reviewed"]} -->
Do: After round one, review only the diff from the last reviewed revision.
<!-- contract: {"clause_id":"A5.Do2","role":"Do","actions":["prior_regressions"]} -->
Do: Run regressions for earlier findings.
<!-- contract: {"clause_id":"A5.Do3","role":"Do","actions":["dependency_boundary"]} -->
Do: Expand the diff boundary for a changed dependency.
<!-- contract: {"clause_id":"A5.Evidence","role":"Evidence","refs":["L1660"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L1660 records about 24,000 versus 231,180 tokens on different targets; source re-checked, no same-task saving established.

<!-- rule_id: A1 -->
**5. Derive audit slots from the wiring.**
<!-- contract: {"clause_id":"A1.Needs","role":"Needs","classes":["audit_seams"],"terms":["seam","slot"]} -->
Needs: producer-consumer wiring and recorded fault families
<!-- contract: {"clause_id":"A1.Default","role":"Default","forbidden":["unwired_coverage"]} -->
Default: Search the whole target without a coverage map.
<!-- contract: {"clause_id":"A1.Do1","role":"Do","actions":["all_seams"]} -->
Do: Enumerate all producer-consumer seams, including checker internals and tree writes.
<!-- contract: {"clause_id":"A1.Do2","role":"Do","actions":["seam_fault_slots"]} -->
Do: Make one slot per seam and recorded fault class.
<!-- contract: {"clause_id":"A1.Do3","role":"Do","actions":["missing_wire_finding"]} -->
Do: Record missing wiring as a finding to fill before assigning slots; unwired stages have no coverage claim.
<!-- contract: {"clause_id":"A1.Evidence","role":"Evidence","refs":["matrix:seams"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: The seam table re-counts to 11 rows and 45 holes; the method identifies missing checker-internal and tree-write wiring.

<!-- rule_id: A3 -->
**6. Require cells to fail and pass in the same run.**
<!-- contract: {"clause_id":"A3.Needs","role":"Needs","classes":["check_validity"],"terms":["plant","cell"]} -->
Needs: plants and an unchanged target
<!-- contract: {"clause_id":"A3.Default","role":"Default","forbidden":["red_base_as_pass","never_failed_cell"]} -->
Default: Trust a green check never seen detecting its fault.
<!-- contract: {"clause_id":"A3.Do1","role":"Do","actions":["spec_cell"]} -->
Do: Run the specification checker where that stage exists.
<!-- contract: {"clause_id":"A3.Do2","role":"Do","actions":["proof_assumptions"]} -->
Do: Compile proofs and list every root assumption where proofs exist.
<!-- contract: {"clause_id":"A3.Do3","role":"Do","actions":["root_statement_pin"]} -->
Do: Pin every proof root statement, separately from compilation.
<!-- contract: {"clause_id":"A3.Do4","role":"Do","actions":["corpus_reference"]} -->
Do: Compare extracted code with the reference on the whole recorded corpus where extraction exists.
<!-- contract: {"clause_id":"A3.Do5","role":"Do","actions":["two_sided_same_run"]} -->
Do: Count a cell only when its own plant is red and the unchanged target green in the same run.
<!-- contract: {"clause_id":"A3.Do6","role":"Do","actions":["broken_base_finding"]} -->
Do: Record an unexecutable or broken base as a finding, never a pass.
<!-- contract: {"clause_id":"A3.Evidence","role":"Evidence","refs":["matrix:S27"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: S27 records eight plant rows marked caught at zero model tokens with a green base, one weakly by output diff; these are re-counted historical labels, not new executions.

<!-- rule_id: A10 -->
**7. Replay meaning and verdict claims at the delivered revision.**
<!-- contract: {"clause_id":"A10.Needs","role":"Needs","classes":["claim_replay"]} -->
Needs: a gate, merge or verdict to rely on
<!-- contract: {"clause_id":"A10.Default","role":"Default","forbidden":["prose_match_verdict","report_only_accept","wrong_revision"]} -->
Default: Accept the verdict or match words that resemble the requirement.
<!-- contract: {"clause_id":"A10.Do1","role":"Do","actions":["semantic_classes"]} -->
Do: Key checks on situation meaning, stable rule ids and structured fields.
<!-- contract: {"clause_id":"A10.Do2","role":"Do","actions":["legitimate_negative"]} -->
Do: Test legitimate lookalikes as negatives.
<!-- contract: {"clause_id":"A10.Do3","role":"Do","actions":["claim_receipts"]} -->
Do: Require each verdict claim to name subject, delivered revision, input hashes, check argv, expected result and actual exit.
<!-- contract: {"clause_id":"A10.Do4","role":"Do","actions":["delivered_revision"]} -->
Do: Replay on the revision actually delivered to the consumer.
<!-- contract: {"clause_id":"A10.Do5","role":"Do","actions":["fresh_copy"]} -->
Do: Run deciding claims from a fresh isolated copy.
<!-- contract: {"clause_id":"A10.Do6","role":"Do","actions":["replay_check_claims"]} -->
Do: Re-run the deciding checks before accepting their claims.
<!-- contract: {"clause_id":"A10.Evidence","role":"Evidence","refs":["late:15","late:16"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: Late DetIO reading caught three text-versus-meaning checks and withheld two faulty commits: five defects the verdict missed; the same summary reports checks crashing on main.

<!-- rule_id: A11 -->
**8. Put each definition and necessity claim into the mesh now.**
<!-- contract: {"clause_id":"A11.Needs","role":"Needs","classes":["definition"]} -->
Needs: a new requirement, rule or deletion claim
<!-- contract: {"clause_id":"A11.Default","role":"Default","forbidden":["next_version","duplicate_owner","decorative_clause"]} -->
Default: Defer the definition or keep a line because it sounds useful.
<!-- contract: {"clause_id":"A11.Do1","role":"Do","actions":["mesh_now"]} -->
Do: Add every definition to the mesh now as a binary semantic hole.
<!-- contract: {"clause_id":"A11.Do2","role":"Do","actions":["unique_owner"]} -->
Do: Assign each hole exactly one owner.
<!-- contract: {"clause_id":"A11.Do3","role":"Do","actions":["presence_absence"]} -->
Do: Specify what must be present and absent.
<!-- contract: {"clause_id":"A11.Do4","role":"Do","actions":["timeless_mesh"]} -->
Do: Keep execution order out of the mesh.
<!-- contract: {"clause_id":"A11.Do5","role":"Do","actions":["one_repair"]} -->
Do: Assign one dependency-ordered repair to each unmet hole.
<!-- contract: {"clause_id":"A11.Do6","role":"Do","actions":["execute_now"]} -->
Do: Execute all repairs now, never defer a definition to a next version.
<!-- contract: {"clause_id":"A11.Do7","role":"Do","actions":["removal_witness"]} -->
Do: Keep a clause exactly when a requirement in the requester's own words needs it; if removing a needed clause turns nothing red, a check is missing, not the clause.
<!-- contract: {"clause_id":"A11.Do8","role":"Do","actions":["live_references"]} -->
Do: Recheck live references before deleting replaced material.
<!-- contract: {"clause_id":"A11.Evidence","role":"Evidence","refs":["L807","L1076"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L807 records 5,994 of 6,422 lines deleted while the done command still claimed met; L1076 records one live citation retained after a cleanup re-check.

<!-- rule_id: A9 -->
**9. Hold closure until a different method adds nothing.**
<!-- contract: {"clause_id":"A9.Needs","role":"Needs","classes":["audit_stop"],"terms":["plant","cell"]} -->
Needs: plants, cells and reader findings
<!-- contract: {"clause_id":"A9.Default","role":"Default","forbidden":["duplicate_rate_stop","repeat_same_reader"]} -->
Default: Stop from duplicate rates, Chao1, tiers or a judge.
<!-- contract: {"clause_id":"A9.Do1","role":"Do","actions":["all_plants_red"]} -->
Do: Require every non-equivalent plant red.
<!-- contract: {"clause_id":"A9.Do2","role":"Do","actions":["green_base"]} -->
Do: Require a green unchanged base.
<!-- contract: {"clause_id":"A9.Do3","role":"Do","actions":["different_method_zero"]} -->
Do: Require a different method to add no findings: mechanical mutants after hand plants, or cells after reading.
<!-- contract: {"clause_id":"A9.Do4","role":"Do","actions":["hold_no_new_method"]} -->
Do: Hold the audit when no new method exists.
<!-- contract: {"clause_id":"A9.Evidence","role":"Evidence","refs":["L216"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L216 records self-audit rounds held pending METHOD3; no measured general stopping benefit is established.

<!-- rule_id: A2 -->
**10. Seal one-fault plants and predicted outcomes.**
<!-- contract: {"clause_id":"A2.Needs","role":"Needs","classes":["audit_plants"],"terms":["slot","plant"]} -->
Needs: audit slots
<!-- contract: {"clause_id":"A2.Default","role":"Default","forbidden":["exposed_keys","equivalence_by_assertion"]} -->
Default: Review without known faults or expose their keys.
<!-- contract: {"clause_id":"A2.Do1","role":"Do","actions":["one_fault_per_slot"]} -->
Do: Reserve at least one single-fault copy per slot.
<!-- contract: {"clause_id":"A2.Do2","role":"Do","actions":["hidden_keys"]} -->
Do: Hide plant keys from readers and check builders.
<!-- contract: {"clause_id":"A2.Do3","role":"Do","actions":["predict_both_sides"]} -->
Do: Predict each plant's red and green check sets.
<!-- contract: {"clause_id":"A2.Do4","role":"Do","actions":["fault_families"]} -->
Do: Include accept-all, early-stop, admitted or axiomatic proof, weakened statement, order, tie-break, swallowed-error and trivial-answer faults.
<!-- contract: {"clause_id":"A2.Do5","role":"Do","actions":["mechanical_mutants"]} -->
Do: Add mechanical mutants.
<!-- contract: {"clause_id":"A2.Do6","role":"Do","actions":["equivalence_proof"]} -->
Do: Exclude an indistinguishable plant only with an equivalence proof.
<!-- contract: {"clause_id":"A2.Evidence","role":"Evidence","refs":["L81","method:reader"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L81 records 59 of 60 mechanical mutants caught, not universal coverage; METHOD3 records cheaper readers missing all first eight plants.

<!-- rule_id: A7 -->
**11. Grade a fix once on unused independent cases.**
<!-- contract: {"clause_id":"A7.Needs","role":"Needs","classes":["heldout"],"terms":["sealed_set"]} -->
Needs: an independently labelled unused set sealed before the fix
<!-- contract: {"clause_id":"A7.Default","role":"Default","forbidden":["reuse_spent_set","claim_bulk_done"]} -->
Default: Keep tuning on the same exposed misses.
<!-- contract: {"clause_id":"A7.Do1","role":"Do","actions":["pre_fix_seal"]} -->
Do: Reserve the grading set before writing the fix.
<!-- contract: {"clause_id":"A7.Do2","role":"Do","actions":["independent_heldout"]} -->
Do: Use independently labelled held-out cases.
<!-- contract: {"clause_id":"A7.Do3","role":"Do","actions":["cross_corpus"]} -->
Do: Reserve sets in bulk, including a different corpus.
<!-- contract: {"clause_id":"A7.Do4","role":"Do","actions":["grade_once"]} -->
Do: Grade a fix once on an unused set.
<!-- contract: {"clause_id":"A7.Do5","role":"Do","actions":["spent_calibration"]} -->
Do: A spent set becomes calibration data.
<!-- contract: {"clause_id":"A7.Do6","role":"Do","actions":["unused_next"]} -->
Do: The next fix requires an unused set.
<!-- contract: {"clause_id":"A7.Do7","role":"Do","actions":["limits"]} -->
Do: Report uncompleted bulk sealing and single reported cases as evidence limits.
<!-- contract: {"clause_id":"A7.Evidence","role":"Evidence","refs":["L1738","L1763"],"status":"source_record_rechecked; efficacy_not_remeasured"} -->
Evidence: L1738 records less than main on 23 of 139 sealed cases; L1763 reports one different-corpus over-cut and bulk sealing NOT YET DONE, not replicated here.