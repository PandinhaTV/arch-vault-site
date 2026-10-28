---
type: mechanic
project: arch
status: status/active
source: recovered-from-session
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Boss Fight Structure

The implemented state machine for [[Johnny Boss]], from `Boss.cs`.

## The loop

![[diagram-boss-loop.svg]]

**Chase.** The boss walks straight at the player until he is within leap range.

**Attack.** The attack is chosen by distance. Closer than `closeRange`, which is 4 units, he ground punches with an area effect centred on himself. Otherwise he leaps onto the player's position.

**Telegraph.** A ring indicator appears at the target point and scales up over the telegraph duration, so the wind-up time is drawn on the floor.

**Vulnerable.** The prone animation plays and the back weak point becomes damageable. This is the only time the boss can be hurt.

**Recover.** He stands up, pauses briefly, and the loop restarts.

## Phases

Three phases, based on health thirds. Each phase retunes the timings rather than adding new attacks, so the player does not have to relearn anything.

| Phase | Telegraph | Vulnerable | Other changes |
|---|---|---|---|
| 1 | 1.2s | 2.5s | — |
| 2 | 0.9s | 1.8s | Slam radius 4.5 |
| 3 | 0.6s | 1.3s | Slam radius 5, move speed 5.5 |

Health is 9, so three stomps per phase.

## Damage

The player damages the boss by ground pounding the back weak point during the vulnerable window. `BossWeakPoint` calls the inherited `Hit()`.

## Do not reshape the collider

The vulnerable state originally reshaped the boss's capsule into a lying pose. Reshaping a `CapsuleCollider` on this dynamic Rigidbody at runtime produces a NaN, and Unity resets the body to (0,0,0). The boss teleported to the world origin every time. Making the body kinematic during the reshape did not fix it.

The reshape was removed and the weak point moved to the top of the standing capsule. If the lying hitbox is wanted later, use a separate child collider enabled only during the vulnerable state.

Full reasoning in [[Decision - No runtime collider reshape on the boss]].

## Ground mask

The leap's `GroundUnder` raycast needs `groundMask` set to the ground layer only. With "Everything" the ray hits the player, and the boss lands on their head, floating and overlapping.

## Open questions

- [ ] What happens when Cache dies during the fight?
- [ ] Does the arena have traversal features, or is it flat?
- [ ] `OnPhaseChanged` exists and nothing subscribes to it. Music could use it. See [[Zone Music Manager]].

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Johnny Boss]] · [[Office]] · [[Ground Pound]]
