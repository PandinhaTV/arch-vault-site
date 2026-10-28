---
type: gdd
project: arch
status: status/active
created: 2026-08-12
tags: [type/gdd, project/arch, discipline/design]
publish: true
---

# Game Structure

**The canonical shape of the game.** Settled 2026-08-12. Where any other note disagrees with this one, this one is right and the other note is out of date.

## The hierarchy

**ARCH** is the operating system. Cache enters it to delete corporate files and free space.

**The hub** is a separate space. From it the player picks a WorkSpace. It is not one of the WorkSpaces and it is not the archipelago.

**A WorkSpace** is one branch of the Frutiger family, with its own aesthetic. Clearing one takes the player to the next folder — §2.1.4 already says this happens.

**This WorkSpace** is the vertical slice being built. It sits mid-game, after every mechanic is unlocked, so nothing in it teaches a move for the first time. It is an archipelago of four islands.

![[Vertical Slice Flow.excalidraw]]

*Your flow diagram, 12 August 2026. The canonical version of the shape below.*

| Island | Role | Holds a folder | Sub-aesthetic |
|---|---|---|---|
| [[Planície]] | Playground, no objective. Where the player arrives | No | — |
| [[Aquatic]] | Speed | Yes | Helvetica Aqua Aero |
| [[Clouds]] | Climbing | Yes | ⚠ To verify with the artist |
| [[Office]] | Uses everything; [[Johnny Boss]] | Yes, on defeating him | Bright Tertiaires + Corporate |

**Islands connect by portal.** Settled 2026-08-12. The player lands on Planície, and portals lead from it to Aquatic and to Clouds, and from each of those to Office.

⚠ What the [[Archipelago]] is — the GDD's *o Mundo*, holding basic enemies and exploration zones — is an open question. It is not a body of water between the islands; that was my invention and it is retracted. → [[Corrections Log]]

**The gate.** Two folders, one from Aquatic and one from Clouds, open Office. Beating Johnny Boss gives the third and ends the WorkSpace.

**Planície is the entry.** Both routes start there, and it has no gate of its own.

## What this fixes

The GDD uses the word *nível* for two different things, one line apart, and every note downstream picked a meaning at random.

- §1.9.1 — the world exists *"para unir os níveis"*, plural
- §1.9.2 — *"Atualmente o jogo apresenta **um nível** com diferentes fases, sendo elas a fase aquática e a fase final"*, singular

§1.9.2 is the one that matches everything else. The cutscene calls the tower *"o Landmark **do nível**"*, singular, describing the whole archipelago. §3.1.2 plot point 3 is *"explora diferentes WorkSpaces"*, plural, and point 7 has Cache continuing afterwards.

So: **the archipelago is one level. The islands are areas inside it. The WorkSpaces are the levels.**

Note the vocabulary shift this forces. `type: area` is now used for the four islands and the archipelago; `type: level` is reserved for a whole WorkSpace.

## Johnny Boss is not the final boss

He is the boss of this WorkSpace, and he appears only here. Settled 2026-08-12.

§1.9 calls him *"o boss final do nosso jogo"* while the same paragraph calls this *"o final da demo"*. The second is right. The first needs correcting in v1.5. → [[Johnny Boss]]

## How many WorkSpaces

Undecided, and deliberately so. The number comes out of the narrative, which is not written yet. → [[Narrative Rework]]

This is the one number the collectible counts and the ending depend on, so it cannot stay open forever — but it is a narrative decision, not an arithmetic one.

## Planície is the playground

`source: inferred` — **needs confirming with the team.**

The opening cutscene names four islands: Aquática, Vertical, Final, Planície. The team's plan names four areas: aquatic, vertical, final, and a playground with no objective. Three match by name. Planície is the one left, *planície* means flatland, and a flat island with nothing on it is what a practice area looks like.

If that is right, Planície should not be cut — it has a job. → [[Planície]]

## What is still open

- [ ] Confirm Planície is the playground. Your flow diagram puts it first with no gate, which is strong evidence, but nobody has said the word.
- [ ] **What happens to the landmark model now that travel is by portal?** See below.
- [ ] Clouds' sub-aesthetic — to verify with the artist.
- [ ] How many WorkSpaces, once the narrative exists. → [[Narrative Rework]]
- [ ] Does the hub need designing this semester, or can the slice ship without it?
- [ ] Every collectible count in the GDD assumes two areas hold folders. It is three.

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is the hub a separate space, or is the archipelago the hub?** *(2026-08-12)* — Separate. The hub is where you choose a WorkSpace; the archipelago is inside one.
- **Is Johnny Boss the final boss of the game or of the slice?** *(2026-08-12)* — Of the slice. He appears only in this WorkSpace.
- **How many WorkSpaces are there?** *(2026-08-12)* — To be defined by the narrative, which is unwritten.
- **Is the game an archipelago of levels, or one level made of islands?** *(2026-08-12)* — One level made of islands. §1.9.2 said so; the vault had drifted.
- **How does the player get between islands?** *(2026-08-12)* — Portals.
- **What are the islands called?** *(2026-08-12)* — Planície, Aquatic, Clouds, Office. Clouds and Office replace "Vertical Island" and "Final Tower".

## The portal question

Portals settle how travel works. What they leave open is what the **landmark model** is for now.

That model — you see a structure in the distance, you choose it, and going there is itself gameplay — is why the opening cutscene traces a route to the tower and why every summit is meant to reveal the next target. A portal means you arrive at a landmark rather than travelling toward one.

It fits what you wrote for Lens 21 — *"the space of the game is discrete."* Discrete space is easier to build, stream and pace.

- [ ] Does a landmark still do anything if you reach it by portal, or does it become decoration you look at from the island you are on?
- [ ] What is *o Mundo* — the third part §1.9.1 names alongside the aquatic and final levels? Until that is answered, [[Archipelago]] is describing something I guessed at.

## Related

[[Archipelago]] · [[World Model - Islands & Landmarks]] · [[Planície]] · [[Aquatic]] · [[Clouds]] · [[Office]] · [[Premise & Synopsis]] · [[Pillars & MDA]]
