#!/usr/bin/env python3
"""
export-from-vault.py — copy EVERY note from the vault into content/, encrypted.

    python export-from-vault.py              # vault assumed at ../Stack Overflow
    python export-from-vault.py /path/to/vault

What goes up
------------
Since 26 Nov 2026 the whole vault goes on the site, behind the password (Diogo's
decision — "absolutely everything"). Before that, only `publish: true` notes went.

Left out, always:
  - Templates/, .obsidian/, .trash/  — not content
  - PDFs                              — the books are copyrighted copies
  - any note with `publish: false`    — an explicit opt-out, for later use

Every exported note is encrypted with the site password EXCEPT the landing page
and any note with `protect: false`. Those open notes are readable by anyone, so
the sensitive check below runs on them, and the export refuses if one trips it.

Why this exists
---------------
Quartz's repo is the site repo, and GitHub Pages on the free plan requires that
repo to be public. The vault repo stays PRIVATE, and this script copies the notes
OUT of it into ../.site-content (outside both repos). Only the built, encrypted
site is pushed. The encrypted pages are still public files: someone can download
them and try to guess the password offline. That is why the password is long.

The sensitive list mirrors the one in the vault's check-vault.py — keep them in step.
"""
import io, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SECRETS = os.path.join(HERE, "site-secrets.json")
VAULT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "Stack Overflow")
VAULT = os.path.abspath(VAULT)
CONTENT = os.path.join(HERE, "..", ".site-content")  # OUTSIDE the repo — see README

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "Templates"}
OPTED_OUT = re.compile(r"^publish:\s*false\s*$", re.M)
OPEN = re.compile(r"^protect:\s*false\s*$", re.M)
COMMENT = re.compile(r"%%.*?%%", re.S)

# Quartz takes the site's landing page from content/index.md. The vault keeps it
# as a normal note so it is edited in Obsidian like everything else.
LANDING = "Site Home.md"

# Must never appear in an OPEN (unencrypted) note, nor in a wikilink title inside one.
# Add to this list; never shorten it.
SENSITIVE = [
    (re.compile(r"\ba(?:5|6)[0-9]{4}\b"), "student number"),
    (re.compile(r"(?i)licen[cs]ed skins?|skins? are kept as parody"), "licensed-skin reasoning"),
    (re.compile(r"(?i)\bLeandro\b|\bJo[ãa]o Ribeiro\b"), "former team member"),
    (re.compile(r"(?i)not for redistribution|OCR'?d|read it by OCR"), "book copy provenance"),
]
LINK = re.compile(r"\[\[([^\]|#]*?)(?:#[^\]|]*?)?(?:\|[^\]]*?)?\]\]")

def notes():
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(root, f)

if not os.path.isdir(VAULT):
    sys.exit(f"vault not found: {VAULT}")

found, problems, skipped = [], [], []
for p in notes():
    body = io.open(p, encoding="utf-8", errors="replace").read()
    rel = os.path.relpath(p, VAULT).replace(os.sep, "/")
    if OPTED_OUT.search(body):
        skipped.append(rel)
        continue
    is_open = rel == LANDING or bool(OPEN.search(body))
    found.append((p, body, is_open))
    if not is_open:
        continue  # encrypted — its contents are not public plaintext
    # Obsidian comments never render, so they are not leaks.
    visible = COMMENT.sub("", body)
    for rx, label in SENSITIVE:
        m = rx.search(visible)
        if m:
            problems.append(f"{rel}: {label} — {m.group(0)[:60]}")
    for m in LINK.finditer(visible):
        title = m.group(1).strip().rstrip("\\")
        for rx, label in SENSITIVE:
            if title and rx.search(title):
                problems.append(f"{rel}: {label} in link title — [[{title}]]")

print(f"vault:     {VAULT}")
print(f"exporting: {len(found)} notes ({len(skipped)} opted out with publish: false)")

if problems:
    print("\nREFUSING TO EXPORT — sensitive content in an OPEN (unencrypted) note:")
    for x in sorted(set(problems)):
        print("  " + x)
    print("\nFix the note, or remove its protect: false, then run again.")
    sys.exit(1)

# Rebuild content/ from scratch so deleting a note removes its page.
if os.path.isdir(CONTENT):
    shutil.rmtree(CONTENT)
os.makedirs(CONTENT)

# ---- password injection ---------------------------------------------------
# The password is injected here rather than stored in the vault, because the
# note's markdown is the plaintext Quartz encrypts from — a password living in
# frontmatter would travel with the note into any copy of it.
try:
    password = json.load(io.open(SECRETS, encoding="utf-8"))["password"]
except FileNotFoundError:
    sys.exit(f"missing {os.path.basename(SECRETS)} — copy site-secrets.example.json to it and set a password")
except (KeyError, json.JSONDecodeError) as e:
    sys.exit(f"could not read a password from {os.path.basename(SECRETS)}: {e}")
if "CHANGE-ME" in password:
    sys.exit("site-secrets.json still holds the example password — set a real one")
if len(password) < 16:
    sys.exit("password is under 16 characters. These are public files attackable offline; use a long passphrase")

PUBLISH_LINE = re.compile(r"^publish:.*$", re.M)

def with_frontmatter(body, lines):
    """Add lines to a note's frontmatter, creating the block if there is none.
    Any existing publish: line is replaced — the explicit-publish plugin needs
    publish: true on every page that should render."""
    end = body.find("\n---", 3)
    if not body.startswith("---") or end < 0:
        return "---\n" + "\n".join(lines) + "\n---\n\n" + body
    fm = PUBLISH_LINE.sub("", body[:end]).rstrip("\n")
    return fm + "\n" + "\n".join(lines) + body[end:]

# ---- site tables ------------------------------------------------------------
# Dataview does not run on the site. A Dataview block preceded by a
# `%% site: epics-table ... %%` comment is replaced with a plain markdown table
# built here from the epic notes, so the site shows the same progress Obsidian does.
EPICS_BLOCK = re.compile(r"%% site: epics-table.*?%%\s*```dataview.*?```", re.S)
FM_FIELD = lambda body, k: (re.search(rf"^{k}:[ \t]*(.*?)[ \t]*$", body.split("\n---", 1)[0], re.M) or [None, ""])[1]

def epics_table(folder):
    rows = []
    for f in sorted(os.listdir(folder)):
        if not f.endswith(".md"):
            continue
        b = io.open(os.path.join(folder, f), encoding="utf-8", errors="replace").read()
        if FM_FIELD(b, "type") != "epic":
            continue
        m = re.search(r"^## Stories[ \t]*$(.*?)(?=^## |\Z)", COMMENT.sub("", b), re.M | re.S)
        boxes = re.findall(r"^\s*- \[(.)\]\s*\S", m.group(1), re.M) if m else []
        done = sum(1 for x in boxes if x.lower() == "x")
        pct = f" ({round(100 * done / len(boxes))}%)" if boxes else ""
        rows.append(f"| [[{f[:-3]}]] | {FM_FIELD(b, 'owner') or '—'} | {done} / {len(boxes)}{pct} | {FM_FIELD(b, 'target') or '—'} |")
    head = "| Epic | Owner | Stories done | Target |\n|---|---|---|---|"
    return head + "\n" + "\n".join(rows) + "\n\n*Built at the last site update.*"

attachments = set()
n_protected = 0
for p, body, is_open in found:
    if EPICS_BLOCK.search(body):
        body = EPICS_BLOCK.sub(lambda _: epics_table(os.path.dirname(p)), body)
    rel = os.path.relpath(p, VAULT)
    if rel == LANDING:
        rel = "index.md"
    dst = os.path.join(CONTENT, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if is_open:
        out = with_frontmatter(body, ["publish: true"])
    else:
        # Not unlisted (since 26 Nov 2026): titles are public anyway — they are in
        # each page's HTML and file name — so hiding pages from listings only broke
        # backlinks, folder pages and tag pages. Page contents stay encrypted.
        out = with_frontmatter(body, ["publish: true", f"password: {password}"])
        n_protected += 1
    io.open(dst, "w", encoding="utf-8").write(out)
    # collect attachments these notes embed, so images are not broken
    for m in re.finditer(r"!\[\[([^\]|#]+?)(?:\|[^\]]*?)?\]\]", body):
        attachments.add(m.group(1).strip())

copied_att = 0
if attachments:
    index = {}
    for root, dirs, files in os.walk(os.path.join(VAULT, "Attachments")):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            index.setdefault(f, os.path.join(root, f))
    for name in attachments:
        src = index.get(name)
        if not src or src.lower().endswith(".pdf"):   # never ship book/GDD PDFs
            continue
        rel = os.path.relpath(src, VAULT)
        dst = os.path.join(CONTENT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        copied_att += 1

print(f"copied:    {len(found)} notes, {copied_att} attachments -> content/")
print(f"protected: {n_protected} encrypted, {len(found) - n_protected} open (landing page + any protect: false)")
print("\nNotes written OUTSIDE the repo on purpose — that markdown is the plaintext")
print("Quartz encrypts from. Only the built site is published.")
print("\nnext:  python update-site.py        (build + deploy)")
print("       python update-site.py --serve (preview locally)")
