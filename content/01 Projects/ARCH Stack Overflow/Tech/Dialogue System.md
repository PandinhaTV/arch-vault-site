---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code, discipline/narrative]
publish: true
---

# Dialogue System

Node-based dialogue with balloons, speakers and triggers. Used by [[Clippy]] and the [[Peeps]].

Every line carries an ID that [[Localization]] resolves, so dialogue is fully localised. Speakers play their own sounds — grunts rather than recorded words. Branching on game state is supported but nothing in the game uses it yet.

## Parts

- Nodes — dialogue content and branching
- Balloons — the display
- Speakers — who is talking
- Triggers — what starts a conversation
- `DialogueManager` — the runtime controller

## Awake and Start ordering

The panel was being hidden immediately after a conversation began.

The cause was that `HidePanelInstant()` was in `DialogueManager.Start()`, while a test call started the conversation from another object's `Awake()`. The hide ran after the conversation opened.

The fix was to move `HidePanelInstant()` into `Awake()`, and keep calls that start conversations in `Start()`.

The general rule: set a component to its default state in `Awake`, and interact with other components in `Start`. Anything that initialises in `Start` can race with objects trying to use it.

## Open questions


## Answered

*Questions that got settled. Keep the answer, not just the tick.*

- **Is dialogue localised through `LocalizationManager`?** *(2026-07-31)* — Yes. Each line has an ID and the localization system resolves it.
- **Is there voice support beyond Clippy's?** *(2026-07-31)* — Yes. Speakers play different sounds.
- **Can dialogue branch on game state?** *(2026-07-31)* — The system supports it. Nothing in the game uses it yet.

## Related

[[Clippy]] · [[Peeps]] · [[Cutscene System]]
