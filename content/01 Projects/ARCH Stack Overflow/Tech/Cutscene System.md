---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code, discipline/narrative]
publish: true
---

# Cutscene System

Timeline-driven cutscenes using Cinemachine, plus a video player path.

Cutscenes contain no dialogue, so they need no localisation. They are skippable with A on controller or Enter on keyboard.

## The one cutscene

The opening. It introduces the archipelago and establishes the final tower as the landmark that gives the player a destination. Its design is described in [[World Model - Islands & Landmarks]].

## Video player skip

There is a key skip on the video player. The GDD lists control layouts for PlayStation, Steam Deck, Switch, Switch 2 and Xbox, so the skip should work on all of them.

- [ ] Verify the skip works on gamepad.

## Timeline placement

Cutscene timelines are placed per scene rather than centrally. This is fine at the current scale. If the number grows it becomes hard to check whether a timeline still references an object that exists.

## Open questions

- [ ] Is the camera handed back to Cinemachine cleanly afterwards?

- [ ] Is the skip state saved, so a returning player isn't shown the intro again?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Are cutscenes skippable?** *(2026-07-31)* — Yes. A on controller, Enter on keyboard.
- **Are cutscenes localised?** *(2026-07-31)* — Not needed. They contain no dialogue.

## Related

[[Dialogue System]] · [[World Model - Islands & Landmarks]]
