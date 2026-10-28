---
type: pattern
status: status/active
source: books
created: 2026-10-09
tags: [type/pattern, discipline/narrative, discipline/design]
publish: true
---

# How to write a game story

The companion to [[How to write a story]]. That note is craft — want, change, but/therefore. This one is **process**: the order a game story actually gets built in, and what you produce at each step.

Still a method, not a story. Nothing here is about any particular project.

Built from three books, cited per section:

- **Heussner, Finley, Hepler, Lemay — _The Game Narrative Toolbox_, 2nd ed. (2023)** → `TB`
- **Heussner (ed.) — _The Advanced Game Narrative Toolbox_ (2019)** → `ATB`
- **Bateman (ed.) — _Game Writing: Narrative Skills for Videogames_, 2nd ed. (2021)** → `GW`

## The idea everything else hangs off

**Narrative is not story.** `GW` ch. 3, Boon:

> *Narrative is the methods by which the story materials are communicated to the audience. Story refers to all story details and primarily to a set of events as driven by characters within a fictional space.*

The same story can be told through many narratives. This matters because in a game **you give the narrative away to the player and keep the story.** The player chooses where to look, what order to do things in, who to talk to. They almost never choose what happens.

So: *"it is easier to render an interactive narrative than an interactive story"* — `GW` ch. 4, DeMarle. Branching the story is expensive and each branch has to feel genuinely different or the choice was fake. Branching the narrative is nearly free.

`TB` ch. 5 says the same thing from the other side — **the essential two stories**:

| | What it is |
|---|---|
| **World story** | Everything you build to support it. Yours |
| **Player story** | What the player actually experiences through their own actions and imagination. Theirs |

Joined by what the book calls an invisible golden thread. `GW` ch. 4 calls the second one the **immediate-level story** and makes the strongest claim in any of the three books:

> *Because immediate-level stories are so personal, they can be more powerful than any high-level story a writer creates.*

The practical consequence is small and cheap. The player flushes a toilet for fun; in the next apartment someone complains about the water pressure; in the café next morning the waitress complains about getting scalded. The plot did not change. The player now believes they are in the story. **Spend effort there before spending it on branches.**

## The order to work in

`TB` is structured as a process, and the structure is the advice. Each chapter ends in exercises, and the book says that completing them leaves you holding a full set of documentation. Reordered as steps:

| # | Step | What you come out with |
|---|---|---|
| 1 | **Concept** | One-liner, one-page design pitch, one-page narrative pitch |
| 2 | **Worldbuilding** | World Overview Document |
| 3 | **Characters** | A filled character template per character |
| 4 | **Story** | Wireframe, then one plot point expanded into a flow chart |
| 5 | **Implementation** | Who builds what, in what order |
| 6 | **Dialogue / cutscenes** | Scripts, in the format the engine wants |
| 7 | **Troubleshooting** | A revision and testing plan |

Do not skip to 4. Steps 1–3 are what make step 4 writable rather than guessable.

## 1 · Concept — the one-liner

`TB` ch. 2. Before documents, before a world: one line. Two kinds, and you want both.

- **As a description** — what it is, in a sentence that could sit on a store page
- **As a comparison** — *X meets Y*, or *X but Y*. Crude and it works, because it tells a team what to expect in four words

The test `TB` opens the chapter with is the only test: does the listener say *"I'm hooked, I have to see how this turns out"*?

Then two one-pagers — a **game pitch** and a **narrative pitch**. One page each, genuinely. The discipline is the point: if the story needs three pages to be interesting, it is not interesting yet.

`TB` names the next step **kill your darlings** and makes it part of the process rather than an attitude: you write the pitch, you hand it over, you lose things.

## 2 · Worldbuilding — macro then micro

`TB` ch. 3 splits it:

- **Macro** — the big rules. History, power, who decides things, what is physically possible
- **Micro** — what a room smells like, what the sign on the door says, what people eat

Macro first, because micro contradicts itself without it. But macro is also where you can waste a year. **Build only the macro the story touches.** A rule nobody will ever bump into is a hobby.

`ATB` adds two chapters worth of warning here: **research and consultants** (if your world touches a real culture, religion or condition, ask someone who lives it — before building, not after) and its own worldbuilding chapter, *Building A Universe*, on making a world that can take sequels without being retconned.

The output is a **World Overview Document** — one place where anyone on the team can look up the answer, so that two people do not invent two incompatible answers in the same week.

## 3 · Characters — trait first, everything else after

`GW` ch. 6, Walsh, draws a line the other books do not draw as sharply:

- **Traits** are who the character is. Core personality
- **Characteristics** are everything else — gender, race, species, career, looks, age

> *Gender and sexuality are two characteristics most often mistaken for traits.*

The rule: start from the trait, then ask how the characteristic colours the way that trait expresses itself. Define the characteristic first and you get a stereotype, every time, and *"they don't challenge or surprise the player and so will not engage them."*

Also from `GW` ch. 6: if two characters are functionally identical in personality, **cut one or change one.** Two of the same halves the impact of both.

`TB` ch. 4 supplies a long template. The fields that actually do work, when the rest is scaffolding:

| Field                 | Why it earns its place                                                   |
| --------------------- | ------------------------------------------------------------------------ |
| **Governing trait**   | The one word. Everything else is consistent with this                    |
| **Conflicting trait** | A second trait that fights the first. This is where behaviour comes from |
| **Breaking point**    | What finally makes them act. Your plot's trigger, written as character   |
| **Strongest dream**   | The want, from [[How to write a story]], in the character's own terms    |
| **Strongest fear**    | What the story should threaten them with                                 |
| **Dark secret**       | Your reveal, pre-loaded                                                  |

Fill those six for a main character and you have a story's worth of material. Fill the full template for a shopkeeper and you have wasted an afternoon.

## 4 · Story — wireframe linear, branch on the second pass

`TB` ch. 5's exercise is specific and worth following exactly:

1. **Wireframe the high-level core story linearly.** Straight line, no choices, no branches. Just the mandatory beats in order
2. **Second pass: branch.** Now go back and ask where a choice belongs
3. **Then pick one plot point and expand it into a flow chart** documenting the start point, every critical-path quest, every decision and branch point, the ending states, and the optional side content hanging off it

Linear first is not a simplification, it is how you find out whether there is a story at all. A branching diagram drawn first hides the absence of a spine behind complexity.

### The spine and the golden path

`GW` ch. 5, Bateman:

> *The spine of any game consists of events that are absolutely mandatory. If those events do not happen, the story will not progress.*

Side plots and optional activities are by definition not the spine. Which makes the spine the useful thing it is: **the only part of your story you can guarantee every player sees.** Anything you need a player to understand has to be on it, or you are hoping.

### Freedom versus clarity

Same chapter, and it is the trade every game story negotiates:

> *The more the game clarifies its goal by, for example, repeating the required action, the more the player is likely to feel constrained. Conversely, the more the game supports the player's ability to ignore the instructions it provides, the less clear the path of the game becomes.*

There is no solution, only a position. `GW` says each project must have **a policy** — a stated stance on how much the player is expected to follow the path — because without one, each individual decision gets made by whoever is in the room.

The goal to aim at, from the same chapter: deliver what the player needs to know *through the metaphors and devices of the narrative*, with the least obtrusive mechanism available, and no meta-level reference except where it is unavoidable. *"The path of the game should be clearly illuminated, even if the player is not expected or required to follow it."*

## 5 · Implementation — the story is not done when it is written

`TB` ch. 6 and `ATB` ch. 7 (*Get It into the Game*) both exist because this is where game stories die. A story that is not in the build is not a story.

`ATB` ch. 11, **Planning Your Work**, is the chapter to read before promising anything. Narrative work is not estimated like prose work: a line of dialogue costs a line of dialogue, plus recording, plus animation, plus localisation, plus the scene it sits in.

Which leads to the single most useful production fact in the three books, `TB` ch. 9:

> *Writing is often the first thing targeted for change. It is far easier to rewrite the words of a dialogue than to painstakingly reanimate the scene that goes with it.*

**Write the parts that are cheap to change late, and lock the parts that are expensive early.** If you invert that, every schedule problem becomes a story problem.

## 6 · Dialogue and cutscenes

`TB` ch. 7 and 8. The main thing to take from them if you are not writing a dialogue-heavy game: cutscene scripts are written in a format the team can build from — interleaved `START CINEMATIC` / `GAMEPLAY SEQUENCE` / `START CUTSCENE (NONINTERACTIVE)` blocks, so it is unambiguous where control leaves and returns.

The format matters more than the prose. Nobody argues about a line; everybody argues about who is holding the camera.

## 7 · Troubleshooting — plan the revision, not just the draft

`TB` ch. 9 splits feedback into two problems that get confused:

| | The problem |
|---|---|
| **Receiving it** | Emotional. Your work gets torn up in a review |
| **Acting on it** | Technical. Fix the concern without destroying what did work |

> *Rule number one in game development: you can't argue someone out of their reaction.*

A reaction is data. The explanation attached to it usually is not — *"the pacing is off"* is a real feeling and a bad diagnosis. Take the reaction, discard the proposed fix, find the cause yourself.

And the chapter's own framing, which is the honest version of how this goes: **design a testing plan for the story before you need one.** Decide what question you are asking players and what answer would count as a pass, and decide it before you run the test rather than after you see the results.

## The short version

1. One line, two one-pagers. If nobody is hooked, stop
2. Macro world, only as far as the story touches it
3. Traits before characteristics. Six fields, not sixty
4. Linear wireframe. Branch second. Flow-chart one piece
5. Name the spine — it is the only thing every player sees
6. Pick a position on freedom versus clarity and write it down
7. Cheap things late, expensive things early
8. Spend on the player's own story before spending on branches
9. Test with a pass condition decided in advance

## Open questions

- [ ] `TB` assumes a team with a narrative designer role. What of this survives one person doing all of it?
- [ ] Does the two-stories idea have a method attached anywhere, or is it only ever an observation?

## Related

[[How to write a story]] · [[Kishotenketsu Level Structure]] · [[Game Design Craft MOC]] · [[How I take notes from sources]]
