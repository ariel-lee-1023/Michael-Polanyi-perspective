#!/usr/bin/env python3
"""Package a skill folder into an installable `.skill` bundle (a zip archive).

Usage:
    python scripts/package_skill.py [path/to/skill-folder] [-o OUTPUT]

Defaults to the repository root and writes `<skill-name>.skill` beside it.
The bundle contains SKILL.md at the top level plus every bundled resource
(references/, scripts/, assets/), and excludes VCS and editor junk.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

EXCLUDE_DIRS = {".git", ".github", "__pycache__", ".venv", "venv", ".idea", ".vscode", "dist", "build"}
EXCLUDE_SUFFIXES = {".skill", ".zip", ".pyc"}
EXCLUDE_NAMES = {".DS_Store", "Thumbs.db", ".gitignore"}


def read_skill_name(skill_md: Path) -> str:
    """Pull `name:` out of the YAML frontmatter, falling back to the folder name."""
    text = skill_md.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            match = re.search(r"^name:\s*(.+)$", text[3:end], flags=re.MULTILINE)
            if match:
                return match.group(1).strip().strip("\"'")
    return skill_md.parent.name


def should_include(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in EXCLUDE_DIRS for part in rel.parts):
        return False
    if path.name in EXCLUDE_NAMES or path.suffix in EXCLUDE_SUFFIXES:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", nargs="?", default=".", help="skill folder (default: current directory)")
    parser.add_argument("-o", "--output", help="output path for the .skill file")
    args = parser.parse_args()

    root = Path(args.folder).resolve()
    skill_md = root / "SKILL.md"
    if not skill_md.is_file():
        print(f"error: no SKILL.md found in {root}", file=sys.stderr)
        return 1

    name = read_skill_name(skill_md)
    output = Path(args.output).resolve() if args.output else root.parent / f"{name}.skill"

    files = sorted(p for p in root.rglob("*") if p.is_file() and should_include(p, root))
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as bundle:
        for path in files:
            bundle.write(path, arcname=str(Path(name) / path.relative_to(root)))

    size_kb = output.stat().st_size / 1024
    print(f"packaged {len(files)} files -> {output} ({size_kb:.1f} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
