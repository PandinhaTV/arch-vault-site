#!/usr/bin/env python3
"""
export-from-vault.py — copy ONLY published notes from the vault into content/.

    python export-from-vault.py              # vault assumed at ../Stack Overflow
    python export-from-vault.py /path/to/vault

Why this exists
---------------
Quartz's repo is the site repo, and GitHub Pages on the free plan requires that
repo to be public. If the vault itself were the site repo, every note would be
readable as a raw file even though only `publish: true` ones render as pages —
`Team & Roles` has six people's student numbers, and the skins decisions are the
team's licensing reasoning.

So the vault repo stays PRIVATE, and this script copies the published subset into
a separate public repo. Nothing unpublished ever leaves the machine.

It refuses to run if it finds anything sensitive in a note marked for publishing.
That check mirrors the one in the vault's own check-vault.py — keep them in step.
"""
import io, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAULT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "Stack Overflow")
VAULT = os.path.abspath(VAULT)
CONTENT = os.path.join(HERE, "content")

SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", "Templates"}
PUBLISHED = re.compile(r"^publish:\s*true\s*$", re.M)
COMMENT = re.compile(r"%%.*?%%", re.S)

# Must never appear in a published note, nor in a wikilink title inside one.
# Add to this list; never shorten it.
SENSITIVE = [
    (re.compile(r"\ba(?:5|6)[0-9]{4}\b"), "student number"),
    (re.compile(r"(?i)licen[cs]ed skins?|skins? are kept as parody"), "licensed-skin reasoning"),
    (re.compile(r"(?i)not for redistribution|read it by OCR"), "book copy provenance"),
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

found, problems = [], []
for p in notes():
    body = io.open(p, encoding="utf-8", errors="replace").read()
    if not PUBLISHED.search(body):
        continue
    found.append((p, body))
    # Obsidian comments never render, so they are not leaks.
    visible = COMMENT.sub("", body)
    rel = os.path.relpath(p, VAULT).replace(os.sep, "/")
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
print(f"published: {len(found)} notes")

if problems:
    print("\nREFUSING TO EXPORT — sensitive content in published notes:")
    for x in sorted(set(problems)):
        print("  " + x)
    print("\nFix the note, or remove its publish: true, then run again.")
    sys.exit(1)

# Rebuild content/ from scratch so unpublishing a note removes its page.
if os.path.isdir(CONTENT):
    shutil.rmtree(CONTENT)
os.makedirs(CONTENT)

# Quartz takes the site's landing page from content/index.md. The vault keeps it
# as a normal note so it is edited in Obsidian like everything else.
LANDING = "Site Home.md"

attachments = set()
for p, body in found:
    rel = os.path.relpath(p, VAULT)
    if rel == LANDING:
        rel = "index.md"
    dst = os.path.join(CONTENT, rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(p, dst)
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
print("\nnext:  npx quartz build && npx quartz serve   (preview)")
print("       git add -A && git commit && git push     (deploy)")
