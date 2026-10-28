---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, discipline/code]
publish: true
---

# Save & Checkpoint System

`SaveManager` handles slot-based JSON saves. There are also in-level checkpoints.

## Save location

```
%LOCALAPPDATA%Low/DefaultCompany/Arch_ Stack Overflow/save_slot0.json
```

The company name in Unity's player settings is still `DefaultCompany`. It determines the save path, so changing it later will orphan existing saves. Worth fixing before release.

The product name is `Arch_ Stack Overflow`, with an underscore because Windows paths cannot contain a colon.

## Flow

`MainMenuManager.ProfileSelect(int)` → `SaveManager.SelectSlot(int)` → `LoadSlot()`

Writes go through `WriteSave()`. For example `SaveSelectedSkin(int)`, called from `GameManager.ChangeSkin(int)`.

## DontDestroyOnLoad warning

```
DontDestroyOnLoad only works for root GameObjects or components on root GameObjects.
```

This is raised by both `LocalizationManager.Awake()` and `SaveManager.Awake()`. Both managers are nested under a parent object, so `DontDestroyOnLoad` does nothing.

Fix: move both to root-level GameObjects, or call `transform.SetParent(null)` before `DontDestroyOnLoad`.

- [ ] Do this. It is a short fix and the failure mode is confusing.

## Duplicate audio listeners

The logs show "There are 2 audio listeners in the scene", rising to 3. More than one `AudioListener` makes spatial audio undefined. It is usually a persistent camera plus a scene camera.

- [ ] Find and remove the duplicates.

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[Zone Music Manager]] · [[Unity Project Conventions]]
