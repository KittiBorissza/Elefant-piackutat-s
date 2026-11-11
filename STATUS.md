# Elefánt Piackép – fejlesztési állapot

## 2026-11-11 – adatfrissítés és első UI-kör

- Forrás: Google Sheets XLSX-export; a sikeres import pontos ideje a `dist/snapshot-meta.json` állományban.
- A dashboard adatfolyam és az Étlap tételek összevetésével 585 ármegfigyelés került be, 34 munkalappal. Az adatfolyamot a központi rekordok azonosítóival összevetve ellenőriztük; a példaszámok változhatnak.
- Az import kézi, a táblázat nincs élő kapcsolattal összekötve. Futtatás: `python scripts/import_snapshot.py /path/to/export.xlsx`. A függőség: openpyxl.
- Az import ellenőrzi a 47 oszlopot és a kötelező fejléceket, az egyedi rekordazonosítókat, az árat, az adatfolyam és az étlaplap azonosságát. Teljesen üres, duplikált, hibás vagy hiányos bemenet esetén nem frissít.
- A felhasználói nézet egy fő témamenüt kapott; a régi böngészők a Kutatási háttérből érhetők el. Az étlapvizualizáció a Dashboard adatfolyamból dolgozik; a régi Elefánt-étlap történeti. A savanyúság / köret saláta kategória kikerül az önálló fogások statisztikájából.
- Egyes eredeti komponensek még indexalapúak, és a kutatási háttér nyers megjelenítése nem minden esetben őrzi meg az eredeti üres sorokat. A vizualizáció nem teljes ár- és tételnormalizálás, a hiányos összetevők kulcsszavas keresése csak közelítés.
- Következő: meetingre rendezett nyitóoldal, ebédmenük összehasonlítása, versenytárskártyák, kalkulátorok és mobilos átvizsgálás. Részletes P2–P7 UX-feladatok még hátravannak.
- A GitHub-forrás önmagában nem kapcsolódik a ChatGPT Site publikálásához; automatikus GitHub-telepítés nincs igazolva.

## 2026-11-11 – meetingkezdő és ebédmenü

- Új kérdésközpontú nyitóoldal és négy megbeszélési pont készült; megmaradt a kutatási háttér, a vizualizáció és a kalkulátor.
- Az ebédmenüben külön két- és háromfogásos, csatorna- és ármód-szűrő, kártyás rangsor és kinyitható részletek működnek. A november 9-i Oliva és Skorpió ajánlatok a korábbi időszakoktól külön, forrásellenőrzést igénylő megfigyelésekként jelennek meg, végösszeg és csatorna igazolása nélkül.
- Ellenőrizve: asztali előnézet, két- és háromfogásos váltás, árak és hiányzó díjak, forgatókönyv alapértéke, JavaScript szintaxis. Mobil böngészős ellenőrzés még szükséges.
- Következő: éttermi versenytárskártyák, étlapok részletesebb összehasonlítása, kiszállítási modell javítása, mobilteszt. Az új nyitóoldal korlátozott megfigyeléseket mutat, nem végleges üzleti ajánlásokat.
