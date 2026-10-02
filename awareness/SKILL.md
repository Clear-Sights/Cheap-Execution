---
name: "awareness"
description: "Use when defining or changing the end result, when adopting an action or receiving a steering message, when choosing a method or observing its result, when work waiting or a result returning, when reading spend or deciding capacity, when a work interval ending or burn lacking progress, when cost exceeding prediction, repeated failure, a miss or unchecked prior art, when the situation changing or context resuming."
---

# Awareness

## Terms

- **WHY**: the requested end result, whose accepted conditions define perfect termination.
- **WHAT**: the work chosen to close a WHY gap.
- **HOW**: the method used to produce WHAT.
- **Headroom**: remaining capacity within a meter’s units and window.

## Rules

<!-- rule_id: W1 -->
**1. Define perfect termination.** Needs: the request. Default: keep acting without reassessment.
State WHY as the requested end result and observable acceptance conditions for perfect termination; break it into pieces, with remaining gaps and evidence of acceptance for each; missing intent or criteria are unknown and must be resolved before dependent choices.
Rate each piece by lever: direct breadth narrow=1 (one piece), medium=2 (recurring family), broad=3 (session-wide); cascade contained keeps breadth, amplifying raises reach, trajectory sets reach=3 when evidence links it to whole-run completion or correctness; impact mild=1 (hygiene), moderate=2 (measured cost or rework improvement), high=3 (correctness or blocking rework removed), decisive=4 (completion enabled or terminal harm avoided); complexity simple=1 (one habit), medium=2 (small check), hard=3 (cooperating mechanisms); the reader computes simplicity, score and value; keep value and complexity separate. Cite support per axis, record recurring occasions as frequency evidence rather than another multiplier, and leave unsupported ratings unknown; failures prove harm, not remedy benefit.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W2 -->
**2. Assess WHAT against WHY.** Needs: WHY and the proposed action. Default: keep acting without reassessment.
State WHAT is being done and which WHY piece its output advances; check every action against that piece and its acceptance conditions. Hyperfocus pursues a sub-goal past its useful contribution; hypofocus drifts or leaves actionable work idle; flag either and name the smallest action closing a real gap.
Treat a new message as steering unless it explicitly replaces WHY; retain unfinished obligations with next action or blocker, and reassess WHAT against an explicitly changed WHY.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W3 -->
**3. Assess HOW against WHAT.** Needs: WHAT and the current method. Default: keep acting without reassessment.
State HOW, its inputs, dependencies, expected output, quality requirements and predicted interval cost with units or unknown; assess the method against whether it reaches WHAT, recording actual output quality and the evidence or uncertainty behind that assessment.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W4 -->
**4. Measure the distance still left.** Needs: WHY pieces and current evidence. Default: keep acting without reassessment.
For each WHY piece compare current accepted state with its acceptance conditions: record the remaining gap, blocker or next action, and direction of travel since the previous observation; do not invent a completion percentage for incomparable pieces.
For relevant work and dependencies identify scope, owner and output; record working, tool, person, idle or done state with next action or blocker; the reader classifies these and checks recorded process identity, output and progress timestamps and wake condition; a live process alone is not progress, and unobservable state is unknown.
A returned result is accepted, missed or unchecked against its conditions; only all accepted WHY pieces with no unresolved required gap establish perfect termination.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W5 -->
**5. Read real burn and limits.** Needs: available session telemetry. Default: keep acting without reassessment.
Run the inline reader without accessing credentials; report token spend, context size and available cost with source, observation time, units, window and coverage; label estimates as estimates and missing readings unknown.
Read five-hour and weekly used or remaining limits and reset times from the provider’s authoritative readout; record fresh authoritative units, window, reset and remaining or limit and used; the reader computes headroom, never inferred from local token totals. In a remote session the readout is claude-code-remote `list_events(session_id, kinds=["rate_limit_event"], limit=100)`: from the newest event's `rate_limit_info.unifiedWindows`, record `five_hour` as limits.five_hour and `seven_day` as limits.weekly, each with units "fraction", limit 1, used = `utilization`, reset = `resetsAt` (Unix seconds), authoritative true, and fresh true only for the newest event; both windows are account-wide. If no readout exists say unknown.
Refresh before capacity decisions and after resets or shared-consumer changes; stale readings are unknown. Compare planned demand with both windows; neither window substitutes for the other.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W6 -->
**6. Compare burn with TRUE results.** Needs: matching interval observations and WHY criteria. Default: keep acting without reassessment.
TRUE results = quality × progress toward perfect termination, trajectory included: quality is satisfaction of the piece’s acceptance conditions, progress is evidenced reduction of its remaining gap, and trajectory is whether successive intervals approach or retreat from WHY; raw output, activity and proxy marks are not progress.
Compare token burn / TRUE results for the same scope and interval, including verification and rework, against the recorded prediction and best evidenced comparable method. Record interval token burn and numeric quality and progress only with defined comparable scales and matching scope; the reader computes TRUE results and ratio; otherwise report the components and direction qualitatively, with unknowns explicit. Positive burn with zero progress is burn without result; zero TRUE results gives no finite ratio.
Call the ratio excellent only when required quality is met, trajectory closes WHY gaps and cost is within prediction without an evidenced better feasible option; absent evidence leaves excellence unknown. Any non-excellent or unknown assessment asks whether HOW or WHAT can improve.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W7 -->
**7. Find the better HOW or WHAT.** Needs: a weak ratio or alternatives signal. Default: keep acting without reassessment.
Pause unchanged repetition and look for alternatives when the ratio is not excellent or unknown, cost exceeds prediction, the same failure repeats, a result misses, or relevant prior art is unchecked; identify whether the weakness is HOW failing WHAT or WHAT failing WHY.
Identify candidate changes to HOW and WHAT from available records, existing implementations and standard methods; report the search scope, reusable option or remaining gap, distinguishing searched absence from unchecked absence. Assess the status of prior-art checking here, without prescribing an implementation-adoption procedure.
Compare continuing, adapting, switching HOW, switching WHAT and stopping against the same WHY: expected quality, gap reduction and trajectory, total token cost including verification and rework, constraints and observed capability. Name the preferred option and evidence, or the missing fact and next inquiry; a WHAT swap must still serve WHY, and this assessment grants no new authority.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

<!-- rule_id: W8 -->
**8. Tell what is what.** Needs: changed findings or consequential unknowns. Default: keep acting without reassessment.
Surface a compact readout of WHY, WHAT, HOW, remaining gaps and trajectory, relevant board changes, burn / TRUE results, limit headroom and the alternative decision; stay silent on unchanged state unless asked. Awareness informs; it does not itself dispatch, enforce gates or set allocation targets.
On resume read the session’s existing work record for these observations and unresolved obligations, then refresh changed facts; session restart and handoff construction are separate execution procedures.
Evidence: inferred from the recorded purpose, measurement and observation contracts; live efficacy is unmeasured.

## Deterministic reader

Run this single block with `python3 -`. Standard Claude transcript discovery uses `CLAUDE_TRANSCRIPT_PATH` or `CLAUDE_SESSION_ID`; absent identity stays unknown. Burn sums input, cache creation, cache read and output once per message ID; context is the last request's input plus both caches, not an exact current context meter. Missing fields invalidate totals; partial lines are skipped. No provider quota or price is inferred.

Record judgments in `AWARENESS_STATE` JSON (or transcript records with type `awareness`, data object): board entries use id/state/pid/start_ticks/output_at/progress_at/wake/next/blocker; lever uses id/breadth/cascade/trajectory/complexity/impact; interval uses burn/quality/progress/prediction/comparable; failures is an ordered list of identical-method failure signatures; miss/prior_art_unchecked/ratio_not_excellent are booleans. Limits use five_hour/weekly objects with fresh/authoritative/units/reset and remaining or limit/used. These are explicit observations, never fabricated telemetry. Freshness, comparability, failure identity, timestamps' meaning and ratings need evidence and judgment; arithmetic and recorded-state classification do not. Process identity uses Linux /proc start ticks; output/progress timestamps are recorded observations, not proof of progress. W1 supplies ratings, W2 alignment, W3 prediction, W4 board, W5 telemetry, W6 comparable scales, W7 triggers; W8 prints three fixed-key JSON lines and adds a short judgment readout when findings change. Unknown observations remain unknown.

```python
import os, json, re, datetime
from pathlib import Path
U = "unknown"
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
base = Path.home()/".claude"/"projects"
p = None
hint = os.environ.get("CLAUDE_TRANSCRIPT_PATH")
sid = os.environ.get("CLAUDE_SESSION_ID")
if hint:
    q = Path(hint).expanduser().resolve()
    if q.is_relative_to(base.resolve()) and q.suffix == ".jsonl": p = q
elif sid and re.fullmatch(r"[A-Za-z0-9-]+", sid):
    matches = list(base.glob("*/"+sid+".jsonl"))
    if len(matches) == 1: p = matches[0]
# Never guess the current session by newest file.
rows, messages, state = [], {}, {}
if p and p.is_file():
    for line in p.open():
        try: rows.append(json.loads(line))
        except ValueError: pass  # incomplete trailing write
for r in rows:
    m = r.get("message", {})
    if r.get("type") == "assistant" and isinstance(m, dict) and m.get("id") and m.get("usage"):
        messages.pop(m["id"], None)
        messages[m["id"]] = (m["usage"], r.get("timestamp", U))
    if r.get("type") == "awareness": state = r.get("data", {})
# Explicit observations may also be supplied as a JSON environment value.
try: state = json.loads(os.environ.get("AWARENESS_STATE", json.dumps(state)))
except ValueError: state = {}
def num(x): return isinstance(x, (int, float)) and not isinstance(x, bool) and x >= 0
keys = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")
valid = bool(messages) and all(all(num(u.get(k)) for k in keys) for u, _ in messages.values())
totals = {k: sum(u[k] for u, _ in messages.values()) if valid else U for k in keys}
last = next(reversed(messages.values())) if messages else None
context = sum(last[0][k] for k in keys[:3]) if last and all(num(last[0].get(k)) for k in keys[:3]) else U
burn = sum(totals.values()) if valid else U
board = []
labels = {"working":"working", "tool":"waiting on a tool/run", "person":"waiting on the person", "idle":"idle with work left", "done":"done"}
for b in state.get("board", []):
    running = U
    if isinstance(b.get("pid"), int) and "start_ticks" in b:
        try:
            stat = (Path("/proc")/str(b["pid"])/"stat").read_text().rsplit(")",1)[1].split()
            running = stat[19] == str(b["start_ticks"]) and stat[0] not in ("Z", "X")
        except FileNotFoundError: running = False
        except OSError: pass
    board.append({"id":b.get("id", U), "state":labels.get(b.get("state"), U), "running":running,
                  **{k:b.get(k,U) for k in ("output_at","progress_at","wake","next","blocker")}})
lever = []
for a in state.get("lever", []):
    b,c,i = (a.get(k) for k in ("breadth","complexity","impact"))
    reach = min(3,b+(a.get("cascade")=="amplifying")) if b in (1,2,3) and a.get("cascade") in ("contained","amplifying") else U
    if a.get("trajectory") is True: reach = 3
    s = 4-c if c in (1,2,3) else U
    lever.append({"id":a.get("id",U),"reach":reach,"simplicity":s,"score":reach*s if num(reach) and num(s) else U,"value":reach*i if num(reach) and i in (1,2,3,4) else U})
interval = state.get("interval", {})
b,q,g,pred = (interval.get(k) for k in ("burn","quality","progress","prediction"))
true = q*g if interval.get("comparable") is True and num(q) and num(g) else U
ratio = b/true if num(b) and num(true) and true>0 else U
flags = {"over_prediction":b>pred if num(b) and num(pred) else U,
         "repeated_failure":U,"burn_without_result":b>0 and g==0 if num(b) and num(g) else U}
f = state.get("failures")
if isinstance(f,list): flags["repeated_failure"] = len(f)>=2 and bool(f[-1]) and f[-1]==f[-2]
for k in ("miss","prior_art_unchecked","ratio_not_excellent"): flags[k] = state.get(k,U)
headroom = {}
for window in ("five_hour","weekly"):
    a = state.get("limits",{}).get(window,{})
    h = U
    if a.get("fresh") is True and a.get("authoritative") is True and a.get("units") and a.get("reset"):
        h = a.get("remaining", U)
        if not num(h): h = a["limit"]-a["used"] if num(a.get("limit")) and num(a.get("used")) else U
    headroom[window] = {"remaining":h,"units":a.get("units",U),"reset":a.get("reset",U)}
def emit(k,v): print(k+"="+json.dumps(v,sort_keys=True,separators=(",",":")))
emit("SOURCE", {"path":str(p) if p else U,"observed_at":now,"usage_at":last[1] if last else U,"coverage":"unique assistant message IDs; last usage per ID; recorded transcript only"})
emit("TOKENS", {**totals,"burn":burn,"context_input":context,"cost":U,"window":"recorded session"})
emit("STATE", {"board":board or U,"lever":lever or U,"true_results":true,"ratio":ratio,"flags":flags,"headroom":headroom})
```