import json,sys,glob,os
files=[f for a in sys.argv[1:] for f in glob.glob(os.path.expanduser(a))]
seen={};rows=0
for f in files:
    for l in open(f):
        try: d=json.loads(l)
        except: continue
        m=d.get('message') or {}
        u=m.get('usage')
        if not isinstance(u,dict): continue
        rows+=1
        seen[m.get('id') or d.get('requestId') or rows]=u
K=['input_tokens','cache_creation_input_tokens','cache_read_input_tokens','output_tokens']
t={k:sum(u.get(k,0) or 0 for u in seen.values()) for k in K}
T=sum(t.values())
print(f"files={len(files)} usage_rows={rows} calls={len(seen)} total={T}")
for k in K: print(f"{k}={t[k]} {100*t[k]/T:.1f}%")
