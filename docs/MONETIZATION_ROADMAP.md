# Monetization roadmap

Commercial intent is part of the architecture, but RC3 enables no ads, tracking, billing SDK or personal-data collection.

Recommended order:
1. Soft launch free and ad-free; validate usage, retention and update cadence.
2. Add light ads outside active crossword solving. Do not routinely interrupt a crossword.
3. Evaluate optional rewarded ads for hints.
4. Add an ad-free premium entitlement as the simplest first paid product.
5. Evaluate premium content packs or subscription only after real demand is visible.

Architecture rule:
- puzzle content
- player progress
- monetization entitlements
- ad/billing integrations

stay separate.

RC3 reserves a monetization bridge and a separate entitlement storage key. A future native wrapper can implement AdMob / store billing while the crossword content format remains unchanged.

Adding ads later is a separate privacy/store-compliance release gate.
