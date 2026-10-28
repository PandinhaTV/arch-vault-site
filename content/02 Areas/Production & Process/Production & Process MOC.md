---
type: moc
tags: [type/moc, discipline/production]
publish: true
---

# Production & Process

How the work gets done: planning, scope control, tools, routines. Process notes belong here rather than inside a project, because they outlive the project.

## Notes in this area

```dataview
LIST
FROM "02 Areas/Production & Process"
WHERE file.name != this.file.name
SORT file.mtime DESC
```

## Current milestones

```dataview
TABLE WITHOUT ID
  file.link AS "Milestone",
  project AS "Project",
  due AS "Due",
  status AS "Status"
FROM #type/milestone AND !"Templates"
WHERE status != "status/done"
SORT due ASC
```

## Recent sprints

```dataview
TABLE WITHOUT ID
  file.link AS "Sprint",
  project AS "Project",
  start AS "Start"
FROM #type/sprint AND !"Templates"
SORT start DESC
LIMIT 6
```

## Open bugs by severity

```dataview
TABLE WITHOUT ID
  file.link AS "Bug",
  severity AS "Severity",
  project AS "Project"
FROM #type/bug AND !"Templates"
WHERE status != "status/done"
SORT severity ASC
```
