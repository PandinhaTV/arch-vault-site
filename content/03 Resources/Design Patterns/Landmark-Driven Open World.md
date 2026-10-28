---
type: pattern
status: status/active
source: recovered-from-session
tags: [type/pattern, discipline/design]
publish: true
---

# Landmark-Driven Open World

The Bowser's Fury and Big Catch: Tacklebox model. One continuous space, where the levels are structures the player can see from anywhere and approach from any direction.

## What it needs

**Silhouettes readable at distance.** The core experience is spotting a structure across open ground, heading for it, and only finding out how dense the design is on arrival. Every landmark needs a shape recognisable from far away. Long sightlines are the mechanic, not the scenery.

**Architecture as the challenge.** Avoid complex moving parts. Use geometry placed for the moveset — surfaces to run, points to grapple, gaps to dash.

**Anchors in the space between.** Hook points and launch pads scattered across open ground, so travelling between landmarks is fun rather than dead walking time.

**Height rewarded with information.** Since the player can climb anything at any time, the reward for climbing should be a view that reveals the next landmark.

## What it costs

Much more content per unit of team time than a corridor.

Difficulty cannot be sequenced, because the player chooses the order. Every landmark must be attemptable at base skill.

Gating becomes awkward. Either gate on collectible count, as ARCH does, or accept that the player can reach the finale early.

## Performance

The layout suits streaming, because each landmark is a natural chunk. Load by distance, and use occlusion culling and LODs, since players constantly look at distant structures. A far silhouette can be a cheap LOD swapped for detail on approach.

Use box zones rather than radii, or tall landmarks will unload under a climbing player. See [[World Streaming - Box Zones]].

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[The Big Catch - Tacklebox]] · [[World Model - Islands & Landmarks]] · [[Decision - The world became the main attraction]]
