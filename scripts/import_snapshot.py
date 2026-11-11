#!/usr/bin/env python3
"""Validate an XLSX export and write a snapshot into a new, empty staging directory."""
import argparse,collections,datetime,json,os,tempfile
from pathlib import Path
from zoneinfo import ZoneInfo
import openpyxl
p=argparse.ArgumentParser();p.add_argument('xlsx');p.add_argument('--output',default='dist');args=p.parse_args()
w=openpyxl.load_workbook(args.xlsx,data_only=True,read_only=True)
required=['Rekordazonosító','Helyazonosító','Étterem','Település','Étlapkategória','Fogás neve a forrásban','Kiírt bruttó ár (Ft)','Kanonikus fogás-ID','Stabil változat-ID','Tételtípus','Forrás URL','Ellenőrzés dátuma']
def norm(v):
 if isinstance(v,(datetime.datetime,datetime.date)):return v.isoformat()[:10]
 if isinstance(v,str) and v.startswith(('#REF!','#VALUE!','#DIV/0!','#N/A')):raise ValueError('Táblázathiba: '+v)
 return v
def read(name):
 if name not in w:raise ValueError('Hiányzó munkalap: '+name)
 return [[norm(v) for v in row] for row in w[name].iter_rows(values_only=True) if any(v is not None for v in row)]
# The dashboard reads columns by position: reject any reordered or changed header.
expected_header=["Rekordazonosító","Helyazonosító","Étterem","Település","Étlapkategória","Fogás neve a forrásban","Összetevők / rövid kivonat","Kiírt bruttó ár (Ft)","Pénznem","Szervizdíj aránya","Szervizdíj kezelése","Szervizdíjjal számítva (Ft)","Árcsatorna","Érvényesség kezdete","Érvényesség vége","Ellenőrzés dátuma","Forrás URL","Allergénkód a forrásban","Adag / méret számszerűen","Áregység","Kapcsolt pizzaár-rekord","Korlát / forrásállapot","Fogáscsoport-ID","Árváltozat","Változat értelmezése","Kanonikus fogás-ID","Stabil változat-ID","Egységes fogáscsalád","Tételtípus","Fő összetevő – kivonat","Köret – kivonat","Szósz – kivonat","Köret az árban","Mennyiség","Mértékegység","Mennyiség mire vonatkozik","Személyek száma","Értékesítési csatorna","Forrásformátum","Forrás-ID","Ár adatminősége","Érvényesség státusza","Összehasonlítás státusza","Kapcsolt alapváltozat-ID","Kínálati összesítés szerepe","Kapcsolt elsődleges rekord-ID","Kódolási státusz"]
flow=read('Dashboard adatfolyam'); head=flow[0]
if head!=expected_header:raise ValueError('Az adatfolyam oszlopainak neve vagy sorrendje eltér; import megszakítva')
indices={k:head.index(k) for k in required}; records=flow[1:]
if not records:raise ValueError('Üres adatfolyam; import megszakítva')
ids=[]
for row in records:
 if len(row)<47:raise ValueError('Csonka rekord; import megszakítva')
 ident=row[indices['Rekordazonosító']]
 if not ident or not row[indices['Étterem']] or not row[indices['Fogás neve a forrásban']]:raise ValueError('Hiányzó rekordazonosító, étterem vagy fogás')
 value=row[indices['Kiírt bruttó ár (Ft)']]
 if value is not None and (not isinstance(value,(int,float)) or value<0):raise ValueError('Érvénytelen ár: '+str(ident))
 ids.append(ident)
if len(ids)!=len(set(ids)):raise ValueError('Duplikált rekordazonosító; import megszakítva')
central=read('Étlap tételek');h=central[0]; c=[r for r in central[1:] if r[h.index('Rekordazonosító')] and r[h.index('Étterem')] and r[h.index('Fogás neve a forrásban')]]
central_ids=[r[h.index('Rekordazonosító')] for r in c]
if set(central_ids)!=set(ids) or len(central_ids)!=len(ids):raise ValueError('Az adatfolyam és a központi adatblokk eltér, esetleg csonkolt')
# Preserve original values and sheet separation, including notes; normalize dates only.
all_sheets={n:read(n) for n in w.sheetnames}
meta={'imported_at':datetime.datetime.now(ZoneInfo('Europe/Budapest')).isoformat(timespec='seconds'),'source':'Google Sheets XLSX export','spreadsheet_id':'1eigqlKCEuAGTrBA-96k44CB51-EedJh_FJafi2lb_ww','worksheet_count':len(w.sheetnames),'price_observations':len(records),'sync':'manual_snapshot','column_mapping':indices}
out=Path(args.output)
# Never overwrite a previously published set: multiple file renames are not atomic.
if out.exists() and any(out.iterdir()):raise ValueError('A célkönyvtár nem üres; adj meg új staging könyvtárat a --output kapcsolóval. Az éles fájlokat nem módosítottuk.')
out.mkdir(parents=True,exist_ok=True)
payloads={'research.json':all_sheets,'data0.json':all_sheets['Éttermek'],'data1.json':flow,'data2.json':all_sheets['Napi menü árak'],'data3.json':all_sheets['Pizzériák'],'snapshot-meta.json':meta}
# Validate every output in memory before replacing files.
encoded={name:json.dumps(data,ensure_ascii=False,separators=(',',':'),allow_nan=False) for name,data in payloads.items()}
for name,content in encoded.items():
 fd,tmp=tempfile.mkstemp(prefix='.import-',dir=out)
 with os.fdopen(fd,'w',encoding='utf8') as f:f.write(content)
 os.replace(tmp,out/name)
print(json.dumps(meta,ensure_ascii=False))
