---
type: mechanic
project: arch
status: status/active
source: gdd-v1.4
tags: [type/mechanic, project/arch, discipline/design]
publish: true
---

# Hoverboard

Cache's head is a mouse cursor. The hoverboard is that head: it leaves its position, moves down to his feet, and he rides it. When he stops hovering, it returns to being his head.

So the hoverboard and the "head-float" listed in §1.3 are the same ability, not two.

Implemented as `HoverboardHandler`, with `TryHover()` and `Reset()`. It has its own VFX through `PlayHoverVFX`, and four animations: enter, exit, idle and move. The GDD refers to it as "andar de overboard".

## The head also carries information

When Cache can interact with something, the cursor changes into a small hand with a pointing finger.

That is the interaction prompt, and it is part of the character rather than the HUD. A player who has used a computer already knows what a pointing-hand cursor means, so it needs no tutorial. It is also the clearest expression of the game's premise anywhere in the design — inside an operating system, the player *is* the cursor.

Worth noting it is not listed as a HUD element in §5.1.1, which lists only the taskbar and the low-health screen. See [[HUD & Menus]].

## What §1.3 should say

The GDD lists "interaction between movement and the main character's head" as a headline feature and never explains it. It should say something like:

> Cache's head is the system cursor. It becomes his hoverboard when he rides, and a pointing hand when something can be interacted with.

## Open questions

- [ ] Does the cursor have other states? A loading spinner, a text caret, a "busy" state?
- [ ] Can he be hit while the head is at his feet, and does that read as a vulnerability?
- [ ] Does the head return instantly or animate back?

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is the head-float the hoverboard, or something separate?** *(2026-07-30)* — The same thing. His head is a cursor; it drops to his feet to become the board and returns when he stops.
- **If they are the same, what should the GDD say?** *(2026-07-30)* — §1.3 should describe the cursor head explicitly rather than listing "head" and "hoverboard" as two features.
- **Does the head do anything else?** *(2026-07-30)* — Yes. It becomes a small hand with a pointing finger when Cache can interact with something.

## Related

[[Cache]] · [[HUD & Menus]] · [[Pillars & MDA]] · [[Open Issues in the GDD]]
