---
type: pattern
status: status/active
source: inferred
created: 2026-09-30
tags: [type/pattern, discipline/design, discipline/art]
publish: true
---

# Character Scale in Platformers

Why platformer protagonists are usually short, stubby and big-headed. It is not only a style choice inherited from mascot platformers — four separate constraints push in the same direction.

## The screen is the real constraint

A platformer has to show the player where they are going. Every bit of screen the character occupies is level the player cannot see.

The smaller the character relative to the world, the more of the level fits on screen at a usable camera distance. That is the whole trade, and it is why the character-to-platform ratio gets decided early and then everything else is built against it.

Level design calls this **metrics** — the sense of scale across a whole game, expressed in character-heights rather than metres.

## The character is the ruler

Players judge a gap by how many of themselves fit into it. Nobody counts metres.

So shrinking the character makes the same physical gap read as more dangerous, without building anything bigger. It is free drama: the level feels like an obstacle course rather than a place, at no cost in geometry.

The reverse is also true. A tall character makes a world feel cramped even when it is not.

## Readability during motion

The standard proportions — roughly 2 to 4 heads tall, large eyes, simple shapes, strong colour — exist so the character stays recognisable when small on screen and moving fast.

In a platformer the player is not admiring the character. They are reading, in a fraction of a second: *where am I, which way am I facing, am I rising or falling, am I in a state that changes what my buttons do.* All of that has to come off a silhouette at speed.

Large heads help because the head carries the facing direction and most of the expression.

## Compact shapes collide better

`source: inferred` — this one is reasoning rather than something found written down.

A short, wide capsule catches on fewer ledges, ceilings and corners than a tall thin one. Fewer edge cases to tune, fewer snags, fewer moments where the player feels the geometry rather than the movement.

It is why collision volumes in platformers are usually stubbier than the visible character.

## In 3D, it decides the camera

A tall character forces the camera further back and higher to keep it framed. That flattens the perspective and makes depth — the thing a 3D platformer lives on — harder to judge.

Camera height gets locked early in prototyping precisely because it decides how large the entire world feels. Character height and camera height are one decision, not two.

## The exceptions prove the rule

Mirror's Edge, Prince of Persia, the Star Wars Jedi games — all realistically proportioned, and all solving the same problems a different way: first person, or a tighter camera, or levels built at human scale where doors and railings supply the reference instead of platforms.

Realistic proportions are possible. They just mean giving up the screen-space argument and paying for it elsewhere.

## Open questions

- [ ] Is there a documented ratio designers actually use, or is it always tuned by feel?
- [ ] How do games with a size-changing character handle metrics?

## Related

[[Landmark-Driven Open World]] · [[Kishotenketsu Level Structure]] · [[Game Design Craft MOC]]

## Sources

- [The Anatomy of Platformers, Part 1: Playable Characters](https://thatsallgames.com/2021/07/23/the-anatomy-of-platformers-part-1-playable-characters/) — proportions and readability
- [Level Design Book — Metrics](https://book.leveldesignbook.com/process/blockout/metrics) — scale measured in character units
- [Scroll Back: camera design](https://gamedesignskills.com/game-design/camera-design-2d-side-scroller-games/) — camera height and sense of scale
- [Guide to 3D platformer level design](https://careergamers.com/your-guide-to-3d-platformer-game-level-design/) — camera as the usual failure point

---

> [!info]- Claude's notes — not part of the note above
> Observations only. Nothing here is decided, and none of it belongs to [[ARCH Stack Overflow MOC]] unless you move it there yourself.
>
> **Cache already does the readability thing, unusually.** His head is a system cursor — a large, hard-edged geometric shape on a small body — and it *changes state* to say what is happening: cursor, hoverboard, pointing hand. That is a silhouette doing HUD work. Worth protecting in any redesign.
>
> **The glass problem cuts both ways.** A tester in [[Playtest 02]] said *"é tudo vidro, eu vejo tudo"* and asked for landmarks. A transparent, low-contrast world is also the hardest background to keep a character readable against — the same complaint may apply to Cache, and nobody has tested for it.
>
> **A question you could take to the artist:** how many Caches tall is a standard platform, and how many wide is a standard gap? If nobody has decided, the answer is currently whatever the first prototype happened to be.
