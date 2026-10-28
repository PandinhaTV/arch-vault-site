---
type: interface
project: arch
status: status/active
source: gdd-v1.4
tags: [type/interface, project/arch, discipline/design]
publish: true
---

# Controls

GDD §5.2. Layouts are documented for six platforms:

- Keyboard
- PlayStation
- Steam Deck
- Switch
- Switch 2
- Xbox

## The problem with how they are stored

Every layout in the GDD is an image with no accompanying text. There is no written table of action-to-button mappings anywhere.

That means the control scheme cannot be searched, diffed between versions, or checked against the actual Input System bindings. If a binding changes in Unity, nothing flags that the document is now wrong.

- [x] Write the mappings out as a table, with one row per action and one column per platform ✅ 2026-08-02

Written 2026-08-02. All six platforms now have a written column. The Steam Deck, Switch and Switch 2 columns are translated from the tested three rather than verified on hardware — see the note under the table.

| Action | PlayStation | Xbox | Steam Deck | Switch | Switch 2 | Keyboard |
| --- | --- | --- | --- | --- | --- | --- |
| Walk | Left stick | Left stick | Left stick | Left stick | Left stick | WASD |
| Look | Right stick | Right stick | Right stick | Right stick | Right stick | Move mouse |
| Jump | X | A | A | B | B | Space |
| Attack | Square | X | X | Y | Y | Left mouse |
| Hook | Triangle | Y | Y | X | X | Right mouse |
| Dash / reel in | R2 | RT | R2 | ZR | ZR | Left Shift |
| Slam / crouch / slide / reel out | L2 | LT | L2 | ZL | ZL | Left Ctrl |
| Zoom in | R1 | RB | R1 | R | R | Scroll up |
| Zoom out | L1 | LB | L1 | L | L | Scroll down |
| Hoverboard | D-pad down | D-pad down | D-pad down | D-pad down | D-pad down | Down arrow |
| Show HUD | D-pad up | D-pad up | D-pad up | D-pad up | D-pad up | Tab |
| Next skin | D-pad right | D-pad right | D-pad right | D-pad right | D-pad right | G |
| Previous skin | D-pad left | D-pad left | D-pad left | D-pad left | D-pad left | F |
| Instant respawn | Select | View | View | − (Minus) | − (Minus) | R |

**How the three new columns were derived.** PlayStation, Xbox and Keyboard are the tested layouts. Steam Deck, Switch and Switch 2 were translated from them by button **position**, not by letter, on 2026-08-02. That matters for Nintendo: their face buttons are mirrored against Xbox, so Xbox A becomes Switch **B** and Xbox X becomes Switch **Y**. Copying the letters across would put jump on the wrong button.

Steam Deck uses the Xbox face layout, so those letters carry over unchanged.

Switch and Switch 2 are identical here. Switch 2 keeps the same face buttons, shoulders and Minus, so the column is duplicated rather than different.

Two things to check against the real bindings:

- The source table said "Right Button" and "Left Button" for dash and slam. That is read here as the **triggers** (R2/RT/ZR and L2/LT/ZL), with the bumpers on zoom. If they are actually the bumpers, the zoom rows swap with these.
- Xbox has no Select button. Instant respawn is on **View** there, and on **Minus** on Switch.



## Actions to cover

From [[Cache]]'s ability list: move, jump, double jump, wall jump, wall run, dash, attack, grappling hook, ground pound, slide, hoverboard, interact, pause.

"Head float" is not a separate action. It is the hoverboard — settled 2026-07-30, see [[Hoverboard]].

## Implementation

Unity Input System, through `InputReader`. Callbacks seen in the logs include `OnHover`, which drives `HoverboardHandler.TryHover()`.

## Open questions

- [ ] Reconcile the table with the action list. Wall run, wall jump, interact and pause have no row, and the table adds skin cycling, instant respawn, show HUD and zoom, which the ability list does not mention.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Are all six platforms actually tested?** *(2026-08-09)* — Three are. PlayStation, Xbox and keyboard are tested. Steam Deck, Switch and Switch 2 are derived from those by button position rather than by letter, because Nintendo's face buttons are mirrored against Xbox — Xbox A is Switch B, Xbox X is Switch Y. Switch and Switch 2 are identical. The team is ready to build for those devices but has not verified the mappings on hardware.
- **Do dash and slam sit on the triggers or the bumpers?** *(2026-08-09)* — Triggers.

- **Are bindings rebindable?** *(2026-08-02)* — Not yet. The team wants them rebindable because it matters as an accessibility feature, and the plan is to put it in the options menu. → [[Accessibility]]
- **Does the game detect the connected device and swap prompts automatically?** *(2026-08-02)* — It detects which device is in use, but it does not swap the prompts yet.

They are just - we are ready to make them to those devices 
the dash and slam are on triggers 

## Related

[[HUD & Menus]] · [[Accessibility]] · [[Cache]]
