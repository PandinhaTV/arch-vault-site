---
type: teardown
game: The Big Catch - Tacklebox
year: 2024
status: status/active
tags: [type/teardown, discipline/design]
publish: true
---

# The Big Catch: Tacklebox

![](https://cdn.akamai.steamstatic.com/steam/apps/2985610/header.jpg)

**2024 · 3D platformer, free prologue**
[Steam](https://store.steampowered.com/app/2985610/The_Big_Catch_Tacklebox/)

The closest structural reference for [[ARCH Stack Overflow MOC]]. A free prologue to a larger game, and reportedly one of the hardest 3D platformers available.

## What it does

One seamless open space, a desert plateau, with all its levels sitting in it as landmarks the player can approach and climb from any direction. Everything is connected by a movement kit built around a fishing-rod grapple.

## What is worth taking

**Landmarks with distinct silhouettes.** Long sightlines make the world navigable without a map. Directly applicable — see [[World Model - Islands & Landmarks]].

**Architecture as the challenge, not moving parts.** Geometry is cheap. Mechanisms are expensive and break. ARCH already works this way and it is worth defending as scope grows.

**Grapple anchors in open space.** Their grapple flowers and fling orbs make travel between landmarks enjoyable on its own.

**Trigger volumes shaped to the level.** A tower is not a sphere. Already adopted — see [[World Streaming - Box Zones]].

**Safety volumes.** They prevent chunks unloading under the player. ARCH gets this for free from box zones.

## The tether connection

Its grapple is a fishing rod, with rod stress, tugging and line physics. ARCH's [[Tether Swing]] comes from the same lineage, but without the fishing fiction that justifies it.

## What not to take

Tacklebox is deliberately punishing. ARCH's stated audience is Explorers and Achievers, and [[Cache]] is fragile but forgiving. Copying the difficulty would work against the audience.

## Sources

- [PC Gamer](https://www.pcgamer.com/games/action/the-big-catch-tacklebox-is-the-hardest-3d-platformer-ive-ever-played-8-hours-long-and-a-free-to-play-prologue-to-a-bigger-better-game-on-the-way/)
- [CritPoints review](https://critpoints.net/2024/06/27/the-big-catch-tacklebox-review/)
- [Steam](https://store.steampowered.com/app/2985610/The_Big_Catch_Tacklebox/)

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Landmark-Driven Open World]] · [[Tether Swing]]
