# Elefánt Piackép – fejlesztési állapot

## Vélemények élő ellenőrzése és kontextusa (2026-11-11)

- Az éles dashboardon a versenytárskártyák és a Chill értékelései, témái, dátumai és linkjei megjelentek. A kezdőlapon a 23 kétfogásos megfigyelés friss szövege is megjelent. A kártya kinyitását ellenőriztük; a forrásoldalak és mobil nem lettek átfogóan tesztelve.
- A véleménykártyákhoz hozzáadtuk a forrássorban lévő kutatási összefoglalót és bizonytalansági megjegyzést; ez megelőzi a vegyes időpontú kritikák félreértelmezését. A módosítás szintaxisát és a kontextus megjelenését tesztadatokkal ellenőriztük. Éles közzététele még nincs igazolva; a szöveg részben angol forrásadat.
- Következő: új kontextus ellenőrzése a Pages oldalon, majd mobilvizsgálat és a P1 forrásfrissesség és többfájlos import kérdése.

## Versenytársak: véleménytémák (2026-11-11)

- A versenytárskártyákhoz kinyitható értékelés- és témarész került, a mentett Ratings 2026-11-09 és Review themes lapokból, pontos étteremnév-aliasokkal. Platform/forrás, érték, véleményszám, eredeti adat ideje vagy megjegyzése, ellenőrzés dátuma, link és témák polaritása látszik; az aggregátorok nem élő értékelések és a témapéldák nem reprezentatívak. Hiányzó kapcsolatok külön jelölve.
- A forráslapok élő tartalma és szerkezete célzottan ellenőrizve; a dashboard továbbra is régi mentett snapshotot használ, nem történt Sheet-import. JS-szintaxis és szintetikus teszt pozitív/negatív hozzárendelésre, dátumokra/hiányokra részben sikerült. Éles telepítés, valódi adatokkal és mobilon történő böngészős ellenőrzés hátra van.
- Következő: Pages friss commit publikációjának ellenőrzése, kártyák megnyitása/források vizsgálata, mobil; majd adatfrissítés és import atomi biztonsága.

## Marketingbenchmark éles ellenőrzés (2026-11-11)

- A felhasználó képernyőképe szerint a f256672 commit Pages buildje sikerült, deploy akkor még folyamatban volt. Ezután az élő dashboardon megjelent a Marketingbenchmark, mindkét követőlista és a posztpéldák. A Chill étteremre szűrés böngészőben működött, a forráslapok lenyithatók. Mobilnézet és szűrő visszaállítása még ellenőrzendő.
- Az adatok történeti pillanatképek; az éles Sheet automatikus szinkronja nincs beállítva. Következő: az éles verzió és az ebédkezdő új szövegének ellenőrzése, majd forrással dokumentált vendégvélemények és adatfrissesség.

## Posztpéldák és közzétételi elakadás (2026-11-11)

- A marketingbenchmark immár a Social live read 2026-11-09 Posts részéből megfigyelt posztkártyákat és étteremszűrőt készít. Külön kezeli a reakciót, hozzászólást, megosztást, nem látható adatot; a profillinket nem állítja posztlinknek. Adat- és időkülönbségi figyelmeztetés látható. A Node-teszt a forrássorral, hiánnyal, profillinkkel és üres forrással sikerült. A szűrő böngészőben még teszteletlen.
- Az éles GitHub Pages ismét ellenőrizve: továbbra is az Újranyitás menüpont és a régi két ajánlatos kezdőszöveg látható, azaz az új commitok nem igazoltan jutottak ki. A build/deploy okát az Actions / Pages felületen kell feltárni. A benchmark kódja a GitHub main ágon van, nem tekinthető ellenőrzött éles funkciónak.
- Következő: GitHub Pages build / deploy helyreállítása, majd követők, posztszűrő és mobil tesztelése; utána forrásadatok frissessége és review-témák.

## Marketingbenchmark első lépése (2026-11-11)

- A Marketingbenchmark menüpontban Facebook- és Instagram-követők összehasonlítása öt vizsgált profilra, forrással, dátummal, hiányokkal és az Oliva közös profiljára vonatkozó megjegyzéssel. A korábbi nyitási feladatkártyák helyét a kért benchmark vette át; a nyers forráslapok továbbra is megnyithatók.
- A Social and ads és Social live read lapokból a mentett pillanatkép adatait olvassa; nem élő kapcsolat. Külön Instagram-megfigyelést akkor vesz át, amikor az első forrásban nincs szám. Fricska hiányzó száma nem nulla. Node ellenőrzés: JS szintaxis, részletes érték, másodlagos forrás és hiányzó érték. Élő oldali és mobilos ellenőrzés még szükséges.
- A forrástábla metaadata most 35 munkalapot mutat; a teljes korábbi snapshot 34 lapos, az ebédárak külön frissebbek. A Napi menü árak lapon 32 rekord látható, de teljes egyezőség és további lapok változásai nem lettek ellenőrizve. A lap neveinek és a social két forrásnak célzott beolvasása megtörtént.
- Következő: a benchmark telepítésének böngészős ellenőrzése és mobilpróba; P1 teljes frissítés/importbiztonság, majd forrásolt posztpéldák és véleménytémák.

## Ebédösszesítő javítás és élő ellenőrzés (2026-11-11)

- A kezdőlap korábban megtévesztően két, dátum alapján kiválasztott megfigyelést nevezett a november 9-i gyűjtésnek. Most a teljes betöltött kétfogásos ármegfigyeléseket számlálja, jelezve az eltérő csatornákat, időszakokat és ismétlődő helyeket. Szintetikus adatokkal és üres adattal, valamint JavaScript-szintaxissal ellenőrizve; a friss publikáció böngészős ellenőrzése még szükséges.
- Élő oldalon ellenőrizve: kétfogásosról háromfogásosra szűrés (23-ról 5 megfigyelés), ebédkalkulátor 4000 Ft/35% mellett 2600 Ft, kiszállítási alapmodell és nullás kapacitás figyelmeztetés. Mobil és többi interakció nincs átfogóan tesztelve. A Sheet aktuális állapotát ez a kör nem ellenőrizte.
- Következő: közzétett javítás ellenőrzése; forrástábla és vegyes adatsnapshot összevetése, importbiztonság, majd marketingbenchmark.

## GitHub Pages elérhető (2026-11-11)

- A https://kittiborissza.github.io/Elefant-piackutat-s/ böngészőben átirányít a dist/ dashboardra; a nyitóoldal és a kutatási adatok betöltődtek. A felület nyilvános. Az összes funkció, mobilnézet, kiszállítási módosítás és az éppen publikált commit azonossága még nem ellenőrzött.
- Következő: a fontos interakciók és a mobilnézet ellenőrzése; utána P1 adatfrissesség és import, majd P5a marketingbenchmark. A Sheet nem élő kapcsolat.

## Folytatási pont – kiszállítási hibajavítás (2026-11-11)

- A felhasználó képernyőképe alapján a Pages beállítása Deploy from a branch, main és /(root); az első építés folyamatban volt. Az ismételt böngészős ellenőrzésnél az URL továbbra is 404. A beállítás helyessége látható, sikeres publikáció nincs igazolva; a telepítés hibáját vagy folyamatát ellenőrizni kell.
- A csatornaárak különbsége és százaléka csak két pozitív, numerikus ár esetén számolódik; hiányzó árnál Nem igazolt jelenik meg. A kapacitásfigyelmeztetés nulla kapacitásnál nem ad hamis megnyugtatást.
- Ellenőrzés: JavaScript-szintaxis és a két összehasonlítás hiányzó/érvényes árakkal, valamint a kapacitásüzenet három helyzetben Node alatt. A módosítás böngészős tesztje és publikációja még hiányzik; az adatok nem frissültek.
- Következő: GitHub Actions Pages build állapotának tisztázása és működő oldal ellenőrzése, P1 importbiztonság és friss Sheet-snapshot; ezután marketingbenchmark.

## Folytatási pont – importvédelem (2026-11-11)

- A GitHub Pages várható címe böngészőben 404 (Site not found); a beállítási oldal az aktuális böngészőből nem elérhető, így a Pages konfigurációja nem ellenőrizhető vagy módosítható itt. A GitHub repó publikus és a gyökér index a dist/ könyvtárba mutat.
- A scripts/import_snapshot.py most a teljes 47 oszlop nevét és sorrendjét ellenőrzi a meglévő dashboard-snapshot alapján, mert a felület pozíció szerint olvas. Eltérésnél import előtt leáll. Szintetikus XLSX-teszt: helyes fejléc sikeres, felcserélt fejléc elutasított, a korábbi kimenet változatlan.
- A forrásadatok nem frissültek. Következő: Pages hozzáférés és beállítás main/root forrással, majd a nyilvános URL, adatok és interakciók ellenőrzése; P1-ben még hátra van a többfájlos import atomi cseréje és a Sheet frissességének ellenőrzése.

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
