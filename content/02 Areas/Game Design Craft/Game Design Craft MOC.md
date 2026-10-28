---
type: moc
tags: [type/moc, discipline/design]
publish: true
---

# Game Design Craft

Your standing craft area: how *you* design, independent of any one project. Things learned here get reused; things learned in `01 Projects` usually don't.

## What lives here
- Personal design principles and heuristics
- Post-mortems on your own design thinking
- Recurring problems you keep hitting

## Notes in this area

```dataview
LIST
FROM "02 Areas/Game Design Craft"
WHERE file.name != this.file.name
SORT file.mtime DESC
```

## Related
- Patterns and reference: `03 Resources/Design Patterns`
- Engine and architecture: [[Code & Tech MOC]]
- Teardowns: `#type/teardown`
- Everything design-tagged:

```dataview
LIST
FROM #discipline/design AND !"Templates"
LIMIT 20
```
