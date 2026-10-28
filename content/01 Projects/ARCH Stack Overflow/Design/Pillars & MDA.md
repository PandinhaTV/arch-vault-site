---
type: gdd
project: arch
status: status/active
source: gdd-v1.4
tags: [type/gdd, project/arch, discipline/design]
publish: true
---

# Pillars & MDA

## Concept (§1.1)

A third-person 3D platformer set inside a 2000s corporate computer, in a virtual world built to represent an ideal future. The player is an ordinary Nexus employee who is tired of excessive, monotonous and exploitative work. He sets work aside to find some leisure, and to do that he has to delete documents to make space to download a video game.

## MDA (§1.2)

**Mechanics:** player movement, health, buttons, boost, collectibles
**Dynamics:** high speed, puzzle solving, precision, shortcuts
**Aesthetics:** challenge, exploration, expressiveness

Two problems with this section:

§1.2 lists puzzle solving as a dynamic. §2.1.3 says the game has no puzzles. Both cannot be true. The likely answer is that working out how to reach a place with the moveset is the puzzle, and the GDD should say so.

Health is listed as a mechanic and the GDD never says what damage costs. It now has a note: a battery on Cache's back, 1 to 5, one damage per hit, teleport to the last checkpoint at zero. → [[Health]]

## Features (§1.3)

- Skins — see [[Skins]]
- Interaction between movement and the main character's head — his head is the system cursor. It becomes the hoverboard, and a pointing hand when something is interactable. Settled 2026-07-30, see [[Hoverboard]]
- Satire

## Genre and audience

Genre: 3D platformer, adventure and exploration.

Audience: Explorers and Achievers, using the Bartle test. Explorers are served by the open island world. Achievers are served by the collectible gate on the final level.

## References (§1.6)

[[Super Mario 64]] · [[The Big Catch - Tacklebox]] · [[A Hat in Time]] · [[Bomb Rush Cyberfunk]] · [[Kinito Pet]]

[[FLCL]] is also named, as the visual reference for Cache.

## Scope (§1.9)

⚠ **§1.9 is out of date and needs rewriting for v1.5.** The canonical version is [[Game Structure]].

What §1.9 says: one world containing two levels, aquatic and final; about 5 minutes per level played perfectly and 15 for a first-time player; the game ends when [[Johnny Boss]] is defeated; four NPC types.

What is actually true, as of 2026-08-12:

- The archipelago is **one level** made of **four islands** — Planície, Aquática, Vertical, Final. §1.9.2 already says *"um nível com diferentes fases"*; §1.9.1 contradicts it two lines earlier.
- That level is **one WorkSpace**, a vertical slice sitting mid-game. The full game has several, and the number comes out of the narrative. → [[Narrative Rework]]
- **Johnny Boss ends the WorkSpace, not the game.** §1.9 calls him *"o boss final do nosso jogo"* in the same paragraph it calls this *"o final da demo"*.
- Three islands hold required folders, not two. Every collectible count in the document is built on two.

The timings are the only part still safe to quote.

## Pillars

The GDD does not state design pillars. Without them there is no test for whether a new feature belongs in the game.

These three are drawn from what the document keeps returning to. They are a proposal for the team, not something anyone has agreed:

1. Movement is the content, not the connection between content.
2. The world is worth looking at.
3. Freeing space is freeing yourself.

`source: inferred`

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Game Structure]] · [[Premise & Synopsis]] · [[World Model - Islands & Landmarks]]
