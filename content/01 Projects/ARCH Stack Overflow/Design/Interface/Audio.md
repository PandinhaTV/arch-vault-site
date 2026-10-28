---
type: interface
project: arch
status: status/active
source: gdd-v1.4
tags: [type/interface, project/arch, discipline/audio]
publish: true
---

# Audio

GDD §5.3 and §5.4, plus the asset list in §10.1.2 and §10.1.3.

## ⚠ Music is being replaced — 2026-08-03

The team decided to remove the house-made music because it does not fit the game, and to learn to write music closer to the Frutiger Aero style. So the tracks below are on the way out, and "make the loops seamless" is no longer the task. → [[Meeting 2026-08-03]]

## Music

Three tracks, all by Air Runners:

| Track | Where |
|---|---|
| *World* | [[Archipelago]] |
| *Water Lvl* | [[Aquatic]] |
| *FinalBoss* | [[Office]] |

Playback is zone-driven. See [[Zone Music Manager]].

All three loop. The loops are not seamless yet and the team wants them to be (2026-07-31).

## Sound effects

The GDD lists only two, both for Cache: footsteps and stun.

The code has considerably more. `Boss.cs` alone defines telegraph, jump, slam, prone, recover, hurt, phase change and death clips, plus a randomised footstep array with pitch jitter.

So the audio asset list in the GDD is significantly out of date.

- [ ] Rebuild the sound effect list from what is actually in the project

## What is missing entirely

There is no documentation for:

- Ambient audio — none yet, confirmed 2026-07-31. A Frutiger Aero world with water, wind turbines and greenery has an obvious ambient bed, and §10.1.2.1 lists only footsteps
- Interface sounds — §10.1.2.2 is an empty heading
- Voice — §10.1.4 is empty, but the approach is settled: **nobody speaks in words.** [[Clippy]] is grunts (2026-07-31) and [[Johnny Boss]] grunts and exhales (2026-07-30). That means no voice localisation is needed, and the boss wants a vocal effort set rather than dialogue: telegraph, slam, hurt, prone, recover, death. Cutscenes have no dialogue either.
- Ducking when dialogue plays — none yet, confirmed 2026-07-31

## Pitch jitter

The boss plays one-shots with a random pitch offset of up to 0.06, so repeated sounds do not feel looped. Worth applying to Cache's footsteps too if it is not already.

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Zone Music Manager]] · [[HUD & Menus]] · [[Clippy]]
