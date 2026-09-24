# Sanaristeys

Oma versionhallintarepositorio Sanaristeys-pelille.

## Nykyinen release-tila
- Release handoff: v0.8.3 RC4
- App shell: v0.3.42 RC4
- Content: 2026.1
- Visible puzzles: 101
- Subtitle: Suomalaiset ristikot

## Sisältöbaseline
- Factory v0.7.6 READY (lukittu)
- 101 / 101 ristikkoa
- 32 Helppoa / 37 Keskitasoa / 32 Vaikeaa
- Production-sanapankki: 1749
- Geometriapankki: 67
- Aktiivikirjaston vihjeduplikaatit: 0

## RC4
- ristikkosisältö on erotettu sovelluksesta
- pieni +6 sisältöpäivitys ei vaadi app-shellin muuttamista
- Tietosuoja-sivu lisätty
- Uutta / päivityshistoria lisätty
- palaute-linkki aktivoituu supportEmail-konfiguraatiolla
- PWA/offline-rakenne valmis
- mainokset, analytiikka ja maksut edelleen OFF
- tuleva monetization bridge ja premium-entitlementit erotettu sisällöstä

## QA
- v0.3.42 release smoke: PASS
- 101 visible / 107 defined
- JS syntax: PASS
- Finnish keyboard: PASS
- content update candidate flow: PASS
- duplicate ID protection: PASS
- RC1 Desktop Chrome: PASS
- RC1 Android quick smoke: PROVISIONAL PASS
- Safari HTTPS smoke: pending

## Seuraava portti
1. Vahvista ja rekisteröi sanaristeys.fi, jos vapaa.
2. Deploy WEB RC4 HTTPS-testiosoitteeseen.
3. Safari + Chrome smoke.
4. Luo erillinen tukiosoite (esim. tuki@sanaristeys.fi) ja aseta se app-configiin.
5. Tee soft-launch-päätös.

Täyttä julkaisemattoman pelin sisältöpakettia ei säilytetä tässä julkisessa repossa. Drive säilyttää täydet release-handoffit.
