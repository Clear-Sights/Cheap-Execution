"""Share of failures predictable before the run, per set and per tagger (mine: incidents.tsv; blind: tag2.tsv)."""
import csv, os
H = os.path.dirname(os.path.abspath(__file__))
A = list(csv.DictReader(open(os.path.join(H, 'incidents.tsv')), delimiter='\t'))
B = list(csv.DictReader(open(os.path.join(H, 'tag2.tsv')), delimiter='\t'))
assert len(A) == len(B)
print('agree predictable %d/%d' % (sum(a['predictable_before_run'] == b['predictable'] for a, b in zip(A, B)), len(A)))
for name, src in [('process', 'MP'), ('experiment', 'LR')]:
    I = [i for i, a in enumerate(A) if a['src'] in src]
    for lab, get in [('mine', lambda i: A[i]['predictable_before_run']), ('blind', lambda i: B[i]['predictable'])]:
        y = sum(get(i) == 'yes' for i in I); p = sum(get(i) == 'partly' for i in I)
        print(name, len(I), lab, 'yes %.0f%%' % (100 * y / len(I)), 'yes+partly %.0f%%' % (100 * (y + p) / len(I)))
