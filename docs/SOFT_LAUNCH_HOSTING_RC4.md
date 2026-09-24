# Soft launch hosting — RC4

Suositeltu testihosting: Cloudflare Pages Direct Upload.

## Testi
- Workers & Pages
- Create application
- Drag and drop
- lataa Sanaristeys_WEB_RC4.zip
- käytä saatua *.pages.dev HTTPS-osoitetta Safari-/PWA-testissä

## Tuotanto
Pysyvä tuotantopolku kannattaa tehdä erillisenä projektina Git-integraatiolla tai Wrangler-deploylla. Direct Upload -projektia ei voi myöhemmin muuttaa Git-integrated-projektiksi.

## Custom domain
Kun sanaristeys.fi on rekisteröity, lisää se Pages-projektin Custom domains -kohtaan. Apex-domain vaatii domainin DNS-zonen/nameserverit Cloudflareen.
