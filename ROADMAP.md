# Elefánt Piackép – GitHub munkaterv

Frissítve: 2026-11-11. A GitHub-repó az elsődleges forrás. A korábbi ChatGPT Site elhagyott; a fejlesztés nem módosítja vagy teszi közzé ott az oldalt.

## Állapot és munkarend

- GitHub: https://github.com/KittiBorissza/Elefant-piackutat-s
- A terv rögzítésekor a main ágon már szerepelt az ebédmenü-adatok külön frissítése; a legújabb commitot munka előtt mindig olvasd be.
- A futó kód a dist mappában található. Meglévő: kérdésközpontú áttekintés, ebédmenü-szűrés és kalkulátor, étlapvizualizáció, öt versenytárskártya, csatornaárak és fedezet-, kapacitásmodell, kutatási háttér.
- Az adatbeolvasás jelenleg kézi XLSX-import; a snapshot metaadata: dist/snapshot-meta.json, az import: scripts/import_snapshot.py. A 2026-11-11 11:46-os pillanatkép 34 lapot és 585 ármegfigyelést rögzített. A számok nem statikus célok.
- Az aktuális Google Sheet 35 lapot jelez. Egy párhuzamos munkakör a Napi menü árak lap 32 ármegfigyelését külön frissítette a repóban; a többi kutatási adat korábbi pillanatkép. A további változtatások előtt ellenőrizni kell a friss commitot és a forrássorokat.
- A gyökér index.html átirányít a dist/ mappába; a GitHubon elérhető weblap telepítése nincs igazolva. GitHub Pages / más GitHub-alapú hosting állapotát és konfigurálhatóságát ellenőrizni kell; a régi Site állapota a feladatnak nem része.
- A repó nyilvános a tulajdonos kifejezett döntése alapján. Fel kell tüntetni, hogy a benne levő JSON-adatok is nyilvánosak.

Minden szakasz után:
1. Ellenőrizd a main HEAD-et és az új változtatások ütközését; ne írj felül más munkát.
2. A legkisebb önálló és hasznos változtatást készítsd el, ellenőrizd a forrássorokat és funkciókat.
3. Írd frissre a STATUS.md elején az állapotot: mi kész, mi ellenőrzött, melyik adatpillanatkép él, mi a következő egy lépés, blokkolók.
4. Commit/push az engedélyezett GitHub repóba; az aktuális működő verziót őrizd meg. Ha telepítés már be van állítva, csak sikeres ellenőrzés után tedd közzé és ellenőrizd a pontos verziót.
5. Token- vagy munkamegszakítás előtt maradjon mentett, visszaállítható állapot. A STATUS.md mindig az igazság; a terveket nem szabad elkészültként feltüntetni.

## P0 – GitHub-on ténylegesen megnyitható dashboard [nyitott]

- Felmérni a repo hosting / GitHub Pages státuszát, szükséges jogosultságokat, támogatott közzétételi beállítást. A dist/ gyökér; a sima fájllink nem működő dashboard.
- A felhasználó már jóváhagyta a publikus repót, de a dashboard jelenlegi Site-változata privát. A publikus repo nem egyenértékű automatikus engedéllyel új, nyilvánosan hostolt oldalra, ha az adat- és hozzáférési következmények nem egyértelműek. A felhasználó GitHub-változatra áttérése szerinti nyilvános hosting gyakorlati következményét jelezni kell; a tényleges döntés a kért közzétételi környezettel és jogosultságokkal összhangban történjen.
- Publikáláshoz helyes útvonalú index, relatív assetek, hozzáférhető JSON, automatizálható workflow vagy támogatott branch-forrás; sem secret, sem privát token ne kerüljön frontendbe.
- Valódi publikus URL és ugyanazon commit működésének megfigyelése: kezdőlap, menü, JSON, kalkulátor, mobil. 404, jogosultsági probléma vagy nem elérhető deploy esetén ne állítsd késznek.
- Ne töröld a korábbi Site-ot.

## P1 – Friss kutatási adat átvétele [nyitott]

- Az aktuális Sheet metaadatait és tartalmát frissen beolvasni, külön az új ebédmenü-forrássorokkal, dátumokkal, forrásokkal. Az új lap címe nem azonos kész megfigyelésekkel.
- P1 előtt a jelenlegi importot auditálni: fejléc- és típusellenőrzés mellett az alkalmazáskód még számozott indexeket használ, ezért oszlopok átrendezésekor jelenleg hibás értelmezés lehetséges. Fejléc szerint rendezni vagy minden elvárt indexet ellenőrizni.
- Importáció stagingbe; dátum és forrás megőrzése; az adatfolyam és központi lap rekord-ID-einek, duplikátumainak, kapacitásának ellenőrzése. Nem minden Sheet-lap egységes tábla. A képletes adatfolyamba nem írunk.
- A korábbi november 9-i étlapgyűjteményt nem duplikáljuk automatikusan; a névegyezés csak jelölt. Napi menü elkülönítése; csatorna, csomag, fogásszám és érvényesség pontos kezelése; ismeretlen díj nem nulla.
- Az import fájlonkénti os.replace nem jelent többfájlos atomi tranzakciót; javítani vagy verziózott staging + egyetlen pointer révén biztosítani, hogy megszakadás ne keverjen régi/új adatokat.
- Ellenőrzés: új rekord, duplikált azonosító, hiányzó adat, rossz fejléc és elérhetetlen forrás. Snapshot dátum és kézi/automatikus állapot a UI-ban. Forrásból összevetett példák.
- Nincs nyilvános Sheet vagy kliensoldali titok, sem állítólagos élő kapcsolat.

## P2 – Ebédmenü meetingváltozat [részben kész]

- Az új forrásokkal érdemben frissíteni az előző szakasz után; külön két- és háromfogás, helyben/elvitel/nem egyértelmű.
- Ár, dátum, csatorna, időszak, tény/hipotézis, szervizdíj, csomagolás és bizonyosság, az eredeti forrássorhoz kapcsolva. Az ismeretlen fizetendő nem nulla. Külön fogások nem csomagok.
- Történeti ajánlatok elválasztása. Részenként vizsgálni a november 9-i Oliva/Skorpió adat átfedését és ellenőrzöttségét. Mobilkártya, rangsor és szűrők ellenőrzése.
- Példaköltségek és adózási alap egyértelmű; a különbözet nem nettó profit.

## P3 – Hasonló ételek és árazás [részben kész]

- Forrásonként tiszta jelentés: étterem, kanonikus fogás, változat, csatorna és megfigyelési idő. Ugyanazt ne számoljuk többször; ismeretlen ID nem olvasztható önkényesen össze.
- Főétel/köret és savanyúság, külön méretek, felárak, gyerekadagok, árütközések, szervizdíj-típusok pontosítása; korábbi 900 Ft-os káposztasaláta hiba védőtesztje.
- Összehasonlítható leves, csirke, sertés, kacsa, marha, tészta, vega és desszert; minimum, medián, maximum, n, éttermek, példák, forrás és dátum. Ne állítsunk keresletet a kínálatból.
- Az Elefánt 39 átvett történeti tételét külön címkével kezelni; csatorna és szerviz nem bizonyított. A másik gyűjtést ne adjuk automatikusan a központihoz.
- A sushi és pizza háttér/inspiráció szűrhető; releváns összehasonlítás nem torzulhat.

## P4 – Kiszállítás és kapacitás [részben kész]

- Csatornaárak: étterem/étel, referencia pontos típusa, Wolt, eltérés, adag- és köretegyezés, dátum, forrás, ismeretlen díjak; a bizonytalan méreteket a szigorú átlagból kizárni.
- A fedezetkalkulátor validálása: csatornánként költségek és áfaalap, negatív/üres/100%-os jutalék, nullával osztás, összehasonlító felár; egyértelműen szemléltető, nem nettó profit.
- Kapacitásmodell: megrendelések, kapacitás, csúcs, elviteli arány, kiszorítás; az előkészítési idő hatása csak ha a modellt alátámasztják az adatok. Túlkapacitáskor ne ígérjen teljesítést, egyébként explicit figyelmeztetés.
- Azonos rendelésállomány, számítási bázis és korlátozás értelmezése dokumentált, próbaszámolásokkal ellenőrzött.

## P5 – Versenytársak, értékelések, marketing és megvalósítás [részben kész]

- Az öt előzetes étteremkártya meglévő, de a források október-novemberi megfigyelések: működés, ár, távolság és csatorna frissessége ellenőrizendő. Nem talált nem jelent nem létezőt.
- Platformonként külön pontszám + véleményszám, idő és eredet; nincs összemosott átlag. Témák és forrásolt példák; gyakoriság csak megfelelő mintával.
- A közeli és távolabbi versenytársak szűrése, pozicionálási következtetések jelölése.
- Marketing és nyitás: séf, étlap, nyitvatartás, Google Cégprofil, heti menü, forgatás és meghívásos tesztvacsora. Felelős, dátum, jóváhagyás csak ha ténylegesen megvan; szerkesztésnél tárolás és megmaradás jelezve.
- Befejezéskor megbeszélésre nyomtatható döntéslista.

## P6 – Minőség, mobil, adatkarbantartás és automatikus frissítés [nyitott]

- Kulcs képernyők telefonon, asztali böngészőben, billentyűzettel; szűrők, visszaállítás, nyitás, hibás vagy üres adatok, forráslinkek, adatdátum és regresszió ellenőrzése.
- Forráskritika és kutatási backlog: teljes/részleges/hozzáférhetetlen, hiányzó szolgáltatási díj, eltérő ár, működési státusz, forrás dátuma és ismert érvényesség.
- Biztonságos fenntartható adatkapcsolat feltérképezése; nem tehető nyilvánossá a Sheet és nem kerülhet titok a böngészőbe. Hiba esetén korábbi egész, validált snapshot maradjon. Ha nem megoldható, dokumentált kézi import.
- Kis elemszámok és bizonytalanság minden kapcsolódó megállapításnál látható. Az utolsó sikeres import, következő kutatási prioritások és működő státusz mindig tényszerű.

## Átadási feltételek

GitHubon dokumentált működő kód és állapot, ténylegesen ellenőrzött dashboard URL ha kész, adatok eredete és frissessége, elvégzett ellenőrzések, hiányzó funkciók és konkrét következő lépés. Ne jelölj késznek vagy élőnek nem tesztelt funkciót.
