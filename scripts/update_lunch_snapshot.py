"""Update only the lunch-price snapshot from a verified Sheets API export on stdin."""
import datetime
import json
import pathlib
import sys
from zoneinfo import ZoneInfo

root = pathlib.Path(__file__).resolve().parent.parent / 'dist'
rows = json.load(sys.stdin)
expected = ['Ármegfigyelés-ID', 'Helyazonosító', 'Hely / forráscsoport', 'Település', 'Ajánlat típusa', 'Fogások száma', 'Csatorna', 'Kiírt bruttó ár (Ft)', 'Szervizdíj aránya', 'Szervizdíj kezelése', 'Ár szervizdíjjal (Ft)', 'Dobozdíj (Ft/db)', 'Pénznem', 'Ajánlat kezdete', 'Ajánlat vége', 'Megfigyelés dátuma', 'Forrás URL', 'Érvényesség státusza', 'Telephely bizonyossága', 'Megjegyzés / hiány']
if not rows or rows[0] != expected:
    raise ValueError('Unexpected lunch-price column headers')
records = []
for row in rows[1:]:
    row = (row + [None] * 20)[:20]
    if not row[0]:
        continue
    for i in (13, 14, 15):
        if isinstance(row[i], (int, float)):
            row[i] = (datetime.date(1899, 12, 30) + datetime.timedelta(days=row[i])).isoformat()
    records.append(row)
ids = [r[0] for r in records]
if len(ids) != len(set(ids)) or len(records) < 32:
    raise ValueError('Duplicate identifiers or unexpectedly incomplete snapshot')
meta = json.loads((root / 'snapshot-meta.json').read_text())
meta['lunch_imported_at'] = datetime.datetime.now(ZoneInfo('Europe/Budapest')).isoformat(timespec='seconds')
meta['lunch_observations'] = len(records)
for name, data in [('data2.json', [expected] + records), ('snapshot-meta.json', meta)]:
    (root / name).write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
print(f'Imported {len(records)} lunch observations; other worksheet snapshots unchanged.')
