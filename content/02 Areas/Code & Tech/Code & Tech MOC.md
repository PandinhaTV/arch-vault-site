---
type: moc
tags: [type/moc, discipline/code]
publish: true
---

# Code & Tech

Engine and programming knowledge that **outlives any one project**.

This is deliberately small. Most technical notes are about a specific game — its managers, its scene names, its bugs — and those belong in that project's `Tech` folder, not here. Only things that would still be true on a different game in a different engine earn a place in this area.

The test: **would this note still be useful if every current project were cancelled?**

## Notes in this area

```dataview
LIST
FROM "02 Areas/Code & Tech"
WHERE file.name != this.file.name
SORT file.name ASC
```

## Where the project-specific notes went

ARCH's implementation notes are in [[ARCH Stack Overflow MOC|the project]], under `Tech` — save system, localisation, dialogue, cutscenes, zone music, streaming, accessibility, Unity conventions.

Moved there 2026-08-09, because sitting in an Area implied they applied to every project, and they do not.

## Related patterns

Reusable techniques live in `03 Resources/Design Patterns` rather than here, because they are as much design as code:

[[Velocity Component Damping]] · [[Landmark-Driven Open World]] · [[Kishotenketsu Level Structure]]

## Related

[[ARCH Stack Overflow MOC]] · [[Game Design Craft MOC]]
