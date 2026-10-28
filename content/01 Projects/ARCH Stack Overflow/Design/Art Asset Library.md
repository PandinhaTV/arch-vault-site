---
type: production
project: arch
status: status/active
source: inferred
tags: [type/production, project/arch, discipline/art]
publish: true
---

# Art Asset Library

The source art lives **outside the vault**, at `Art Source`, alongside the vault folder rather than inside it.

759 MB, 733 files. It is out of the vault because Obsidian cannot open `.blend`, `.clip`, `.aseprite` or `.psd`, and because the vault is going into git — binaries that large would dominate every clone for no benefit.

Flattened previews for embedding in notes live in `Attachments/Concept Art`.

## What is in it

**3D with textures** — 234 MB, 50 asset folders. The aquatic level's props and characters: Clippy (three variants, including "Mexican clippy"), Wanker, corals, seaweed, shells, palm trees, plus the office set — keyboard, printer, router, USB, floppy disk, whiteboard, desks, PC tower. 74 `.blend`, 179 `.png`, 54 `.aseprite`.

**ART** — 229 MB. Character art, with `USER Character` and a `referencias` subfolder. 68 `.png`, 28 `.clip`.

**Backgrounds + Level Design** — 116 MB. 32 `.png`, 14 `.clip`.

**Posters** — 79 MB. The poster studies reproduced in GDD §7.1.1.

**3D PART (Cache Textures)** — 64 MB. Cache's textures, plus the only `.fbx` in the library.

**Referencias** — 17 MB, 73 files, with a `Logos` subfolder.

**MoodBoard** — 12 MB, a single `.pur` file (PureRef).

**Logo Arch** — the ARCH logo, including the only `.ai` file.

**Aseprite (Assets 2D)** — 2D assets, with `Thinking` and `UI` subfolders.

**John Boss Texture** — the boss's texture and blend.

## Things worth tidying, when someone has time

**44 `.blend1` files, 71 MB.** These are Blender's automatic backups, regenerated on every save. Safe to delete and safe to exclude from any backup.

**Two reference folders.** `Referencias` at the top level and `ART/referencias` inside. Probably should be one.

**Folder name typos.** `Secreeetaroa` sits next to `Secretaria`; `Lava Lampp++++++`; `PAto`; `Palmier`. Harmless until someone writes a script that walks the folder, or until an asset list needs to match the GDD's §10.1.1.1 list.

**Naming is mixed Portuguese and English.** `Conchas`, `Toalha`, `Ventoinha eolica` alongside `Office Ring`, `White board`, `Carpet`. The GDD's asset list is in Portuguese and the code is in English, so this reflects a real split rather than carelessness — but it makes the asset list hard to cross-check.

## Related

[[Art Direction - Frutiger Aero]] · [[Unity Project Conventions]] · [[Team & Roles]]
