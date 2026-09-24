# WEB/PWA RC1 preparation

Desktop Chrome manual QA is PASS. Android quick smoke is PROVISIONAL PASS. iPhone Safari remains pending because a local HTML file could not be opened directly in Safari.

A separate WEB RC1 package has been prepared for HTTPS testing:
- index.html: v0.3.39 RC1 plus PWA metadata
- manifest.webmanifest
- sw.js for light offline caching

The complete test build is stored in Drive, not committed to this public repository yet. This avoids publishing the unreleased game source before an explicit hosting/release decision.

When hosting is chosen:
1. deploy the WEB RC1 package over HTTPS;
2. test Safari from the actual URL;
3. test Add to Home Screen / standalone launch;
4. add final app icons before public PWA/app release.

No analytics, cookies, tracking, or external network dependencies are added by this package.
