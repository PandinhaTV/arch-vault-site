---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code]
publish: true
---

# Localization

`LocalizationManager`, using Unity Localization. Language is switchable from the Accessibility section of the pause menu.

**Portuguese and English** (2026-07-31). [[Dialogue System]] text is localised — each line has an ID that the system resolves. Cutscenes need no localisation because they contain no dialogue, and no voice needs it because nobody speaks in words.

## Known bug

`LocalizationManager.Awake()` raises:

```
DontDestroyOnLoad only works for root GameObjects or components on root GameObjects.
```

The manager is nested under a parent object, so `DontDestroyOnLoad` does nothing. The same problem affects `SaveManager` — see [[Save & Checkpoint System]].

- [ ] Move it to a root GameObject, or call `transform.SetParent(null)` first

## Open questions

The system exists, but nothing records what is actually localised.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is [[Clippy]]'s voice localised?** *(2026-07-31)* — No. His voice is grunts, so there is nothing to translate.
- **Which languages are supported?** *(2026-07-31)* — Portuguese and English.
- **Is [[Dialogue System]] text localised?** *(2026-07-31)* — Yes. Each line has an ID and the localization system resolves it.
- **Are [[Cutscene System]] subtitles localised?** *(2026-07-31)* — Not needed. The cutscenes contain no dialogue.

## Note on the GDD

The GDD is written in Portuguese and the game's in-engine language is English. If the game ships in both, the design document and the string table will drift apart unless someone owns the mapping.

## Related

[[Save & Checkpoint System]] · [[Accessibility]] · [[Dialogue System]]
