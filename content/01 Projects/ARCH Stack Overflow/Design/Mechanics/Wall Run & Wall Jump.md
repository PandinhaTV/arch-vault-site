---
type: mechanic
project: arch
status: status/active
source: recovered-from-session
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Wall Run & Wall Jump

Implemented in `PlayerMachine.cs`.

## Getting on the wall

A check runs every airborne tick. It raycasts toward the stick input, or toward velocity if there is no input. The surface must be within 20 degrees of vertical. It refuses if the player is moving away from the wall.

There is no button. The player sticks by flying into the wall deliberately.

## Entry

On entering the wall state the code calls `FastestHorizontalVelocityInHistoryRelativeToPlane(wall, 0.4s)`.

The controller keeps a history of recent velocities. On contact it takes the fastest speed from the last 0.4 seconds along the wall plane. This means the speed lost while decelerating into the wall over the last few frames is given back.

Velocity is then projected onto the wall plane and rotated to run along it, keeping its magnitude. Vertical speed is kept at 80% when descending and 65% when ascending.

## While on the wall

Velocity is flattened onto the wall plane each tick and pinned with a constant pull of 1 unit toward the wall.

Gravity along the wall is 0.4×, and it reduces further as horizontal speed increases. At high speed the player barely falls.

Stick input is reduced to three states: along the wall, against it, or neutral. Acceleration is 0.3× and deceleration 0.25×.

`MaintainingWall()` checks with three rays at heights 0.2, 0.5 and 0.8. On curved walls it rotates the player's velocity around the corner. If the wall curves away from the direction of travel, the turn angle is converted into upward velocity, so wrapping a convex wall gives a boost.

## Getting off

Three things end a wall run: the 0.5 second timer expires, the wall is no longer there, or the player is falling faster than 40.

Each one pushes the player away along the wall normal and briefly suppresses air control so they cannot immediately re-attach.

## Wall jump

Full jump height, plus a lateral force away from the wall that scales with speed along the wall — lerped from 13 down to 10 as tangent speed increases.

A minimum deflect angle is then applied. If the resulting trajectory is within 35 degrees of the wall plane, it is rotated outward to at least 35 degrees. The player cannot wall-jump back into the same wall.

Air control is suppressed for 0.15 seconds so the deflection commits.

## What playtesting said

The **single biggest cluster of complaints** in [[Playtest 01]]. Three of the nine counted testers named walls unprompted:

> *"Wall Jumping / Running"* · *"O wall jump deve ser mais responsivo"* · *"pular entre paredes"* / *"Grudar nas paredes"*

It survived the response filtering almost intact, which makes it the most reliable problem in the data.

Every constraint documented above is invisible to the player: the 0.5-second timer, the 20° verticality requirement, the clamp preventing a jump back into the same wall, the refusal to attach when moving away. Each is defensible alone. Together they mean a player who does something reasonable and gets nothing has no way to know why, so it reads as the game not responding.

Also reported, and it is a genuine bug: **double jump does not reset on wall contact.** → [[Jump & Double Jump]]

### What the player needs to know

From the [[Lens Review|Lens 57 review]], 2026-08-09. Three pieces of information, none of which the game currently shows:

- [ ] **Where** the wall is taking them — direction of travel along the surface
- [ ] **How far** it goes — the end of the run, or the next wall, visible before committing
- [ ] **How long** they have — the 0.5-second timer, the most invisible rule in the game

The point of showing these is not to make walls easier. The intended feeling is adrenaline from possible failure, and adrenaline requires the player to believe the failure was theirs. A wall that refuses to grab because of a rule nobody can see reads as the game's fault, which is frustration. Legible rules are what convert the danger into the feeling.

- [ ] Fix double jump reset on wall contact
- [ ] Decide whether climbing needs different feedback from gap-crossing. All of the above assumes horizontal travel; [[Clouds]] teaches wall run for [[Office]]'s vertical interior, where the goal is height.

## Open questions

- [ ] Is the 0.5 second wall-run timer visible to the player? An invisible timer reads as a bug.
- [ ] Nothing teaches wall run today. The plan is [[Clouds]], which is not built. Until it is, the vertical interior of [[Office]] is where players meet wall run for the first time.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is wall run taught anywhere before [[Office]]?** *(2026-07-31)* — Yes. [[Clouds]] is the teaching level for it. Its geometry needs tall flat faces with clear gaps, so the player learns the run-jump-run rhythm rather than fighting the surfaces.

## Related

[[Movement Feel Philosophy]] · [[Jump & Double Jump]] · [[Cache]]
