"""Build incidents.tsv: every logged failure with its class and whether inputs held before the run predict it.
Sources (paths relative to the shared project folder; incidents.tsv is the kept result): memory FAILED list (M), PLANS FAILED sections (P), ledger void/flagged/fails rows (L, all),
ledger failure rows (R, random sample seed 7 of 45). Tags are one reader's judgment: counts are inferred until
the blind second tagging (tag2.tsv) agrees."""
import csv, random
C = {'reach':'an input or ref the run needs is absent/stale in its env',
     'cap':'a tool, env var, auth, permission or host the run needs is absent in its env',
     'budget':'cost/time/bound arithmetic from known unit costs decides it',
     'logic':'the design contradicts its own goal or is vacuous; decidable on paper or tiny case',
     'shape':'the command or file shape itself (self-match, lost exit, concurrent edit, format)',
     'claim':'a number/fact stated without its command, counted twice, or from memory',
     'order':'a step ran before its inputs settled or its gate finished',
     'intent':'misread of his words; checkable against WORDS/decisions only in part',
     'outcome':'only the run reveals it (effect size, model behaviour, noise)'}
rows = []
def a(src, what, cls, pred): rows.append((src, what, cls, pred))
for w,c,p in [("Over-scoped Scour","intent","partly"),("thread-id typos","shape","yes"),
 ("thread-reported merges stated as my fact","claim","yes"),("card claimed before posted","claim","yes"),
 ("misread 'Give me the card'","intent","partly"),("Codex row launch-red","cap","yes"),
 ("credential extraction attempt","cap","yes"),("Launch rows touched Scour tree","order","yes"),
 ("CD step 1 machine claim","claim","yes"),("claimed steps terminate before checking","claim","yes"),
 ("research ends open without projection","logic","yes"),("six per-repo handoffs","intent","partly"),
 ("sealed Scour reader","logic","partly"),("misnumbered skill steps","shape","yes"),
 ("Scour folding backwards","intent","partly"),("setup courthouse/apt/pip/private-clone errors","cap","yes"),
 ("24k framed as hard","intent","partly"),("handoffs NOT self-contained","reach","yes"),
 ("attackers never ran a handoff from its zip alone","reach","yes"),
 ("CLAUDE_CODE_ENABLE_FUNCTION_HOOKS left out of setup","cap","yes"),
 ("two threads gave different round-nine paste lines","claim","yes"),
 ("other fixes jumped ahead of the 11 missing zip files","order","partly"),
 ("handoffs never told launched sessions to push and merge","cap","yes"),
 ("Scour started changes before modeling","order","yes"),
 ("handoff zip lacked 11 files a step reads (launch stopped)","reach","yes"),
 ("stale Makoto clone turned launch row red","reach","yes"),
 ("permission check refused START.md / relink edits after his approval","cap","partly")]: a('M',w,c,p)
for w,c,p in [("ATTACK2: gloss literal evaluation exponential (12M steps)","budget","yes"),
 ("ATTACK2: kdiff blocked by regen desync (Wire.culprits, Scc.Ecnt)","reach","yes"),
 ("ATTACK2: p4 worker stalled waiting on its own monitor","shape","yes"),
 ("ATTACK2: tiered audit stopped as wasteful","budget","yes"),
 ("CRITIQUE: pgrep -f wait loops matched themselves","shape","yes"),
 ("CRITIQUE: sole.sh foreground hits 590 s cap","budget","yes"),
 ("CRITIQUE: edit to check.py while sole read it spoiled a run","shape","yes"),
 ("CRITIQUE: rm of check.py.wip refused","cap","yes"),
 ("FIX-MZ: Wire.v 1b54 did not compile against fb69","reach","yes"),
 ("FIX-MZ: push to old branch rejected (unmerged superseded commits)","cap","yes"),
 ("LEDGER: harvest workers estimated counts, not parsed","claim","yes"),
 ("MAKOTO2: run.py cannot take makoto (wants one file returning a number)","shape","yes"),
 ("MAKOTO2: installed copy uncheckable before account sync","cap","yes"),
 ("METHOD: 40 mutants x 6 min on 4 cores stopped, 0 finished","budget","yes"),
 ("METHOD: Codex reader blocked by 401","cap","yes"),
 ("NAIVE: hand-built adversarial Rule did not empty narrowed(s)","outcome","no"),
 ("PROVE: dropped absent-owner clause without trial; it was needed","logic","yes"),
 ("PROVE: static end rule gave 5 runs that never end","logic","yes"),
 ("RULES: removal harness skipped units, 51 false greens","claim","yes"),
 ("TOOLS2: force-reset of merged branch refused (auto mode)","cap","yes"),
 ("TOOLS2: output-level capture cannot reach 90% of bill","budget","yes")]: a('P',w,c,p)
rows_l = list(csv.reader(open('../LEDGER/OUTCOMES.tsv'), delimiter='\t'))[1:]
for r in rows_l:
    v = r[3].strip().lower() if len(r) > 3 else ''
    if v.startswith(('void (live','flagged','fails','impossible')):
        a('L', r[0][:140], 'budget', 'yes')
    elif v.startswith('void (stated'):
        a('L', r[0][:140], 'claim' if any(k in r[0].lower() for k in ('count','number','miscount','correction','test run')) else 'intent', 'yes' if 'count' in r[0].lower() or 'number' in r[0].lower() else 'partly')
    elif v.startswith('mistake'):
        a('L', r[0][:140], 'reach', 'yes')
bad = [r for r in rows_l if len(r) > 3 and r[3].strip().lower().startswith(('hurt', "didn't", 'didnt', 'no-effect', 'harm'))]
random.seed(7); s = random.sample(bad, 45)
T = "logic yes|cap yes|intent partly|logic yes|claim yes|budget yes|logic yes|budget yes|reach yes|budget yes|cap yes|claim yes|budget yes|- -|cap yes|claim yes|outcome partly|reach yes|reach yes|order yes|logic yes|- -|cap yes|order yes|logic partly|budget yes|order yes|logic yes|intent partly|logic yes|budget yes|logic partly|outcome partly|- -|claim yes|outcome no|logic yes|- -|logic yes|- -|budget yes|logic yes|outcome no|logic partly|claim yes".split('|')
for r, t in zip(s, T):
    c, p = t.split()
    if c != '-': a('R', r[0][:140], c, p)
with open('incidents.tsv', 'w') as f:
    f.write('src\twhat\tclass\tpredictable_before_run\n')
    for x in rows: f.write('\t'.join(x) + '\n')
with open('classes.tsv', 'w') as f:
    for k, v in C.items(): f.write(k + '\t' + v + '\n')
