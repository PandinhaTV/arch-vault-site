---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code, discipline/art]
publish: true
---

# Modular Character Creation

The system behind [[Cache]]'s skins.

`GameManager.ChangeSkin(int)` sets the skin. `SaveManager.SaveSelectedSkin(int)` persists it. `PlayerData.Start()` applies it on load.

## Why it is modular

There are around 25 skins sharing one skeleton and one animation set of 30 animations. Duplicating rigs at that count would be unmaintainable.

## The constraint

Every skin has to fit the same silhouette and skeleton. That rules out anything with different proportions, such as a quadruped or a floating shape.

It also means the [[Skins]] IP decision is cheap to act on. Changing which meshes are referenced does not touch the system.

## Open questions


## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **How are skins unlocked in the real build?** *(2026-07-31)* — Through a shop. Still to confirm with the team.
- **Is there a preview UI, and where does it live?** *(2026-07-31)* — There will be one, probably reached by talking to an NPC in game.
- **Are skins purely visual?** *(2026-07-31)* — Yes, always. Nothing about a skin changes the hitbox.

## Related

[[Skins]] · [[Cache]] · [[Save & Checkpoint System]]
