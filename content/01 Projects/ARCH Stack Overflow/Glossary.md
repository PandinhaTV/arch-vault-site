---
type: production
project: arch
status: status/active
source: gdd-v1.4
tags: [type/production, project/arch]
publish: true
---

# Glossary

One definition per term, so seven people use the same words. If a term here disagrees with a note, the note is probably right and this needs updating.

## The world

**ARCH** — the operating system built by Nexus. The game takes place inside it. Written in capitals. Full note: [[ARCH (the system)]].

**Nexus** — the corporation that built ARCH. The real antagonist. Never appears as a character. Full note: [[Nexus]].

**WorkSpace** — a level. One branch of the Frutiger family with its own aesthetic, entered from the hub. Clearing one takes Cache to the next folder. How many exist is undecided. → [[Game Structure]]

**Hub** — the separate space where the player chooses a WorkSpace. Not the archipelago, and not designed yet.

**Archipelago** — the open space of a WorkSpace, holding its islands. The GDD calls it *o Mundo*. Full note: [[Archipelago]].

**Island** — an area inside a WorkSpace. This one has four: [[Planície]], [[Aquatic]], [[Clouds]], [[Office]]. Renamed 2026-08-12 — *Clouds* was "Vertical Island", *Office* was "Final Tower".

**Portal** — how the player moves between islands, settled 2026-08-12. Planície leads to Aquatic and Clouds; both lead to Office. → [[Vertical Slice Flow.excalidraw|Vertical Slice Flow]]

**Level** — use it only for a whole WorkSpace. The GDD used it for both a WorkSpace and an island, which is what caused the §1.9.1 / §1.9.2 contradiction. → [[Game Structure]]

**Frutiger Aero** — the visual style of early-2000s operating systems. The game's parent aesthetic. Sub-styles are *Helvetica Aqua Aero* for [[Aquatic]] and *Bright Tertiaires* for [[Office]]. [[Clouds]] has none yet. Full note: [[Art Direction - Frutiger Aero]].

## Characters

**Cache** — the player character. The digital avatar of a Nexus employee. Full note: [[Cache]].

**Bloatware** — the enemy, as a species. Small red spheres created by Nexus to monitor employee efficiency. **Canonical in prose.** Full note: [[Bloatwares]].

**Wanker** — the same creature's character name, used in the concept art and in the Unity class. Not a placeholder. Applies to the small enemies only, not to [[Johnny Boss]]. "SpyWare" in §3.1 is the odd one out and should become Bloatware.

**Peep** — a small helper created by Nexus to maintain the illusion that it supports its workers. Helps Cache anyway. Full note: [[Peeps]].

**Gold Peep** — a [[Peeps|Peep]] painted gold, marking that a secret item is nearby. Confirmed 2026-07-31.

**Clippy** — ARCH's official digital companion. Found in the aquatic level, with dialogue and a voice. Full note: [[Clippy]].

**Johnny Boss** — the boss of this WorkSpace, and the last thing in it. He appears in no other. Called when a defect is found in an employee's behaviour. **This spelling is canonical**, settled 2026-07-30, over "JohnnyBoss", "John Boss" and the older concept-art name "John Wanker". He is not a scaled-up Bloatware. Full note: [[Johnny Boss]].

## Play

**PDF / ZIP** — the collectibles. Corporate files Cache gathers and deletes to free disk space.

**Folder** — the required collectible. One in [[Aquatic]], one in [[Clouds]], one from beating [[Johnny Boss]]. The first two gate the final island.

**Cursor head** — Cache's head is the system mouse cursor. It has three states: his head, the hoverboard he rides on, and a pointing hand shown when something is interactable. Full note: [[Hoverboard]].

**Landmark** — a structure visible from a distance that the player can approach and climb from any direction. ⚠ Under review since portals were settled on 2026-08-12. Full note: [[World Model - Islands & Landmarks]].

**Flow** — the theme of the aquatic island. Continuous movement without stopping. The reason every button in that level can be skipped.

**Kishōtenketsu** — the four-part structure used to divide an island: introduce, develop, twist, conclude. Full note: [[Kishotenketsu Level Structure]].

**Vertical slice** — the current build: one WorkSpace, sitting mid-game. Built so far are [[Aquatic]] and [[Office]]. [[Planície]] and [[Clouds]] are planned. → [[Vertical Slice Flow.excalidraw|Vertical Slice Flow]]

**Playground** — [[Planície]]. An island with no objective, for practising a moveset the player already owns. Not a tutorial.

**Gym** — the Unity test scene. A developer tool, not a place in the game. Not the playground.

## Naming still in dispute

Tracked in [[Open Issues in the GDD]]:

- SpyWare in §3.1 becomes Bloatware. Settled 2026-07-31. Bloatware and `Wanker` coexist, and the class is not renamed — see [[Bloatwares]]

Johnny Boss was settled on 2026-07-30 and is no longer in dispute. §7.3.2 and §4.5 still need correcting in the GDD itself.

## Also worth knowing

**Arch_ Stack Overflow** — the Unity product name, with an underscore because Windows paths cannot contain a colon. The title proper is **ARCH: Stack Overflow**.

## Related

[[ARCH Stack Overflow MOC]] · [[Open Issues in the GDD]]
