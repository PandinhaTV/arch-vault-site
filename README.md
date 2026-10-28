# arch-vault-site

The ARCH: Stack Overflow design vault, published as a **password-protected** site with [Quartz 5](https://quartz.jzhao.xyz).

**This repo is public. It contains no notes.** Only the build config and scripts.

## How the protection works

Pages are encrypted at build time with **AES-256-GCM** (600,000 PBKDF2 iterations) and decrypted in the browser. One password covers the site; entering it on any page unlocks the rest for that browser session.

Protected pages are also `unlisted`, so they do not appear in search, the graph, the explorer, RSS or the sitemap, and their metadata is encrypted separately. The search index drops from 82 entries to 4.

### Why the notes are not in this repo

Encryption happens at build time **from the markdown**. If the markdown were committed here, the plaintext would sit in a public repo next to the ciphertext and the password would be decorative.

So `export-from-vault.py` writes the notes to **`../.site-content`, outside this repo**, and only the built site is published. They cannot be gitignored instead — Quartz respects `.gitignore` and would skip them, producing an empty site that looks like a successful build.

### Where the password lives

In `site-secrets.json`, which is gitignored. The export injects it into each note's frontmatter on the way out, so it never exists in the vault or in any repo. To rotate it: change that file, run `update-site.py`, and everything is re-encrypted.

Copy `site-secrets.example.json` to `site-secrets.json` to start. The export refuses to run on the example password or anything under 16 characters.

## What is still visible without the password

Be clear-eyed about this:

- **Page titles and URLs.** `/design/characters/johnny-boss` tells a visitor that a character called Johnny Boss exists. Unavoidable — the file name is the URL.
- **The landing page**, deliberately. It carries `protect: false` and says only what the project is and that a password is needed. **Do not add link tables or a contents list to it** — that would publish the whole structure of the game by name, which is what the password is for.
- **Page count and folder shape**, inferable from URLs.

What is *not* visible: all body text, every heading, tags, descriptions, and the search index.

## Notes that are never published at all

Encryption is good enough for internal material whose exposure would be embarrassing. It is not good enough for other people's personal data, because the ciphertext is public, permanently downloadable and attackable offline forever.

So these stay off the site entirely, password or not:

- `Team & Roles` — six people's student numbers
- `Mechanics/Skins` and the two licensed-skin decisions — a licensing argument, not a privacy one
- The three Lens Review notes — they reproduce the question sets of a commercial book

## Daily use

```bash
python update-site.py                 # export, build, check, deploy
python update-site.py --serve         # preview locally instead
python update-site.py --dry-run       # build and check, deploy nothing
python update-site.py -m "message"    # custom commit message
```

Publishing a note: add `publish: true` to its frontmatter in the vault. Add `protect: false` as well to leave it unencrypted. Notes are private by default and protected by default.

## Three guards

1. **`export-from-vault.py`** copies only `publish: true` notes, and refuses on student numbers, licensed-skin wording or book provenance — including inside wikilink *titles*, since a link renders its title even when its target is private.
2. **Quartz's `explicit-publish` filter** drops anything untagged that somehow reaches `../.site-content`. Verified: an untagged note emits no page.
3. **The leak check in `update-site.py`** pulls real sentences out of every protected note and refuses to deploy if any survived into the built output. It ignores note titles (legitimately public) and `%%` comments (never rendered).

That third check earned its place. It caught two real leaks during setup that the design had missed:

- **The table of contents rendered outside the encrypted block**, publishing every heading of every protected page — including `johnny-boss-is-not-the-final-boss` and `planície-is-the-playground`. The ToC plugin is now disabled, which is the cost of this approach.
- **Tags were linked** on protected pages. Removed from the properties panel.

It has also been proven to fail: re-enable the ToC plugin and the check blocks the deploy.

## Config choices worth knowing

| | |
|---|---|
| `table-of-contents` | **disabled** — leaked headings |
| `note-properties` | `tags` removed from `includedProperties` |
| `encrypted-pages` | `unlistWhenEncrypted: true` |
| `analytics` | `null` — no third-party tracking on team documentation |

## First-time setup

1. `cp site-secrets.example.json site-secrets.json` and set a long passphrase. Share it with the team somewhere that is not this repo.
2. Create a **public** repo `arch-vault-site` under `PandinhaTV`, then:
   ```bash
   git remote add origin https://github.com/PandinhaTV/arch-vault-site.git
   git push -u origin main
   ```
3. `python update-site.py` — creates and pushes the `gh-pages` branch.
4. Repo → **Settings → Pages → Source: Deploy from a branch → `gh-pages` / root**.
5. Check `baseUrl` in `quartz.config.yaml` matches the real URL.

Lands at `https://pandinhatv.github.io/arch-vault-site`.

## Known cosmetic warnings

- *"found invalid date 0"* on the eight teardown notes — their `year:` field is not a date. Harmless.
- *"Failed to fetch font from Google Fonts"* when offline. Set `fontOrigin: local` in `quartz.config.yaml` to drop the dependency.
