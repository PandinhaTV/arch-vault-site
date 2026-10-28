---
type: pattern
status: status/active
source: inferred
tags: [discipline/code, discipline/design, type/pattern]
publish: true
---

# Movement Feel Philosophy

The wall run, the grapple and the tether swing were written for different purposes, but they use the same four techniques. This note names them so they can be reused.

`source: inferred` — nobody wrote this down. It is a reading of the code.

## 1. Split velocity into meaningful parts, then damp each one

Velocity is never treated as a single vector. It is broken into components that mean something for that ability, and each component gets its own multiplier.

- Grapple: toward the target versus orbiting around it. 50% and 80% on attach.
- Wall run: into the wall versus along it. Into-wall becomes suction, along-wall becomes speed.
- Tether: radial versus tangential. Radial is bled off at 0.33, tangential is kept.

The reason this helps is that "how fast is the player going" is not a question a designer can answer. "How much swing should survive grabbing the rope" is.

## 2. Take exit velocity from what the player saw

- Tether release sets velocity to the measured positional movement of the last frame, so it is exactly tangent to the arc on screen.
- Wall entry takes the fastest speed from the last 0.4 seconds of history, giving back the speed lost decelerating into the wall.
- Wall corners rotate existing velocity around the corner instead of recalculating it.

If the screen showed movement in a direction, the physics honours it, even when the simulation says otherwise.

## 3. Include a small bonus the player is not told about

- Releasing the tether with low vertical speed grants a flat +10 upward, so swing-jumps clear gaps consistently.
- Grapple orbital deceleration ramps to 2000 within 3 units of the target, which works as aim assistance.
- Wall run gravity shrinks as horizontal speed rises.
- Convex wall corners convert turn angle into upward velocity.

## 4. Remove options that let the player make a move feel bad

- Wall jump has a minimum deflect angle of 35 degrees, so the player cannot jump back into the same wall.
- Air control is suppressed for 0.15 seconds after a wall jump.
- Grapple sets `Walkable = 0` after 0.85 seconds so the player cannot catch on a ledge mid-pull.

This is a trade. The player loses a little freedom in exchange for a move that reads clearly every time.

## Gravity is a per-state parameter

The controller runs two gravity profiles. Normal is 0.8 rising and 1.4 falling. Swinging is 0.85 and 1.15, because a pendulum that loses energy feels wrong.

## The cost of point 3, found in playtesting

One tester in [[Playtest 01]] reported the character is too fast to control: *"Falta de controle da velocidade do personagem"*, *"a velocidade do jogador deveria ter um limite"*.

Originally three testers said this, but two were excluded when the responses were filtered, so the evidence is thinner than it first looked. The remaining source is the most experienced movement-game player in the group — Mirror's Edge, Neon White, Penny's Big Breakaway — which is worth something on its own.

Treat as a hypothesis to test, not a confirmed finding.

Each generosity above is small. The wall-entry velocity refund, gravity that shrinks as horizontal speed rises, corner boosts, the tether's flat +10 — they compound, and nothing caps the result.

The lesson generalises: **hidden bonuses need a ceiling.** A system that always gives the player a little more, with no upper bound, eventually gives them more than they can steer.

- [ ] Audit which systems stack, and add a cap

## Using this on the next project

For any new traversal ability, ask:

1. What are the meaningful components of velocity here?
2. What did the player see, and does the exit velocity match it?
3. Where is the hidden bonus?
4. What option should be removed to keep the move clean?

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Grappling Hook]] · [[Wall Run & Wall Jump]] · [[Tether Swing]] · [[Velocity Component Damping]]
