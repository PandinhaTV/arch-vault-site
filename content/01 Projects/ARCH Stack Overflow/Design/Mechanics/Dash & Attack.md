---
type: mechanic
project: arch
status: status/active
source: recovered-from-session
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Dash & Attack

## Dash

Ground dash and attack dash, both driven through `PlayerData`. It has its own particle effect and animation. It is part of the speed-building toolkit that [[Aquatic]] is built around.

## Attack

From §2.2.7, Cache spins on himself and attacks all around him. Combat is based on movement rather than standing still.

Combat happens between Cache and the [[Bloatwares]] or [[Johnny Boss]]. Bloatwares run at the player and damage on contact. A stun system, `IsStunned`, exists on both sides.

A radial attack means the player does not have to aim, so they do not have to stop moving. A directional attack would work against the rest of the design.

## Gaps

§2.2.7 is three sentences long and nothing else covers this. Undecided or undocumented:

- [ ] Attack cooldown, and whether it can be spammed
- [ ] Whether attacking affects Cache's momentum
- [ ] What taking damage costs — health is listed as a mechanic but never explained. See [[Pillars & MDA]]
- [ ] Whether dash and attack dash are one ability or two

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Ground Pound]] · [[Bloatwares]] · [[Movement Feel Philosophy]]
