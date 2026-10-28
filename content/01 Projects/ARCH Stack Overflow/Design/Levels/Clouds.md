---
type: area
project: arch
status: status/idea
created: 2026-07-31
source: gdd-v1.4
tags: [type/area, project/arch, discipline/design]
publish: true
---

# Clouds

The climbing island. Confirmed, not yet built. Decided 2026-07-31.

**Renamed from "Vertical Island" on 2026-08-12**, from your flow diagram. The old name described its axis; this one describes the place. → [[Vertical Slice Flow.excalidraw|Vertical Slice Flow]]

It is named in v1.4 §1.7, where the cutscene shows "as ilhas com os níveis (aquático e vertical)", and it appears in the island list in §1.9.1. §1.9 counts only the world, the aquatic and the final — one of several places the GDD uses *nível* two ways. → [[Game Structure]]

The world then became the main attraction and absorbed most of the effort. See [[Decision - The world became the main attraction]].

Status decided 2026-07-31: **planned, not cut.** The cutscene stays as it is, because the island is still coming.

## Purpose

The vertical counterpart to [[Aquatic]], which is about building speed along the ground.

It is also where wall work gets its long run. [[Office]]'s vertical interior assumes the player is fluent with walls, and this is the only place in the WorkSpace that gives them room to become so.

**It does not teach wall run.** That changed on 2026-08-12: this WorkSpace sits mid-game, after every mechanic is unlocked, so nothing here is a first meeting. Teaching happens in an earlier WorkSpace that does not exist yet. What this island does is *re-establish* the move before the tower demands it — which is a different design brief, and a more forgiving one. It can assume competence and build on it rather than starting from zero.

The distinction matters for [[Playtest 01]]. Walls were the biggest complaint, and this island being unbuilt means the tested build had no wall content at all before the tower.

## Placement

- Comes after: [[Archipelago]] — reachable whenever the player chooses it
- Comes before: [[Office]]
- Expected player skill level: comfortable with jump and double jump, new to sustained wall work

The player picks between this and [[Aquatic]] in either order. Neither is a prerequisite for the other. Both feed [[Office]].

## Mechanics used

- [[Wall Run & Wall Jump]] — *re-establish*, at length
- [[Jump & Double Jump]] — *reinforce*
- [[Grappling Hook]] — *reinforce*
- [[Ground Pound]] — *reinforce*

Wall run has a 0.5 second timer and needs a surface within 20 degrees of vertical. Both constraints want geometry built out of tall flat faces with clear gaps between them, so the player learns the rhythm of run, jump, run rather than fighting the geometry.

## Beats

The emotional shape, in order. Same kishōtenketsu split used in [[Aquatic]] — see [[Kishotenketsu Level Structure]].

| # | Beat | Intent | Player feeling |
|---|---|---|---|
| 1 | Ki — the base | Show the summit from the ground | Small, and told where to go |
| 2 | Shō — the ascent | Long wall sections, low cost of failure | Back in the rhythm |
| 3 | Ten — the twist | Change what a wall is for | Caught out, then quick |
| 4 | Ketsu — the summit | Pay off the climb with the view | Earned it |

⚠ The twist is not designed. [[Aquatic]] has the same gap — its twist section is not identified either.

## Layout

Not drawn. When it is, drop the sketch in `Attachments/` and link it here.

## Critical path vs. optional

- Critical: the ascent to the folder at the summit. The folder is required for the progression gate, so this island cannot be skipped.
- Optional / secrets: gold [[Peeps]] mark the secrets, as everywhere else

## Pacing

Tension rises with height, because height is what a fall costs. The release is the summit view.

The landmark model asks that the top of each climb reveals the next target. From this summit the player should be able to see the Nexus tower, the same way the aquatic island keeps it on the horizon. See [[Landmark-Driven Open World]].

## Known problems

- The island does not exist yet, and the opening cutscene already promises it.
- [[Planície]] is also unbuilt, though it now has a purpose. → [[Game Structure]]
- Scope. The team is now five and already treats the world as the main attraction. The expensive answer was chosen deliberately on 2026-07-31 — the island is built, not cut.
- It holds a required folder, so the progression gate spans three islands instead of two. Every collectible count in the GDD still assumes two. → [[Game Structure]]

## Technical

Streaming uses box zones rather than spheres, and this is the case they were built for — a sphere measured from a chunk's centre unloads a tall level under a climbing player. The box for this island is tall and thin. See [[World Streaming - Box Zones]].

## Open questions

- [ ] What is the twist section? Still to decide as of 2026-07-31. [[Aquatic]] has the same gap.
- [ ] Which sub-aesthetic? [[Aquatic]] has Helvetica Aqua Aero and [[Office]] has Bright Tertiaires. This has none. → [[Art Direction - Frutiger Aero]]
- [ ] Where in the build order does it sit, now that it is confirmed?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is the Vertical island built, cut, or planned?** *(2026-07-31)* — Planned, and not built. It stays in the cutscene.
- **What is the island for?** *(2026-07-31, revised 2026-08-12)* — Climbing, and re-establishing wall work before [[Office]]. It does not *teach* wall run: this WorkSpace is mid-game and every mechanic is already unlocked. → [[Game Structure]]
- **Is it actually going to be built, or should it be cut from the cutscene?** *(2026-07-31)* — It is going to be built. The cutscene stays.
- **Does it hold a folder needed for the progression gate, or is it optional?** *(2026-07-31)* — It holds a folder, at the top of the climb. So it is on the critical path, not optional.

## Related

[[Game Structure]] · [[World Model - Islands & Landmarks]] · [[Archipelago]] · [[Planície]] · [[Aquatic]] · [[Office]] · [[Wall Run & Wall Jump]]
