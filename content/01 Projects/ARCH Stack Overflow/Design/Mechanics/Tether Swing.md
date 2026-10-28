---
type: mechanic
project: arch
status: status/active
source: recovered-from-session
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Tether Swing

The rope pendulum, separate from [[Grappling Hook]]. Implemented as `ApplyTetherPhysics()`. It is a positional constraint, not a spring.

## How it works

`_swinging` is true when the rope is taut — within 1 unit of full length — and the player is airborne.

While taut, position is corrected directly. The code works out where the player should be on the sphere of radius `_tetherLength`, then applies `position = Lerp(position, constrained, 0.5)` each tick. Half the error is removed per tick, which reads as taut but slightly elastic.

Outward radial velocity is bled off with `Lerp(velocity, ProjectOnPlane(velocity, rope), 0.33)`. This is the pendulum redirect, softened so it is not abrupt.

Swing gravity is a special case: 0.85 rising and 1.15 falling, compared to 0.8 and 1.4 normally. It is close to symmetric, so the swing conserves energy like a real pendulum.

Hanging directly below the anchor with no input, horizontal velocity is multiplied by 0.99 each tick, so the player settles instead of swinging forever.

## Release

In `Untether()`, if the player is swinging:

```csharp
_velocity = GetFrameDelta() / _dtFixed;
```

Launch velocity is the player's actual measured movement over the last frame, so it is exactly tangent to the arc they just watched. The release direction always matches what was on screen.

There is also a hidden bonus: releasing in mid-air with low vertical speed grants a flat +10 upward, which makes swing-jumps clear gaps consistently.

## The rope works both ways

The same code builds up force on the tethered object. Pull force comes from stick input multiplied by 50 when grounded, and from gravity when airborne.

Stress builds a `_tugTimer`. Vibration ramps with it. At 1.0 the object pops. Rod stress, vibration and the bend visuals all read from one `_currentRodStress` value.

While grounded and tethered, `DoWalkMovement` rotates the move direction into the sphere around the anchor, so running at the end of the rope orbits the anchor instead of jittering against the constraint.

## Open questions

The tether comes from fishing — the rod, the tug, the pop. In a game about deleting corporate files there is no stated reason for it to exist. It is the most complex system in the project and the one with the least narrative justification.

- [ ] Give it a reason to exist in the fiction, or fold it into the grapple.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Grappling Hook]] · [[Movement Feel Philosophy]] · [[The Big Catch - Tacklebox]]
