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

## Soft launch / GitHub Pages
Branch: `soft-launch-rc5`

Valmis:
- RC5 standalone build -> index.html
- privacy.html
- updates.html
- manifest.webmanifest
- sw.js
- GitHub Pages workflow
- workflow julkaisee vain varsinaisen sivuston tiedostot erillisen `_site`-hakemiston kautta

GitHub Actions -run käynnistyy oikein, mutta pysähtyy tällä hetkellä `actions/configure-pages`-vaiheeseen, koska repository Pages ei ole vielä käytössä.

Tarvittava omistajan asetus:
`Settings -> Pages -> Build and deployment -> Source: GitHub Actions`

Tämän jälkeen uusi push branchiin käynnistää valmiin deployn.

## PWA
Manifest + service worker ovat mukana. Lopulliseen asennuskelpoiseen PWA-brändiin puuttuvat vielä 192x192 ja 512x512 sovellusikonit. Chromiumin installability-vaatimukset täytetään ikonivaiheessa ennen varsinaista PWA-markkinointia.

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
1. GitHub Pages Source -> GitHub Actions.
2. Trigger soft-launch-rc5 deploy.
3. Safari + Chrome + Android HTTPS regression.
4. Vahvista ja rekisteröi sanaristeys.fi.
5. Luo tuki@sanaristeys.fi.
6. Tee lopullinen app icon / PWA icon set.
7. Soft launch.

Täyttä tuotannon kehityspolkua ei julkaista Pagesiin. Drive säilyttää täydet release-handoffit.
