---
type: gdd
project: arch
status: status/active
source: gdd-v1.4
tags: [type/gdd, project/arch, discipline/design]
publish: true
---

# World Model — Islands & Landmarks

How the player navigates the [[Archipelago]]. The structure it sits inside is in [[Game Structure]]; this note is only about getting around.

⚠ **Under review since 2026-08-12.** Islands are now linked by portals, so the player no longer travels *toward* a landmark to reach it. Everything below was written for a world where they did. It is kept because the ideas still apply inside an island and at the moment of arrival — but the model no longer describes how the WorkSpace is crossed.

## The model

One continuous space where the destinations are landmarks the player can see from a distance and approach from any direction. Bowser's Fury and [[The Big Catch - Tacklebox]] work this way.

The opening cutscene is built for it. The camera takes Cache's viewpoint, shows each island, then moves in on the distant tower and traces the route to it. The player is given control with a destination already in mind. The GDD calls the tower the landmark of the level.

## What the model requires

- Landmarks with silhouettes that can be recognised from far away
- Difficulty built into the shape of structures rather than into moving parts
- Somewhere to go between landmarks, so travelling is not dead time — moot if travel is by portal
- A view from the top of each climb that shows the next landmark

More detail in [[Landmark-Driven Open World]].

## The islands

Four, all present in the opening cutscene:

- [[Planície]] — the playground
- [[Aquatic]] — speed
- [[Clouds]] — climbing
- [[Office]] — the landmark everything points at

The player arrives on Planície and chooses Aquatic or Clouds in either order. Both lead to Office, which is gated on the folders from both.

## Progression gate

The player collects PDFs and ZIPs scattered through the archipelago and the islands, and deletes them. Collecting is the main challenge.

Small NPCs in difficult situations point to secret items. These are optional and ask the player to think past the basic moveset.

⚠ Every collectible count in the GDD assumes two areas hold required folders. It is three. → [[Open Issues in the GDD]]

## Where this note used to be wrong

Until 2026-08-12 this note described the archipelago as the whole game — a semi-open world connecting separate levels, with Planície listed as "no note, no plan."

That reading came from §1.9.1, which says the world unites *os níveis*. §1.9.2, one line later, says the game has *um nível com diferentes fases*. The second is the one that matches the cutscene and the plot points. → [[Game Structure]]

## Technical

Chunks stream by distance using box-shaped zones rather than spheres, because the islands are tall. → [[World Streaming - Box Zones]]

## Open questions

- [ ] Does a summit view still mean anything if the next island is reached by portal rather than by heading toward it?
- [ ] Where do the portals live — on the shore, at the summit, in the middle of Planície? The answer decides whether an island's exit is a reward or a convenience.
- [ ] What is *o Mundo* that §1.9.1 names, and is any of it traversable? → [[Archipelago]]

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Was the Vertical island cut, or does §1.9 undercount?** *(2026-07-31)* — Neither. It was planned and never built. It stays in the cutscene. → [[Clouds]]
- **What is the Planície island?** *(2026-08-12)* — The playground. It is one of the four islands, not an orphan in the cutscene. Inferred from the island list and awaiting team confirmation. → [[Game Structure]]
- **Is the archipelago the game, or part of it?** *(2026-08-12)* — Part of it. It is one WorkSpace, and the WorkSpaces are the levels.
- **How does the player get from island to island?** *(2026-08-12)* — Portals. Which is why this note is under review.

## Related

[[Game Structure]] · [[Archipelago]] · [[Landmark-Driven Open World]] · [[ARCH (the system)]]
