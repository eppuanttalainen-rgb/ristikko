# Sanaristeys

Oma versionhallintarepositorio Sanaristeys-pelille.

## Brändi
- Nimi: Sanaristeys
- Alaotsikko: Suomalaiset ristikot
- Release: v0.8.2 RC3
- App shell: v0.3.41 RC3
- Content: 2026.1 / 101 näkyvää ristikkoa

## Sisältöbaseline
- Factory: v0.7.6 READY (lukittu)
- Sisältö: 101 / 101 ristikkoa
- Jakauma: 32 Helppoa / 37 Keskitasoa / 32 Vaikeaa
- Production-sanapankki: 1749 sanaa
- Geometriapankki: 67 perhettä
- Aktiivikirjaston vihjeduplikaatit: 0

## RC3
Ristikkosisältö on erotettu sovelluksesta. Tuleva normaali +6 ristikon päivitys voidaan julkaista uutena versionoituna `content/current.js`-pakettina ilman käyttöliittymän tai tallennuslogiikan muutosta.

Sisältöversio tallennetaan erikseen pelaajan etenemisestä. Uusi sisältöpaketti voi ilmoittaa `addedPuzzleIds`-listan, jolloin peli pystyy näyttämään automaattisesti ilmoituksen uusista ristikoista.

PWA-service worker hakee sisältöpaketin network-first-periaatteella ja säilyttää viimeisen varmennetun version offline-käyttöä varten.

## Ansaintavalmius
RC3:ssa on erillinen, pois päältä oleva monetization bridge ja entitlement-tallennus. Ensimmäinen soft launch pysyy ilman mainoksia, seurantaa tai maksukirjastoja. Myöhemmin mainokset/premium voidaan toteuttaa ilman että ristikkodata tai etenemistallennukset sidotaan niihin.

## QA
- content 2026.1: 101 visible / 107 defined
- Sanaristeys release smoke: PASS
- Finnish keyboard + JS syntax: PASS
- mekaaninen content update -testi: PASS
- duplicate puzzle ID protection: PASS
- RC1 Desktop Chrome: PASS
- RC1 Android quick smoke: PROVISIONAL PASS
- RC3 tarvitsee vielä nopean laiteregression
- iPhone Safari testataan HTTPS-hostatusta versiosta

Täyttä julkaisemattoman pelin sisältöpakettia ei säilytetä tässä julkisessa repossa. Drive säilyttää täydet release-handoffit.
