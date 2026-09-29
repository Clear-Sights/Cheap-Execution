import csv,collections,sys
f=sys.argv[1] if len(sys.argv)>1 else 'incidents.tsv'
R=list(csv.DictReader(open(f),delimiter='\t'))
for src in ['all','M','P','L','R']:
  S=[r for r in R if src=='all' or r['src']==src]; c=collections.Counter(r['predictable_before_run'] for r in S)
  print(src,'n=%d'%len(S),'yes=%d partly=%d no=%d'%(c['yes'],c['partly'],c['no']),'yes%%=%.0f yes+partly%%=%.0f'%(100*c['yes']/len(S),100*(c['yes']+c['partly'])/len(S)))
print(collections.Counter(r['class'] for r in R).most_common())
