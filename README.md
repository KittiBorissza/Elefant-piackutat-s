# Elefánt Piackép

Statikus, magyar nyelvű éttermi piackutatási dashboard.

## Helyi indítás

A projekt gyökeréből: `python -m http.server 8000 --directory dist`, majd nyisd meg a `http://localhost:8000` címet.

A `dist/` a jelenlegi alkalmazáskódot és adatpillanatképeket tartalmazza. A Google Sheet nem frissül automatikusan. Az adatok és a hozzáférés belső kezelésére figyelni kell. A meglévő privát ChatGPT Site külön kiszolgálón fut; a GitHubra másolás önmagában nem kapcsolja át a hostingot vagy az automatikus telepítést.

## Adatfrissítés

A pillanatkép Google Sheetsből exportált XLSX-szel frissíthető: `python scripts/import_snapshot.py export.xlsx`. Szükséges a Python `openpyxl` csomag. A parancs ellenőrzi az adatfolyam szerkezetét és rekordjait; hibánál nem futtat frissítést. Az import ideje a `dist/snapshot-meta.json` fájlban van. A weboldal nem használ élő Sheets-kapcsolatot.
