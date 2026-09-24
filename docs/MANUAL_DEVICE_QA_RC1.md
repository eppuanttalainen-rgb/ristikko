# Manual device QA — RC1

## Android Chrome (required)
- Home/library render without horizontal overflow.
- Open Easy/Medium/Hard puzzles.
- Tap cells and crossing direction switching.
- Å/Ä/Ö and backspace.
- Grid zoom 100/125/150/175%.
- Browser pinch zoom.
- A+ text size.
- Calm/Challenge modes.
- Progress persists after close/reopen.
- Reset cancel preserves state; reset confirm clears it.
- Hint/check flow.
- Portrait -> landscape -> portrait remains usable.

## Desktop (required, at least one modern browser)
- App centered at max width.
- Keyboard letters, Backspace, Left/Right.
- Visible tab focus.
- Refresh preserves progress.
- No uncaught console errors in normal flow.

## iPhone Safari (strongly recommended)
- Notch/Dynamic Island safe area.
- Home indicator safe area.
- Pinch zoom.
- Grid scrolling.
- Persistence after reopen.

Release only when Android + desktop are PASS and there is no P0/P1 issue.
