---
type: mechanic
project: arch
status: status/active
source: recovered-from-session
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Grappling Hook

The main ability of [[Aquatic]], alongside bubble rings and slippery ramps.

## What it is

It is not a physics rope. It is a scripted pull with dampening applied to make it feel right.

## How it works

**On attach.** The player's velocity is split into two parts: the part pointing at the target, and the part orbiting around it. The toward part is kept at 50% and the orbital part at 80%. The player keeps some swing energy, but the pull dominates.

**Each tick.** The toward part accelerates to the grapple point's own speed, following an `AnimationCurve`. Each grapple point has its own acceleration curve and its own minimum and maximum.

The orbital part is actively slowed. The deceleration ramps from 1 to 200 over one second, then up to 2000 once the player is within 3 units of the target.

The result is that the player spirals in wide at first and is pulled straight at the end. It works as aim assistance, but reads as momentum.

**After 0.85 seconds.** `Walkable` is set to 0, so the ground is ignored and the player cannot catch on a ledge during the pull.

**Chaining.** Within 10 units of the target the player can attach to another grapple point immediately, at 0.65× velocity.

**Feedback.** Controller vibration scales with pull speed. The character model rotates around a pivot to lean along the rope, blended in over 0.2 seconds.

## Why the tuning is per-point

Every parameter belongs to the individual grapple point rather than to the system. Level designers can make one anchor slow and floaty over water and another one fast and violent up a tower, without changing any code.

## Tuning values

| Parameter | Value | Effect |
|---|---|---|
| Initial dampening, toward | 0.5 | How much approach speed survives attaching |
| Initial dampening, orbital | 0.8 | How much swing survives attaching |
| Grapple speed and curve | Per point | The main thing designers author |
| Orbital deceleration ramp | 1 → 200 over 1s | Higher is straighter and less swingy |
| Close-range deceleration | 2000 within 3u | Makes the arrival clean |
| Chain window | 10u, ×0.65 | How chainable a route feels |

## Open questions

- [ ] Is there an aim cone or auto-target, and how forgiving is it?
- [ ] Can a pull be cancelled mid-flight?
- [ ] What happens if the anchor is destroyed or streamed out during a pull?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Tether Swing]] · [[Movement Feel Philosophy]] · [[Aquatic]]
