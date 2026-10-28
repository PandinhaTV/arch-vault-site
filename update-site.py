#!/usr/bin/env python3
"""
update-site.py — one command to push vault changes to the live site.

    python update-site.py
    python update-site.py -m "added the tutorial note"
    python update-site.py --dry-run
    python update-site.py --serve       # build and preview, no deploy

What it does, stopping at the first failure:
  1. export-from-vault.py   — copy published notes OUT of the repo, inject the password
  2. npx quartz build       — encrypt and render
  3. leak check             — refuse if plaintext from a protected note is in the output
  4. push public/ to the gh-pages branch

Only the BUILT site is published. The notes never enter this repo, because the
markdown is the plaintext Quartz encrypts from.
"""
import argparse, io, json, os, re, shutil, subprocess, sys, tempfile, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "..", ".site-content")
PUBLIC = os.path.join(HERE, "public")
BRANCH = "gh-pages"

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--message")
ap.add_argument("--vault")
ap.add_argument("--dry-run", action="store_true")
ap.add_argument("--serve", action="store_true", help="build and preview locally, do not deploy")
args = ap.parse_args()

IS_WIN = os.name == "nt"

# On Windows, bare `npx` resolves to npx.ps1, which PowerShell refuses to run
# under the default execution policy ("running scripts is disabled on this
# system"). The .cmd wrapper has no such restriction, so call it directly
# rather than asking the user to change a machine-wide security setting.
NPX = "npx.cmd" if IS_WIN else "npx"

def run(cmd, cwd=HERE, **kw):
    return subprocess.run(cmd, cwd=cwd, text=True, **kw)

def ok(cmd, **kw):
    if run(cmd, **kw).returncode != 0:
        sys.exit(f"\nfailed: {' '.join(cmd)}")

# 1 · export -----------------------------------------------------------------
print("1/4  exporting published notes")
cmd = [sys.executable, "export-from-vault.py"] + ([args.vault] if args.vault else [])
if run(cmd).returncode != 0:
    sys.exit("\nExport refused — nothing was built or pushed. Fix the note above.")

# 2 · build ------------------------------------------------------------------
print("\n2/4  building (encrypting protected pages)")
if not os.path.isdir(os.path.join(HERE, "node_modules")):
    sys.exit("node_modules is missing — run:  npm install")
shutil.rmtree(PUBLIC, ignore_errors=True)
if run([NPX, "--yes", "quartz", "build", "-d", CONTENT]).returncode != 0:
    sys.exit(
        "\nBuild failed.\n"
        "If the error mentions esbuild and 'another platform', node_modules was\n"
        "installed on a different OS. Delete it and reinstall here:\n"
        "    rmdir /s /q node_modules   (or: rm -rf node_modules)\n"
        "    npm install\n"
    )

# 3 · leak check -------------------------------------------------------------
# Take real sentences out of each protected note and confirm none survived into
# the built output. This is the check that actually proves the encryption ran —
# an empty build would otherwise look like a pass.
print("\n3/4  leak check")
password = json.load(io.open(os.path.join(HERE, "site-secrets.json"), encoding="utf-8"))["password"]
blob = ""
for root, _, files in os.walk(PUBLIC):
    for f in files:
        if f.endswith((".html", ".json", ".xml")):
            blob += io.open(os.path.join(root, f), encoding="utf-8", errors="replace").read()

if password in blob:
    sys.exit("REFUSING: the password itself is in the built output.")

# Note titles are legitimately visible — they are the URLs. Collect them so a
# phrase that is merely a title is not reported as a leak.
titles = set()
for root, dirs, files in os.walk(CONTENT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if f.endswith(".md"):
            titles.add(os.path.splitext(f)[0].lower())

def is_title(ph):
    p = ph.strip().lower()
    return any(p in t or t in p for t in titles)

leaks, checked = [], 0
for root, dirs, files in os.walk(CONTENT):
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    for f in files:
        if not f.endswith(".md"):
            continue
        src = io.open(os.path.join(root, f), encoding="utf-8", errors="replace").read()
        fm = src.split("\n---", 1)[0] if src.startswith("---") else ""
        if "password:" not in fm:
            continue  # unprotected page (the landing page) — plaintext is intended
        body = src.split("\n---", 1)[-1]
        body = re.sub(r"\[\[[^\]]*\]\]", " ", body)        # drop wikilinks: titles, not prose
        body = re.sub(r"%%.*?%%", " ", body, flags=re.S)   # drop comments: never rendered
        phrases = [p for p in re.findall(r"[A-Za-z][A-Za-z ,'\-]{45,70}", body) if not is_title(p)]
        if not phrases:
            continue
        checked += 1
        for ph in phrases[:8]:
            if ph in blob:
                leaks.append((f, ph.strip()[:60]))
                break

if leaks:
    print("  REFUSING TO DEPLOY — plaintext from protected notes is in the output:")
    for f, ph in leaks[:10]:
        print(f"    {f}: “{ph}…”")
    sys.exit(1)
print(f"  {checked} protected notes checked, no plaintext in the output")

if args.serve:
    print("\npreviewing — Ctrl+C to stop")
    # Quartz 5 has no `serve` subcommand — serving is a flag on `build`.
    run([NPX, "--yes", "quartz", "build", "-d", CONTENT, "--serve"])
    sys.exit(0)

if args.dry_run:
    print("\n--dry-run: built and checked. Nothing deployed.")
    sys.exit(0)

# 4 · deploy the built site to gh-pages --------------------------------------
print(f"\n4/4  publishing public/ to {BRANCH}")
msg = args.message or f"site update {datetime.date.today().isoformat()}"
work = tempfile.mkdtemp()
try:
    if run(["git", "rev-parse", "--verify", f"origin/{BRANCH}"], capture_output=True).returncode == 0:
        ok(["git", "worktree", "add", "-f", work, BRANCH])
    else:
        ok(["git", "worktree", "add", "-f", "--orphan", "-b", BRANCH, work])
    for e in os.listdir(work):
        if e != ".git":
            p = os.path.join(work, e)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    shutil.copytree(PUBLIC, work, dirs_exist_ok=True)
    io.open(os.path.join(work, ".nojekyll"), "w").write("")
    run(["git", "add", "-A"], cwd=work)
    if not run(["git", "status", "--porcelain"], cwd=work, capture_output=True).stdout.strip():
        print("  no change in the built site — nothing to deploy")
    else:
        ok(["git", "commit", "-q", "-m", msg], cwd=work)
        if run(["git", "push", "-u", "origin", BRANCH], cwd=work).returncode != 0:
            sys.exit("\npush failed — the commit is saved on the gh-pages branch; fix the remote and push")
        print("\nDone. GitHub Pages will serve the update in a minute or two.")
finally:
    run(["git", "worktree", "remove", "--force", work], capture_output=True)
