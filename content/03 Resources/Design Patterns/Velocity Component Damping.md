---
type: pattern
status: status/active
source: inferred
tags: [type/pattern, discipline/code, discipline/design]
publish: true
---

# Velocity Component Damping

A technique for making movement abilities feel authored rather than simulated.

## The idea

Do not treat velocity as one vector. Break it into components that mean something for that ability, then damp each one separately with hand-tuned constants.

## Why it helps

"How fast is the player going" is not a question a designer can tune. "How much of their swing should survive grabbing a rope" is. Decomposing velocity turns a physics quantity into parameters someone can adjust by feel.

## Examples from this project

| Ability | Components | Treatment |
|---|---|---|
| Grapple | toward target / orbital | 50% and 80% on attach; orbital actively decelerated |
| Wall run | into wall / along wall | into-wall becomes suction; along-wall speed is kept |
| Tether swing | radial / tangential | radial bled at 0.33; tangential kept |

## The recipe

1. Name the two or three things velocity means for this ability.
2. Project the vector onto those axes.
3. Give each axis its own multiplier, curve or ramp.
4. Recombine.

Step 3 is where the feel comes from, which is why these constants are never round numbers.

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Movement Feel Philosophy]] · [[Grappling Hook]] · [[Tether Swing]]
