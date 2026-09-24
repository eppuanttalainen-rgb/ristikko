# Sanaristeys

Oma versionhallintarepositorio Sanaristeys-pelille.

## Nykyinen release-tila
- Release handoff: v0.8.4 RC5
- App shell: v0.3.43 RC5
- Content: 2026.1
- Content format: JSON schema v1
- Visible puzzles: 101
- Subtitle: Suomalaiset ristikot

## Sisältöbaseline
- Factory v0.7.6 READY (lukittu)
- 101 / 101 ristikkoa
- 32 Helppoa / 37 Keskitasoa / 32 Vaikeaa
- Production-sanapankki: 1749
- Geometriapankki: 67
- Aktiivikirjaston vihjeduplikaatit: 0

## RC5
- ristikkosisältö on puhdasta dataa: `content/current.json`
- app shell ei suorita verkosta ladattavaa ristikkopäivityskoodia
- +6 sisältöpäivitys ei vaadi app-shell-muutosta
- remote sisältö voidaan cachettaa native-versiossa offline-käyttöä varten
- bundled 101 ristikon paketti säilyy fallbackina
- Tietosuoja + Uutta -sivut mukana
- supportEmail-koukku valmiina
- PWA/offline-rakenne valmis
- mainokset, analytiikka ja maksut OFF
- Capacitor 8 native-prep tehty erilliseen handoffiin

## QA
- RC5 bundle regression: PASS
- 101 visible / 107 defined
- 3101 active entries
- exact active clue duplicates: 0
- JS syntax: PASS
- JSON schema/content: PASS
- mechanical content update 101 -> 102: PASS
- duplicate ID protection: PASS
- standalone syntax: PASS
- RC1 Desktop Chrome: PASS
- RC1 Android quick smoke: PROVISIONAL PASS
- Safari HTTPS smoke: pending

## Seuraava portti
1. Vahvista ja rekisteröi sanaristeys.fi, jos vapaa.
2. Deploy WEB RC5 HTTPS-testiosoitteeseen.
3. Safari + Chrome + Android quick regression.
4. Luo erillinen tukiosoite (esim. tuki@sanaristeys.fi).
5. Soft launch.
6. Android Capacitor / Play closed test rinnalle.

Täyttä julkaisemattoman pelin sisältöpakettia ei säilytetä tässä julkisessa repossa. Drive säilyttää täydet release-handoffit.
