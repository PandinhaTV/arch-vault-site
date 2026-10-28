# arch-vault-site

The published subset of the ARCH: Stack Overflow design vault, built with [Quartz 5](https://quartz.jzhao.xyz) and deployed to GitHub Pages.

**This repo is public. The vault is not.**

## Why the vault is not in this repo

GitHub Pages on the free plan only serves from a public repo. If the vault were this repo, every note would be readable as a raw file — including `Team & Roles`, which carries six people's student numbers, and the skins decisions, which are the team's licensing reasoning. The `publish: true` tag controls which notes become *pages*; it does nothing about the repo being readable.

So the vault stays private, and `export-from-vault.py` copies the published subset here. Nothing unpublished ever leaves the machine.

## Publishing a note

In the vault, add to the note's frontmatter:

```yaml
publish: true
```

That is the only step. Notes are **private by default** — an exclusion list would mean forgetting once is enough to leak something.

## Updating the site

```bash
python export-from-vault.py      # copy published notes from the vault
npx quartz build                 # optional: build locally
npx quartz serve                 # optional: preview at localhost:8080
git add -A && git commit -m "..." && git push
```

The push triggers `.github/workflows/deploy.yml`, which builds and deploys.

By default the script expects the vault at `../Stack Overflow`. Pass a path if it moves:

```bash
python export-from-vault.py "D:/Stack Overflow Obsidian/Stack Overflow"
```

## Three layers stop an unpublished note going live

1. **`export-from-vault.py`** copies only notes with `publish: true`, and **refuses to run** if it finds a student number, the licensed-skin wording, or book-copy provenance in a note marked for publishing — including inside wikilink *titles*, since a link renders its title even when its target is not published.
2. **The GitHub Action** fails the build if any markdown in `content/` lacks the tag.
3. **Quartz's `explicit-publish` plugin** filters again at build time. Verified: a note without the tag emits no page.

Text inside `%%` Obsidian comments `%%` is ignored by the first check, because it never renders.

## The landing page

`content/index.md` is generated from the vault note **`Site Home.md`** — edit it in Obsidian like any other note. The export renames it on the way across.

## Known cosmetic warnings

- *"found invalid date 0"* on the eight teardown notes — their `year:` field is not a date field. Harmless; affects nothing on the page.
- *"Failed to fetch font from Google Fonts"* when building offline. Fine in CI, which has network. Set `fontOrigin: local` in `quartz.config.yaml` to drop the dependency.

## First-time setup

1. Create a **public** repo named `arch-vault-site` under the `PandinhaTV` account and push this folder to `main`.
2. Repo → **Settings → Pages → Source: GitHub Actions**.
3. Confirm the vault repo `ArchObsidian` is **private**.
4. Check `baseUrl` in `quartz.config.yaml` matches the real URL.

Site lands at `https://pandinhatv.github.io/arch-vault-site`.
