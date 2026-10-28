---
type: source
source-type: book
author: Michael Sweet
year: 2014
status: status/active
created: 2026-10-15
tags: [type/source, discipline/audio, discipline/design]
publish: true
---
%% The PDF is a scan with no text layer — searching it in Obsidian will find nothing.
   I read it by OCR. Page numbers below are approximate for that reason. %%

# Writing Interactive Music for Video Games

**Addison-Wesley · 641 pages · 30 chapters in five parts · Berklee professor, foreword-level endorsements from Sony and GameSoundCon**

**Link:** `Attachments/Documents/Books/577407865-Writing-Interactive-Music-for-Video-Games.pdf` — in the vault, out of git
**Finished:** [ ] — structure and the two core technique chapters. Not read through

⚠ **This PDF is a scan.** No text layer, so Obsidian search will not find anything inside it.

---

## 1 · Before — the question

The GDD says the music should respond to play. What does that actually mean in practice, and is it something two people can build?

---

## 2 · While — where, not what

| Where | Reaction |
|---|---|
| ch. 8 | horizontal resequencing — the name for it |
| ch. 9 | vertical remixing — the other half |
| ch. 10 | transition matrix |
| ch. 6 | Terry Riley, *In C*, 1964 |
| ch. 16–17 | aleatoric and generative |
| ch. 12 | music as a gameplay element |
| parts IV–V | 11 chapters on contracts and bidding |

---

## 3 · After — close it, then write

### Claims worth keeping

- **There are two core techniques and everything else is a variation.** *Horizontal resequencing* — changing what plays next (crossfading, transitional and branching scores). *Vertical remixing* — changing what plays at the same time, by muting and unmuting layers. Having the names makes the whole subject tractable
- **Vertical remixing is the one worth building first.** Write the layers to be non-synchronised and individually controllable, and intensity becomes a dial. The hard part is the fade times, which get their own section
- **Transitions are a design problem with their own vocabulary** — transition matrices, synchronised versus non-synchronised, stingers, and what to do about rubato passages with no clear beat. Getting from cue A to cue B is harder than either cue
- **Interactive music is older than games.** Bach's *Art of Fugue*, Duchamp 1913, Cage, Stockhausen, Terry Riley's *In C* (1964) — a whole chapter of precedent. Useful for the report, and it reframes generative music as a century-old practice rather than a software trick
- **Chapters 16 and 17 are aleatoric and algorithmic composition** — rule sets, mapping gameplay inputs to musical parameters, generating melody and harmony from constraints. This is the part closest to what Strudel already does

### Quotes

None worth keeping — I OCR'd this book rather than read it properly, and quoting from OCR output risks quoting the OCR rather than the author.

### Disagreements

- **A third of it is a careers book.** Parts IV and V are eleven chapters on contracts, estimates, bidding psychology, negotiation tactics, taxes and legal fees. Written for someone going freelance in 2014 — nothing to do with us
- **It assumes middleware.** Wwise or FMOD, a DAW, and a programmer to wire it up. Chapters 18 and 19 are about middleware engines and building a custom music solution. We have Unity, Strudel and no audio programmer
- **It is from 2014**, which in game audio is a long time. The history chapter ends at 2013 and the middleware landscape has moved
- The scan is a real problem. No text layer means it cannot be searched or quoted from reliably, and the OCR mangles headings badly enough that I may have mis-titled a section or two above

### Apply to

- [ ] **Build the aquatic music as vertical layers rather than one track**, so intensity can follow the player instead of looping regardless. This is the cheapest version of what §5.3 already promises → [[Audio]]
- [ ] Nothing from parts IV and V. Ever

### Follow-ups

- Terry Riley, *In C* (1964) — the clearest ancestor of what Strudel does
- Appendix C, *Game Music Canon*, 1970–2013 — a listening list
- Wwise and FMOD, if we ever get an audio programmer
- Karlheinz Stockhausen, *Klavierstücke XI* (1956) — score as a set of options

---

## Verdict

- Partly, and honestly: I took the vocabulary and left the book. *Horizontal resequencing* and *vertical remixing* are the two terms I was missing, and one of them is buildable by us. The rest is for a professional composer with middleware and a lawyer. Worth keeping on the shelf, not worth reading through

---

%% No transcript. %%
