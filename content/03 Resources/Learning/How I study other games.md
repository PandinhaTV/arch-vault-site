---
type: moc
status: status/active
created: 2026-10-20
tags: [type/moc, discipline/design]
publish: true
---

# How I study other games

The companion to [[Reference Game Teardown]], the same way [[How I take notes from sources]] is the companion to [[Source Note]]. The template is the form; this is the method.

Eight teardowns exist in `03 Resources/Reference Games`. Worth saying plainly before the method: **most of them are the course reference sheet retyped.** `hours-played` is blank in all eight, Bomb Rush Cyberfunk says *"placeholder"*, and several are organised around what the sheet records rather than what the game does. That is the same failure the source-note method warns about — a transcript wearing a hat. The method below exists to stop that.

## The one rule

**A teardown is worth writing only if it ends in a mechanism you could build.**

Not an impression. Not a list of features. A mechanism: something specific enough that Lucas could implement it from the sentence, and specific enough to argue about.

| Not usable | Usable |
|---|---|
| Great sense of flow | Landing a trick refills the boost meter, so stopping is the only thing that costs you |
| The hub feels alive | NPCs in the hub comment on the level you just finished, before you reach the next door |
| Good game feel | Coyote time of about 5 frames after leaving a ledge |

If you cannot get to the right-hand column, the note is not finished. It is not a failure — it means you watched a game.

## 1 · Pick the game by the problem

Same as the source method: a weak reason gives you a summary, a strong one gives you an answer.

| Weak reason | Strong reason |
|---|---|
| It's a famous platformer | Why does their big empty space feel intentional and ours feels unfinished? |
| It's the aesthetic we want | How do they make a transparent world readable? |
| It's on the GDD's reference list | Three of our testers said scenery stopped guiding them — what does this game do instead? |

The open problems are already written down — [[Open Issues in the GDD]], the playtest notes, the meeting notes. Start there, not from a list of good games.

## 2 · Play it. Record the hours honestly

The template has an `hours-played` field and it is the credibility of the whole note. A teardown from a trailer, a review, or a course sheet is worth very little, and a note that hides which one it is, is worth less than nothing — because someone will build on it.

If you have not played it, say so in the note and mark it `status/idea`. [[Bomb Rush Cyberfunk]] does this correctly.

## 3 · Three passes, in this order

The order matters, because pass 1 cannot be recovered once you know how the game works.

**Pass 1 — play as a player.** No notes. None. You get exactly one chance to experience the game not knowing how it works, and that is the thing you are actually studying. Write down nothing until you stop.

**Pass 2 — replay the first 15 minutes as a designer.** This is the most transferable part of any game and the template already asks for it. How does it teach? What does it teach first? What does it refuse to explain? Where does it let you fail safely?

**Pass 3 — one system, all the way down.** One. Camera, or the jump, or how collectibles are placed. A teardown that covers everything shallowly is a review.

## 4 · Work backwards through MDA

The course uses MDA, and the project already does — [[Pillars & MDA]]. It is also a diagnostic if you run it in reverse, which is how Schell's lenses work too.

| Step | Question |
|---|---|
| **Aesthetic** | What did I actually feel? |
| **Dynamic** | What behaviour of mine produced that feeling? |
| **Mechanic** | What rule made that behaviour the obvious one? |

Forwards, MDA is a description and produces the kind of bullet list the reference sheets contain. Backwards, it finds the mechanism — because you start from something true (what you felt) rather than from something stated.

## 5 · Borrow a lens

You own a book of a hundred questions. Pick the lens that matches the problem from step 1 and hold it against *their* game instead of ours. → [[Lens Reviews Index]]

It is often easier to see a lens clearly in someone else's game, and the answer usually transfers straight back.

## 6 · Two columns: steal, and don't

The template has both. The second one is the one that gets skipped and the one that saves time.

**Don't steal** is for things that only work because of budget, team size, genre, or audience. Astro Bot's 327 collectible bots work because Sony paid for 327 of them. Journey's score works because a composer was engaged for three years.

Naming these is not pessimism. It stops a plan being built on a cost nobody noticed.

For anything in **steal-worthy**, the template asks *would it work for me?* — answer it with a note or a link, not a yes. An idea with nowhere to go is not an idea yet.

## 7 · The case-study trick

[[The Game Music Toolbox]] is twenty teardowns of game soundtracks, and the thing it does that we do not is **transcribe**. It does not say "the melody develops across the game"; it puts three versions of the Journey theme side by side on one stave.

The equivalent for us is cheap: a screenshot with the camera angle marked, a diagram of a room's sightlines, a timing written in frames. One concrete artefact per teardown beats three paragraphs.

## 8 · How to tell if it worked

Not "is the teardown thorough". The test is the same as for a source note:

**Can you name one thing in ARCH that is different because you played that game?** Link to it. If nothing is different and nothing is queued to change, the verdict is *no*, and that is a real answer — it usually means step 1 was skipped and you picked the game because it was good rather than because it was relevant.

Once in a while, open `03 Resources/Reference Games` and check how many teardowns link into `01 Projects`. The [[Learning MOC]] has an **Unapplied** query that does this for sources; teardowns deserve the same treatment.

## When you're stuck

| Stuck on | Try |
|---|---|
| Can't name what's good about it | Play the worst-reviewed game in the same genre. The contrast names it for you |
| Everything seems worth stealing | You are in pass 1 still. Pick one system |
| It's nothing like our game | Good. Different genre, same problem, is where the non-obvious answers are |
| Can't tell if it's budget or design | Ask what it would cost to do half as much of it. If half is still good, it's design |
| The note won't end | You are writing a review. Delete everything that is not a mechanism |

## Related

[[Reference Game Teardown]] · [[How I take notes from sources]] · [[Reference Shelf]] · [[Game Design Craft MOC]] · [[Pillars & MDA]] · [[Lens Reviews Index]]
