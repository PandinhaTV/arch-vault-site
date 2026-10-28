---
type: interface
project: arch
status: status/active
source: gdd-v1.4
tags: [type/interface, project/arch, discipline/design]
publish: true
---

# HUD & Menus

Covers GDD §5.1 and §2.3.

## HUD

Two elements are listed:

- A taskbar
- A low-health screen

The taskbar is the right choice for this game. The player is inside an operating system, so the interface that tells them how they are doing is the same interface the fiction is made of. Nothing has to be explained.

The GDD does not say what the taskbar shows. Likely candidates are collected files, health, and current WorkSpace.

The GDD misses one. Cache's cursor head becomes a pointing hand when something is interactable — that is an interaction prompt, and it is diegetic rather than an overlay. See [[Hoverboard]].

- [ ] Add the cursor states to §5.1.1
- [ ] Document what the taskbar displays
- [ ] Document what the low-health screen looks like and when it triggers

## What playtesting said

[[Playtest 01]], counting 9 of 13 responses: objectives clear **3.7/5**, scenery guides you **4.0/5**, camera helped **3.9/5**.

Better than the unfiltered numbers suggested — one excluded respondent had given all three a 1, which was dragging the camera and scenery figures down on its own. Scenery guidance at 4.0 is a genuine strength for a game with no HUD guidance beyond a taskbar.

Still open: one tester rated the camera 2, and one reported it *"bugava (raramente)"* and getting stuck in places.

## Menus

- Main menu — save slot selection
- Pause menu — options

The pause menu has six sections:

| Section | Contents |
|---|---|
| Video | Screen mode, resolution, FPS, VSync |
| Audio | Master, music, and sound effect volume |
| Gameplay | Mouse sensitivity |
| Graphics | Anti-aliasing, motion blur, FOV |
| Controls | A screen showing the available controls |
| Accessibility | Screen brightness, game language |

That is a complete settings menu for a student prototype, and more than most shipped indie games offer.

## Camera

Third person. GDD §5.1.3.

Implemented with Cinemachine. Nothing else is documented — no note on distance, collision behaviour, or how the camera handles the grapple and tether, which is where most third-person cameras fail.

- [ ] Document camera behaviour during grapple, tether swing and wall run

## Lighting

Unity's sun is used as the lighting model. GDD §5.1.4.

## Interface flow

The menu hierarchy and UI flowchart were planned on the project whiteboard rather than written into the GDD: https://canva.link/165vao4rj5s77f5

That means the flow only exists in Canva. If the link dies or the account closes, the interface design is gone.

- [ ] Export the flowchart and put it in `Attachments`

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Controls]] · [[Accessibility]] · [[ARCH (the system)]]
