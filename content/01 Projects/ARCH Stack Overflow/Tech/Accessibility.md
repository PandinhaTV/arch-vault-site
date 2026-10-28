---
type: architecture
status: status/active
source: gdd-v1.4
tags: [type/architecture, discipline/code, discipline/design]
publish: true
---

# Accessibility

There is an accessibility section in the pause menu. GDD §2.3.2 lists two options:

- Screen brightness
- Game language

Language is handled by [[Localization]].

## What is there

Having a dedicated accessibility menu at prototype stage is unusual for a student project and worth keeping.

## What is missing

Two options is a small menu, and this game has specific accessibility pressure that nothing currently addresses.

**Motion.** The moveset is fast, and the camera follows a grapple, a pendulum swing and a wall run. That is a strong motion-sickness profile. Motion blur and FOV are in the Graphics menu rather than Accessibility, which is where a player looking for them would check.

**Difficulty.** [[Cache]] has deliberately weak resilience and the design expects skill-based avoidance. There is no assist option of any kind.

**Input.** Answered 2026-08-02: bindings are **not** remappable yet, and the team wants them to be, specifically as an accessibility feature. The plan is to put it in the options menu. This is the single most requested accessibility feature in platformers, so it is the strongest item on this list. See [[Controls]].

Related: the game detects which device is connected but does not swap the button prompts yet, so a controller player still sees keyboard prompts.

**Audio.** No subtitle setting is documented, and [[Clippy]] has voiced dialogue.

- [ ] Move motion blur and FOV into the Accessibility menu, or duplicate them there
- [ ] Decide whether any assist options exist
- [x] Confirm whether controls can be remapped ✅ 2026-08-02
- [ ] Build the rebinding UI in the options menu
- [ ] Swap button prompts to match the connected device
- [ ] Add a subtitle toggle if voice stays

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Can controls be remapped?** *(2026-08-02)* — Not yet. The team wants it and plans to add it in the options menu, as an accessibility feature. → [[Controls]]

## Related

[[Localization]] · [[Controls]] · [[HUD & Menus]]
