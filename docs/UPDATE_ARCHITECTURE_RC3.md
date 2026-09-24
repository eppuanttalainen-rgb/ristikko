# Update architecture — RC3

RC3 separates the application shell from crossword content.

## Stable application
- index.html
- app-config.js
- manifest.webmanifest
- sw.js

## Content
Production web builds load one stable path: `content/current.js`.

Current pack:
- version 2026.1
- 101 visible puzzles
- previousVersion: null
- addedPuzzleIds: []

A normal future batch is intended to be 6 reviewed puzzles (2 Easy + 2 Medium + 2 Hard). Factory still performs the editorial/quality gates. Only an APPROVED_FOR_GAME_IMPORT batch can become a candidate content pack.

Example future sequence:
- 2026.1 = 101
- 2026.2 = 107
- 2026.3 = 113

The app records the last content version separately from puzzle progress. When a later pack declares addedPuzzleIds, the app can notify the player about the new puzzles automatically.

The service worker treats `content/current.js` network-first, so an online player receives the newest pack while the last verified copy remains available offline.

Important: content updates remain reviewable releases. The helper only creates a candidate; it does not publish or bypass editorial/regression gates.
