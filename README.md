# Sanaristeys

Oma versionhallintarepositorio Sanaristeys-pelille.

## Nykyinen release-tila
- Release handoff: v0.8.4 RC5
- App shell: v0.3.43 RC5
- Content: 2026.1
- Content format: JSON schema v1
- Visible puzzles: 101
- Subtitle: Suomalaiset ristikot
- HTTPS soft launch: LIVE
- Test URL: https://eppuanttalainen-rgb.github.io/ristikko/

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
Public site is deployed through GitHub Actions from main, while the actual release build is checked out from `soft-launch-rc5`.

Public artifact contains only:
- index.html
- privacy.html
- updates.html
- manifest.webmanifest
- sw.js

Latest successful Pages run:
- run id: 36151520668
- conclusion: success
- deployed URL: https://eppuanttalainen-rgb.github.io/ristikko/

## PWA
Manifest + service worker ovat mukana. Lopulliseen asennuskelpoiseen PWA-brändiin puuttuvat vielä 192x192 ja 512x512 sovellusikonit.

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
- GitHub Pages HTTPS deploy: PASS
- RC1 Desktop Chrome: PASS
- RC1 Android quick smoke: PROVISIONAL PASS
- Safari HTTPS smoke: NEXT

## Seuraava portti
1. Safari HTTPS smoke live-URL:sta.
2. Chrome + Android HTTPS quick regression.
3. Vahvista ja rekisteröi sanaristeys.fi.
4. Luo tuki@sanaristeys.fi.
5. Tee lopullinen app icon / PWA icon set.
6. Soft launch.

Drive säilyttää täydet release-handoffit.
