---
type: character
project: arch
status: status/active
source: gdd-v1.4
tags: [type/character, project/arch, discipline/narrative]
publish: true
---

# Johnny Boss

The final boss. §1.9.3 calls him a kind of bloatware, summoned when a defect is found in an employee's behaviour. That is the GDD's wording for his *role*, not his design — he is not built like one.

![[concept-characters.png]]

The concept art shows him suited and headless. He is not a scaled-up [[Bloatwares|Bloatware]]. Nexus does not send a monster, it sends management.

## Name

**Johnny Boss** is canonical. Settled 2026-07-30.

The GDD spells it three ways: "Johnny Boss" (§1.7, §1.9.3), "JohnnyBoss" (§7.3.2) and "John Boss" (§4.5). §7.3.2 and §4.5 still need correcting — tracked in [[Open Issues in the GDD]].

The concept art originally read "John Wanker" and "The Boss-Man". It has since been changed to Johnny Boss.

A past Claude session invented the name "the Custodian" for this character because `Boss.cs` had no name. That name is not yours and should not be used.

## Where he appears

The final room of [[Office]]. Entering the room starts the fight. Beating him gives the last folder of the vertical slice and unlocks the door.

## Behaviour

From §2.2.7: he has an attack around himself, and he throws himself at the player if the player is far away. Two ranges, two responses.

The implemented state machine is in [[Boss Fight Structure]].

## Open questions

- [ ] What happens to him when he is defeated?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **What is his canonical name?** *(2026-07-30)* — Johnny Boss. The concept art was changed to match.
- **Does he speak?** *(2026-07-30)* — Grunts and exhales, no words.
- **Does he look related to the [[Bloatwares]]?** *(2026-07-30)* — No. Bloatwares are small red spheres. Johnny Boss has no head.

## Related

[[Bloatwares]] · [[Nexus]] · [[Office]] · [[Boss Fight Structure]]
