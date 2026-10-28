---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code]
publish: true
---

# Unity Project Conventions

What the project currently does. This is a description, not a standard.

Repo: `github.com/Escarleto/PUC-2-ano-2-Semestre` — a coursework repo, not a dedicated one for this game.

## Layout

```
Assets/Scripts/
  GameManager.cs
  Player/          PlayerData, PlayerMachine, InputReader,
                   HoverboardHandler, PlayerVisualsHandler
  Enemies/         Enemy, Boss, Wanker
  Managers/Game/   SaveManager, LocalizationManager
  Managers/UI/     MainMenuManager
  BossWeakPoint.cs   ← loose at the root
```

## PlayerData as a hub

`PlayerData` is the central object that the movement abilities hang off. This is why abilities chain easily. It is also the file that will become hardest to change as the moveset grows.

## Naming

Scenes are `Terrain`, `FinalBoss`, `SC_Profile`, and a gym or test sandbox. The `SC_` prefix is used on some scenes and not others.

The enemy class is `Wanker` and the GDD calls it Bloatware. See [[Open Issues in the GDD]].

## Things to fix

- [ ] Move `BossWeakPoint.cs` into `Enemies/`
- [ ] Apply the `SC_` scene prefix consistently, or drop it
- [ ] Change the company name away from `DefaultCompany` — see [[Save & Checkpoint System]]
- [ ] Make `DontDestroyOnLoad` managers root objects
- [ ] Strip `Debug.Log` calls before builds. Several were left in `BossWeakPoint` and `Boss`

## Third-party packages

DOTween, Cinemachine, Unity Input System, Unity Localization.

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Save & Checkpoint System]] · [[Movement Feel Philosophy]] · [[Code & Tech MOC]]
