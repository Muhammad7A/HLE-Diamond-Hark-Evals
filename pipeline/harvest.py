import json,glob,os,sys
# union all records from batch files into write-once per-id files; never deletes
for p in ['primary','review']:
    n=0
    for f in glob.glob(f'out/{p}/*.jsonl'):
        for l in open(f):
            l=l.strip()
            if not l: continue
            try: r=json.loads(l)
            except: continue
            fn=f'out/items/{p}/{r["id"]}.json'
            if not os.path.exists(fn):
                json.dump(r,open(fn,'w')); n+=1
    print(p,'new',n,'total',len(os.listdir(f'out/items/{p}')))
