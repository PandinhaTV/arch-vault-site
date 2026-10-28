---
type: project-moc
project: arch
status: status/active
phase: prototype
started: 2026-06
updated: 2026-07-30
source: gdd-v1.4
tags: [type/moc, project/arch]
publish: true
---

# ARCH: Stack Overflow

> A Nexus employee wants to install a game on the work computer. There's no disk space. So he dives into the ARCH operating system as his avatar **Cache**, to delete the corporate PDFs choking it — a small rebellion, dressed as housekeeping.

3D third-person platformer, Unity + C#. Frutiger Aero. Built by Grupo 1 at IPB Mirandela as a cross-unit academic project; the team decided to keep going after the semester.

## Status

- **Phase:** prototype / vertical slice
- **GDD:** working on v1.5 — [[GDD v1.5 EN (working)]] · [[GDD v1.5 PT (working)]]. Submitted version frozen at [[GDD v1.4 - Source Text (PT)]]
- **Playtests done:** 2 — [[Playtest 01]], [[Playtest 02]]
- **Needs attention:** [[Open Issues in the GDD]]

## Design

- **[[Game Structure]]** — the shape of the game. Start here if a note contradicts another one
- [[Glossary]] — canonical names for everything
- [[Lens Reviews Index]] — all 100 design lenses applied to the game
- [[Premise & Synopsis]] — the story, in both languages
- [[Pillars & MDA]] — what the game is *for*
- [[Art Direction - Frutiger Aero]] — the aesthetic and its three sub-styles
- [[Art Asset Library]] — where the source files live

**Narrative** — [[Premise & Synopsis]] · [[ARCH (the system)]] · [[Nexus]] · [[Narrative Rework]]

**Characters** — [[Cache]] · [[Johnny Boss]] · [[Bloatwares]] · [[Peeps]] · [[Clippy]]

**Structure** — [[Game Structure]] · [[Vertical Slice Flow.excalidraw|Vertical Slice Flow]] · [[World Model - Islands & Landmarks]]

**Places** — [[Archipelago]] · [[Planície]] · [[Aquatic]] · [[Clouds]] · [[Office]]

**Interface** — [[HUD & Menus]] · [[Controls]] · [[Audio]]

**Mechanics** — [[Grappling Hook]] · [[Wall Run & Wall Jump]] · [[Tether Swing]] · [[Dash & Attack]] · [[Hoverboard]] · [[Ground Pound]] · [[Jump & Double Jump]] · [[Health]] · [[Boss Fight Structure]] · [[Skins]]

```dataview
LIST
FROM "01 Projects/ARCH Stack Overflow/Design"
WHERE file.name != this.file.name
SORT file.name ASC
```

## Tech

How it is built. Moved into the project 2026-08-09 — these are about ARCH's own systems, not general engine knowledge.

- [[Unity Project Conventions]] · [[Save & Checkpoint System]] · [[Localization]] · [[Accessibility]]
- [[Dialogue System]] · [[Cutscene System]] · [[Zone Music Manager]] · [[Modular Character Creation]] · [[World Streaming - Box Zones]]

```dataview
LIST
FROM "01 Projects/ARCH Stack Overflow/Tech"
WHERE file.name != this.file.name
SORT file.name ASC
```

## Production

- **[[Semester Game Plan]]** — start here this term
- [[Team & Roles]] · [[Prototype Milestone]] · [[Open Issues in the GDD]] · [[Meeting 2026-08-03]] · [[Semester Units 2026-27]]

```dataview
LIST
FROM "01 Projects/ARCH Stack Overflow/Production"
SORT file.mtime DESC
```

## Decisions

```dataview
TABLE WITHOUT ID file.link AS "Decision", date AS "Date"
FROM "01 Projects/ARCH Stack Overflow" AND #type/decision
SORT date DESC
```

## Playtests

```dataview
TABLE WITHOUT ID file.link AS "Session", date AS "Date", build AS "Build"
FROM "01 Projects/ARCH Stack Overflow/Playtests"
SORT date DESC
```

## Open tasks

```dataview
TASK
FROM "01 Projects/ARCH Stack Overflow"
WHERE !completed
GROUP BY file.link
```

## Links

- UI flow whiteboard (Canva): https://canva.link/165vao4rj5s77f5
- Music: Air Runners — *World*, *Water Lvl*, *FinalBoss*
- Save data: `%LOCALAPPDATA%Low/DefaultCompany/Arch_ Stack Overflow/save_slot0.json`

> [!note]- Provenance
> Notes here carry a `source:` field. `gdd-v1.4` = stated in the official GDD. `recovered-from-session` = reconstructed from past Claude conversations, so verify. `inferred` = my reading, not anyone's statement — treat with suspicion.
