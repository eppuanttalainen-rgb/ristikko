# Soft-launch external setup — RC5

## HTTPS test branch
Branch: `soft-launch-rc5`

Contains:
- RC5 standalone build as index.html
- privacy.html
- updates.html
- manifest.webmanifest
- service worker
- GitHub Pages workflow

GitHub Pages still requires the repository owner to enable:
Settings -> Pages -> Build and deployment -> Source: GitHub Actions.

After that, a new push to soft-launch-rc5 will deploy the test site. The connector-created workflow commit did not trigger a run before Pages was enabled.

## Domain recommendation
Primary: `sanaristeys.fi`.

Recommended registrar for the current plan: Domainhotelli, domain-only.
2026 published pricing:
- first year .fi: EUR 12.90 + VAT
- renewal: EUR 20.90/year + VAT

Availability must still be confirmed in Traficom/registrar domain search immediately before purchase.

## DNS + support email
After registration:
- move/use DNS at Cloudflare
- use Cloudflare Email Routing for inbound `tuki@sanaristeys.fi`
- route it to the chosen existing inbox
- set app-config supportEmail to `tuki@sanaristeys.fi`

Cloudflare Email Routing can receive/forward custom-domain mail on the free plan. A separate mailbox/SMTP can be added later if branded outbound replies are needed.

## Long-term hosting
GitHub Pages is only the immediate HTTPS test path.
Preferred production architecture remains Cloudflare Pages + sanaristeys.fi.
