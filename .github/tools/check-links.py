"""Checks that every internal link and #anchor in the playbook still works.

Run it:  python .github/tools/check-links.py

It also runs automatically on every push and pull request. Section numbers are
part of a heading's anchor, so renumbering a section breaks every link to it,
silently. This is what catches that.
"""

import re
import sys
from pathlib import Path


def repo_root():
    """The folder holding .git, so this works wherever the script is kept."""
    for folder in Path(__file__).resolve().parents:
        if (folder / ".git").exists():
            return folder
    raise SystemExit("No .git folder found above this script, so the repository root is unknown.")


ROOT = repo_root()
pages = {f.resolve(): f.read_text(encoding="utf-8")
         for f in ROOT.rglob("*.md") if ".git" not in f.parts}


def headings(text):
    """GitHub turns "## 4. Map risk" into the anchor "#4-map-risk".

    Each space becomes its own hyphen, so "Interface / contract" drops the
    slash and keeps both spaces: "interface--contract".
    """
    found = re.findall(r"^#+\s+(.*)$", text, re.M)
    return {re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", h.strip().lower())) for h in found}


broken = []
for page, text in pages.items():
    for link in re.findall(r"\]\(([^)]+)\)", text):
        if link.startswith(("http", "mailto:")):
            continue
        path, _, anchor = link.partition("#")
        target = (page.parent / path).resolve() if path else page
        if not target.exists():
            broken.append(f"{page.name}  ->  {link}   file not found")
        elif anchor and target in pages and anchor not in headings(pages[target]):
            broken.append(f"{page.name}  ->  {link}   heading not found")

print("\n".join(broken) if broken else "All internal links work.")
print(f"{len(pages)} files checked, {len(broken)} broken.")
sys.exit(1 if broken else 0)
