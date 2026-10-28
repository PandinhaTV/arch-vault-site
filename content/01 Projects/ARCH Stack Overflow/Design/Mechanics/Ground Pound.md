---
type: mechanic
project: arch
status: status/active
source: gdd-v1.4
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Ground Pound

Also called stomp or slam. Animations: `SlamFall` and `Slam`.

## Uses

Pressing floor buttons in [[Aquatic]].

Damaging [[Johnny Boss]] during his vulnerable window. See [[Boss Fight Structure]].

## Effect on level design

Ground pound is the one ability that requires the player to stop. In a level themed on flow that is a problem.

The team handled it by making every button bypassable, so a player who knows the route never has to stop. See [[Decision - Buttons can be skipped to preserve flow]].

## Note on the boss

The boss's vulnerable window originally reshaped his collider into a lying pose so the player could stomp his back. That reshape corrupted the Rigidbody and teleported the boss to the world origin, so it was removed. The weak point now sits on top of the standing capsule. See [[Decision - No runtime collider reshape on the boss]].

## The first button confused people

In [[Playtest 01]] one tester got lost at *"o primeiro botão"*, and another wrote *"fiquei um pouco confusa para saber como funciona o botão e a bola azul"*. Both survived the response filtering.

The ground-pound button gate is the first thing in the game that stops a player, and nothing teaches it. Cheap to fix — and it matters more than it looks, because a player who never learns ground pound cannot use the expert route either. → [[Decision - Buttons can be skipped to preserve flow]]

- [ ] Teach the button, or move the first one later

## Open questions

- [ ] Does ground pound keep or kill horizontal momentum on landing?
- [ ] Is there a minimum height, or can it be used as an instant ground snap?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Dash & Attack]] · [[Boss Fight Structure]] · [[Aquatic]]
