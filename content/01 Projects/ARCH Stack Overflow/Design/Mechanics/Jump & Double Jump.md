---
type: mechanic
project: arch
status: status/active
source: gdd-v1.4
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Jump & Double Jump

The base of the moveset. Animations: `Jump`, `DoubleJump`, `Falling`, `Land`, `LedgeGrab`, `LedgeClimb`.

## Gravity

Normal gravity is 0.8× when rising and 1.4× when falling. The player floats slightly at the top of the jump, where they are making decisions, and drops quickly afterwards.

[[Tether Swing]] overrides this to 0.85 and 1.15, because a pendulum with asymmetric gravity loses energy and feels wrong. The controller runs two gravity profiles for two different purposes.

## Ledge grab

Cache catches ledges and climbs them, using `LedgeGrab` and `LedgeClimb`. This turns a near-miss into a success, which matters for a character with weak resilience.

## Open questions

- [ ] Is there coyote time and a jump buffer? Neither is documented. They are the two cheapest improvements available in any platformer.
- [ ] Does double jump reset on wall contact, grapple, or hoverboard?
- [ ] Does jump height vary with how long the button is held?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Wall Run & Wall Jump]] · [[Movement Feel Philosophy]] · [[Cache]]
