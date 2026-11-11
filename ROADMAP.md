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

## P5a – Marketing és vendégvélemények: UI-terv [megtervezve, nincs megvalósítva]

### Helye a navigációban

- A jelenlegi, hétpontos főmenüben az „Újranyitás” átnevezhető „Marketing és nyitás”-ra, megtartva a meglévő feladatokat és interakciókat. A menüponton belül két jól látható alfül: **„Mit csinálnak mások?”** és **„Elefánt újranyitása”**. A menü címét mobilon is tesztelni kell; ha nem fér, rövidebb „Marketing” cím megengedett.
- A vendégvélemények elsődleges helye a **Versenytársak** oldalon az adott étterem kártyája. Egy kapcsolódó **„Mit szeretnek a vendégek?”** összefoglaló a Marketing és nyitás oldalról is elérhető. Közös adatmodellre mutassanak; ugyanazt a véleményt nem tároljuk vagy számoljuk kétszer.
- Az Áttekintés oldalon legfeljebb egy rövid, forrással, dátummal és korláttal ellátott marketinges megfigyelés vagy az Elefánt kiugró posztja jelenjen meg, **„Megnézem a kommunikációt”** gombbal. A tulajdonosi döntések és ebédmenük továbbra is elsőbbséget kapnak.

### 1. „Mit csinálnak mások?” – követők

- A blokk kérdése: **„Mekkora közönséget építettek a környékbeli helyek?”** Az első nézet két vízszintes, könnyen összehasonlítható lista: Facebook és Instagram, öt vizsgált hely, forrás és megfigyelés dátuma. A listához tartozzon étterem- és platformszűrő, forrásmegnyitás és szűrőtörlés; a részletes elem az éttermi profilra mutasson.
- A 2026-11-09-i kutatásban rögzített kiinduló számok: Elefánt FB 3 792 / IG 637; Chill FB 6 242 / IG 659; Oliva hotel+étterem FB 10 081 / IG 3 170; Gusto 13 FB 17 173 / IG 2 051; Fricska FB 29 004 / IG nem igazolt. Ezek korábbi megfigyelések és forrásellenőrzést, illetve importfrissítést igényelhetnek, nem beégetendő állandó értékek.
- A két social lap eltérő pontosságú/kerekített és eltérő módon olvasott értékeket tartalmazhat; a külön nézetek közötti egyezést és megfigyelés körülményeit fel kell tüntetni. Nem olvasható Instagram-szám = „Nem sikerült ellenőrizni”, nem nulla. Az Oliva Facebook-profilja a hotel és az étterem közös oldala. Gusto Delicate és Gusto 13 külön profil, a követők nem adhatók össze.
- Követőszám nem azonos eléréssel, aktív közönséggel, vendégszámmal vagy hirdetési hatással; értelmező egy mondatot a grafikon mellett kell megjeleníteni. „Ember beszél erről” és „járt már itt” csak részletekben, saját definícióval és dátummal, nem vendég- vagy reachmutatóként.

### 2. Posztpéldák és témák

- **„Miket és hogyan kommunikálnak?”**: étterem és platform szerinti kártyák/lista; témaszűrők: heti menü, étel/fotó, szezonális ajánlat, esemény, nyitvatartás, egyéb, és csak dokumentált posztnál töltsük a címkét.
- Minden példán dátum vagy az eredeti relatív időmegjelölés a 2026-11-09-i megfigyelési dátummal, téma, platform, a látható reakció/komment/megosztás külön, és a konkrét posztlink, ha valóban megvan. Ha csak profillink van, jelölése **„Profil megnyitása”**; nem állítjuk, hogy posztlink. Forrásrészlet, kutatási dátum, bizonytalanság kinyitható.
- „–” = nem volt megjelenítve / ismeretlen; „nem olvasható” = nem ellenőrzött. Egyik sem automatikus 0. Ha a forrás nem mondja ki, ne következtessünk nullára.
- Egy november 9-én feljegyzett Elefánt, 2026-10-25-i „Néha meg kell állni…” fotós poszt **583 reakció, 14 hozzászólás, 20 megosztás**; ez forráspélda és kiugró megfigyelés, nem biztos következtetés. A posztot, a kontextust és lehetőleg a közvetlen linket ellenőrizni kell. Ne írjuk, hogy „bezárási poszt” vagy hogy sikert hozott, amíg ez nem igazolt.
- Referenciaként szerepelhetnek a táblázatból más menü/szezonális/esemény posztok, mindig pontos adat és dátum mellett. Ne számoljunk engagement rate-et az elérés hiányában, és ne állítsuk, hogy a különböző időpontú posztok egymással egyenlő feltételek mellett versenyeztek.
- A követőszám, reakció, komment, megosztás egymástól külön, és nem azonos eléréssel, forgalommal, foglalással, vásárlással vagy bevétellel. „Legsikeresebb” állítás csak az összehasonlítható mérés alátámasztásával.
- Látható állapot: Meta Ad Library aktív hirdetések nem voltak megbízhatóan olvashatók; nem állítható, hogy nincs hirdetés. Nincs mért médiaköltés, reach, megjelenítés, foglalás, eladás vagy kampánymegtérülés.

### 3. Vendégvélemények az étteremkártyákon

- Az étterem profilján „Vélemények” kinyitható rész: platformonként külön értékelés + véleményszám + eredeti forrás / közvetítő aggregátor + az **adat eredeti dátuma** és **ellenőrzés dátuma**. Az eltérő platformok és források nem képeznek közös átlagot; a régebbi aggregátoradat nem „aktuális Google-érték”.
- „A forrásban feljegyzett pozitív témák” és „További ellenőrzést igénylő panaszok” alatt rövid, étteremhez illesztett példák; az egyedi tapasztalat, keresési összefoglaló és teljes eredeti értékelés külön jelölve, forrás és dátum amennyiben van. Az Elefánt összesített terasz/helyszín témája dátum szerint nem lesz az elmúlt 12 hónap igazolt mintája.
- Nem mintavételes adatból ne írjuk: „a legtöbben panaszkodnak”, „a vendégek ezt szeretik” vagy a megállapítás reprezentatív. Nem ismert szám = nem ismert. Az eltérő időszakok és beszerezhetőségi korlátok megmaradnak.

### 4. „Elefánt újranyitása” – javaslatok és működtetés

- A felhasználó céljára épülő, javaslatnak jelölt tartalomkártyák: zárás/újranyitás és nyitvatartás, Google Cégprofil, új séf, új étlap, heti menü, ételfotó és rövid videó, meghívásos tesztvacsora, nyitási kampány.
- Minden kártya: **miért érdekes** (forrással alátámasztott megfigyelés, ha van), **javasolt lépés**, csatorna/formátum, szükséges anyag, felelős/határidő/jóváhagyás/állapot — ha nincs eldöntve, „Egyeztetendő”. A konkrét gyakoriság is javaslat és kapacitáshoz igazítandó, nem kész terv.
- Ha később szerkeszthető állapotmező kerül bele, tároló, tulajdonos, megosztás és frissítés utáni megmaradás világos legyen; hamis mentésjelzés tilos. Addig statikus megbeszélési lista.

### Adatforrás és fázisolás

- Forráslapok: **Social and ads**, **Social live read 2026-11-09**, **Ratings 2026-11-09**, **Review themes**, plusz az éttermi törzs és források. Az egyezés étterem/profil/platform alapján ellenőrzendő, aliasok és külön üzletek kézzel felülvizsgálva. A november 9-i megfigyelés nem élő csatornaadat; a külön lapok frissessége és importideje eltérhet.
- Az első megvalósítás előtt: az aktuális Sheet és a GitHub-pillanatkép ellenőrzése, másik munkakör frissítéseinek megőrzése, a vegyes importfrissesség javítása (P1). Olyan adatok kerüljenek ki, melyeknél az eredet és dátum megjeleníthető.
- **P5a.1**: követőszámok és hiányok két platformon, étteremválasztó, forrás; **P5a.2**: dokumentált posztpéldák és Elefánt-kiemelés; **P5a.3**: értékelések és témák a versenytárskártyákban; **P5a.4**: nyitási lehetőségek és tartalomműködés. Mindegyik önmagában használható, tesztelt és önállóan commitolható.
- Az új igényt tartsuk látható prioritásban: P0 működő GitHub-webcím és P1 megbízható aktuális adat/import után a P5a.1–2 előre hozható a meeting szempontjából, párhuzamosan a P2/P3-mal; P5a.3–4 ezután. A felhasználó kérésére itt csak a terv frissül, a UI megvalósítása későbbi lépés.
- Elfogadási feltételek: minden mutató mellett platform és dátum, hiányzó érték kezelése, öt hely adatainak spotellenőrzése, Gusto-különbség és Oliva-közös profil jelölése, reakció/megtekintés keverésének kizárása, ismeretlen hirdetésstátusz, források megnyitása, telefonos nézet és szűrők ellenőrzése, a jelenlegi kalkulátorok/étlapnézetek regressziótesztje.

## P6 – Minőség, mobil, adatkarbantartás és automatikus frissítés [nyitott]

- Kulcs képernyők telefonon, asztali böngészőben, billentyűzettel; szűrők, visszaállítás, nyitás, hibás vagy üres adatok, forráslinkek, adatdátum és regresszió ellenőrzése.
- Forráskritika és kutatási backlog: teljes/részleges/hozzáférhetetlen, hiányzó szolgáltatási díj, eltérő ár, működési státusz, forrás dátuma és ismert érvényesség.
- Biztonságos fenntartható adatkapcsolat feltérképezése; nem tehető nyilvánossá a Sheet és nem kerülhet titok a böngészőbe. Hiba esetén korábbi egész, validált snapshot maradjon. Ha nem megoldható, dokumentált kézi import.
- Kis elemszámok és bizonytalanság minden kapcsolódó megállapításnál látható. Az utolsó sikeres import, következő kutatási prioritások és működő státusz mindig tényszerű.

## Átadási feltételek

GitHubon dokumentált működő kód és állapot, ténylegesen ellenőrzött dashboard URL ha kész, adatok eredete és frissessége, elvégzett ellenőrzések, hiányzó funkciók és konkrét következő lépés. Ne jelölj késznek vagy élőnek nem tesztelt funkciót.
