#!/usr/bin/env python3
"""Compare a staged lunch snapshot to the currently published lunch data."""
import argparse, json, math
from pathlib import Path

def load(path):
    rows=json.loads(Path(path).read_text(encoding="utf-8"))
    if not rows or rows[0][0] != "Ármegfigyelés-ID":
        raise ValueError(f"Hibás fejléc: {path}")
    result={}
    for row in rows[1:]:
        if not row or not row[0]: continue
        if row[0] in result: raise ValueError(f"Ismétlődő azonosító: {row[0]}")
        result[row[0]]=row
    return result

def same(a,b):
    if isinstance(a,(int,float)) and not isinstance(a,bool) and isinstance(b,(int,float)) and not isinstance(b,bool):
        return math.isclose(a,b,rel_tol=0,abs_tol=0.001)
    return a==b

p=argparse.ArgumentParser()
p.add_argument("published")
p.add_argument("staged")
a=p.parse_args()
old,new=load(a.published),load(a.staged)
missing=sorted(old.keys()-new.keys())
added=sorted(new.keys()-old.keys())
changed=[]
for key in sorted(old.keys() & new.keys()):
    left,right=old[key],new[key]
    indexes=[i for i in range(max(len(left),len(right))) if not same(left[i] if i<len(left) else None,right[i] if i<len(right) else None)]
    if indexes: changed.append({"id":key,"columns_1_based":[i+1 for i in indexes]})
print(json.dumps({"published_count":len(old),"staged_count":len(new),"missing":missing,"added":added,"changed":changed},ensure_ascii=False,indent=2))
if missing or changed: raise SystemExit(1)
