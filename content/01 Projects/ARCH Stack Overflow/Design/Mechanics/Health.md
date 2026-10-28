---
type: mechanic
project: arch
status: status/active
created: 2026-08-12
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Health

Cache carries a battery on his back. It reads 1 to 5.

Every enemy does 1 damage, and the indicator on his back updates. At 0 he is teleported to the last checkpoint.

Your answer, written 2026-08-09. It sat loose in [[Open Issues in the GDD]] until it was given a note on 2026-08-12.

## Why the battery is on his back

The health bar is diegetic — it is on the character, not on the HUD. That fits a game whose main character's head is already a system cursor, and it means the screen stays clear during movement, which is what the game is mostly made of.

The cost is that the player cannot see their own health while running forward. Worth knowing rather than worth fixing; it is a normal trade for a third-person game and the camera sits behind Cache most of the time anyway.

## Healing

Not designed. The team has discussed it and settled nothing.

Open question worth answering before the next playtest: if there is no healing, five hits is the whole run, and the checkpoint becomes the only reset. That may be the right answer for a game about flow — dying is cheap, so a run is short. But it should be a decision rather than an omission.

## Where it sits in the design

§1.2 lists health as a mechanic. Until this note existed, nothing in the GDD said what damage cost or what happened at zero — one of the two contradictions in [[Pillars & MDA]].

Damage comes from [[Bloatwares]] on contact and from [[Johnny Boss]], who has an area attack and a leap. There is a stun system on both sides.

Falling into the void is not damage. It teleports the player to the last checkpoint directly. → [[Save & Checkpoint System]]

## Open questions

- [ ] How does Cache heal, if at all?
- [ ] Does the battery refill at a checkpoint, or carry its state across?
- [ ] Do the [[Time Medals]] interact with damage taken, or only with time?
- [ ] Is 5 the right number? Nothing has tested it.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **What does damage cost, and what happens at zero?** *(2026-08-09)* — A battery on Cache's back, 1 to 5. Each enemy hit takes 1. At 0 he is teleported to the last checkpoint.

## Related

[[Pillars & MDA]] · [[Bloatwares]] · [[Johnny Boss]] · [[Save & Checkpoint System]] · [[HUD & Menus]] · [[Cache]]
