---
type: moc
tags: [type/moc]
publish: true
---

# Learning

Books, courses, talks, articles. One note per source, using [[Source Note]].

## Currently working through

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  source-type AS "Type",
  author AS "Author"
FROM #type/source AND !"Templates"
WHERE status = "status/active"
```

## All sources

```dataview
TABLE WITHOUT ID
  file.link AS "Source",
  source-type AS "Type",
  author AS "Author",
  year AS "Year"
FROM "03 Resources/Learning"
WHERE type = "source"
SORT file.mtime DESC
```

## Teardowns

```dataview
TABLE WITHOUT ID
  file.link AS "Game",
  developer AS "Developer",
  year AS "Year"
FROM #type/teardown AND !"Templates"
SORT year DESC
```

## Unapplied
Sources you took notes on but never linked to a project. Not a failure — but worth a glance now and then.

```dataview
LIST
FROM #type/source AND !"Templates"
WHERE length(file.outlinks) < 2
```
