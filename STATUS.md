# Elefánt Piackép – fejlesztési állapot

## Marketing és vélemények – tervezési mérföldkő (2026-11-11)

- A ROADMAP.md P5a szakasza rögzíti a követőszámok, posztpéldák és vendégvélemények összehasonlító felületi tervét és külön megvalósítási lépéseit. A felhasználó pontosítása szerint a benchmark nem tartalmaz feladatlistát, kampánytervet vagy tartalomnaptárt. Ez terv; az új felületek még nincsenek megvalósítva.
- A GitHub Pages ellenőrzése és a megbízható adatfrissítés az első; ezek után a követőszámok és posztpéldák a meeting érdekében előrehozhatók. A forrásokat, dátumokat és hiányokat meg kell jeleníteni.

## Aktuális folytatási pont – GitHub-only (2026-11-11)

- A korábbi ChatGPT Site elhagyott; csak a GitHub repó változik. Részletes, prioritásos terv: ROADMAP.md.
- Az ebédmenü-árlap 32 megfigyeléssel frissült párhuzamos munkában; a többi adat korábbi kivonat. Közzétett GitHub dashboard URL nincs igazolva.
- A gyökér index.html továbbvisz a dist/ alkalmazásba, ha a GitHub Pages main/root beállítás aktív. A Pages beállítása, publikációja és a működő URL még nem ellenőrzött; a feladat nincs kész.
- Következő lépés: Pages-hozzáférés és kiadás ellenőrzése; utána a vegyes adatfrissesség, importvédelem és a friss ebédmenüsorok integrációjának alapos ellenőrzése. A munkát mindig aktuális main HEAD alapján folytasd.

## 2026-11-11 – ebédmenü árak frissítése

- A Napi menü árak forráslap 32 ármegfigyelése került be; csak ez a munkalap frissült, a többi kutatási adat korábbi pillanatkép. A frissítés ideje külön szerepel a nyitóoldalon.
- A menülistában csatornaszűrésnél Wolt és kiszállítás is választható; az érvényesség, a csatorna és az egyetemi jogosultság figyelmeztetése látható. A régi november 9-i külön gyűjtésből már nem adunk hozzá potenciálisan duplikált sorokat.
- Az adatfrissítés továbbra is kézi; sem a Google Sheets, sem a GitHub nem frissíti automatikusan a privát ChatGPT Site-ot.

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

## 2026-11-11 – versenytárskártyák

- A versenytársak nézet öt előzetes meetingkártyát mutat: Chill, Oliva, Fricska, Gusto 13 és Skorpió. A források szerinti cím, kínálat, dokumentált csatornák, meglévő ebédmenü-megfigyelések, valamint ahol van, becsült gyalogos és légvonalbeli távolság szerepel; a kiválasztás nem végleges.
- A kinyitható étlap-példák az adatfolyam helyszíni, önálló fogásaiból származnak, forrással és ellenőrzési dátummal. A korábbi nyers távolság-, értékelés-, vélemény- és éttermi adatok megmaradtak.
- Ellenőrizve: asztali előnézet, öt kártya és a Chill kinyitható ételpéldái. Az útvonal és a régi adatok friss helyszíni ellenőrzése, mobilos teszt még szükséges.
- Következő: hasonló ételek árbenchmarkja, Wolt- és kapacitásnézet javítása, használható véleménytémák, mobilteszt.
