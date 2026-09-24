# Native prep — RC5

Native-polku on suunniteltu Capacitor 8:lle.

Ehdotettu package/bundle ID: `fi.sanaristeys.app` (lukitaan lopullisesti ennen store-julkaisua).

Android:
- target API 36 current Play requirement huomioitava
- Play signing / closed testing / Data safety omana release-porttinaan

iOS:
- nykyinen App Store upload buildataan Xcode 26+ / iOS 26 SDK+:lla
- App Privacy omana porttinaan

Ensimmäiseen native-testibuildiin ei lisätä mainoksia tai billing-SDK:ta. Rahastus lisätään myöhemmin erillisenä privacy/store-compliance-julkaisuna.
