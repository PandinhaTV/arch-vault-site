---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code, discipline/audio]
publish: true
---

# Zone Music Manager

The music track follows the zone the player is in. There are three tracks.

⚠ The tracks are being replaced — the team decided on 2026-08-03 that the house-made music does not fit and wants something closer to Frutiger Aero. The *system* is unaffected; only the assets change. → [[Meeting 2026-08-03]]

| Zone | Track |
|---|---|
| [[Archipelago]] | Air Runners — *World* |
| [[Aquatic]] | Air Runners — *Water Lvl* |
| [[Office]] | Air Runners — *FinalBoss* |

## Why zone-driven

The player chooses their own route through the world, so music cannot follow a linear progression. It has to react to position.

The part to get right is the transition. In a seamless world the player can cross a boundary at speed and cross back immediately. A hard cut will expose that, so crossfade length should be tuned against how fast Cache actually moves.

## Unused hook

`Boss.OnPhaseChanged` fires an `Action<int>` on every phase transition, and nothing subscribes to it. Connecting music to it would give the boss fight escalation for very little work. See [[Boss Fight Structure]].

- [ ] Consider subscribing the music manager to `OnPhaseChanged`.

## Open questions


## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Are the three tracks looped, or do they have intros?** *(2026-07-31)* — Looped. The team wants the loops to be seamless, which they are not yet.
- **Is there ambient audio separate from music?** *(2026-07-31)* — Not yet.
- **Does music duck for dialogue?** *(2026-07-31)* — Not yet.

## Related

[[Save & Checkpoint System]] · [[Boss Fight Structure]]
