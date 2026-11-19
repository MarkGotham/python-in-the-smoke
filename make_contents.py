#!/usr/bin/env python3
"""
generate_notebooks_table.py

- Finds all .ipynb files,
- Groups by directory,
- Prints a markdown table
"""

from pathlib import Path
import json
from collections import defaultdict

USER = "MarkGotham"
REPO = "python-in-the-smoke"
COLAB_BASE = f"https://colab.research.google.com/github/{USER}/{REPO}/blob/main/"
SKIP = {"smoke_test.ipynb"}


def notebook_title(nb_path: Path) -> str:
    """Extract title from first markdown-cell heading; fall back to filename."""
    try:
        with open(nb_path) as f:
            nb = json.load(f)
        for cell in nb.get("cells", []):
            if cell.get("cell_type") == "markdown":
                for line in "".join(cell.get("source", [])).splitlines():
                    line = line.strip()
                    if line.startswith("#"):
                        return line.lstrip("#").strip()
    except (json.JSONDecodeError, OSError):
        pass
    return nb_path.stem.replace("_", " ")


def label_for(nb_path: Path) -> str:
    """
    For cases with alphabetic prefix, like 'a_getting_started', insert the colon.
    Else just the name.
    Placeholder in case of further dev.
    """
    stem = nb_path.stem
    if stem and stem[0].isalpha() and len(stem) > 1 and stem[1] == "_":
        return f"{stem[0]}: {stem[1:].replace('_', ' ')}"
    return stem.replace("_", " ")


def make_row(nb: Path, root: Path, topic = False) -> str:
    """Topic is a placeholder in case we want to use title."""
    rel = nb.relative_to(root).as_posix()
    label = label_for(nb)
    download = f'<a href="./{rel}" download>Download</a>'
    colab = (
        "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
        f"({COLAB_BASE}{rel})"
    )
    if topic:
        topics = notebook_title(nb)  # This would need adjusting, currently repo title
        return f"| {label} | {download} | {topics} | {colab} |"
    return f"| {label} | {download} | {colab} |"


def main():
    root = Path(__file__).resolve().parent
    notebooks = sorted(
        (nb for nb in root.rglob("*.ipynb") if nb.name not in SKIP),
        key=lambda p: p.relative_to(root).as_posix(),
    )

    groups: dict[str, list[Path]] = defaultdict(list)
    for nb in notebooks:
        groups[nb.parent.relative_to(root).as_posix()].append(nb)

    for part_dir in sorted(groups):
        print(f"**{part_dir}**\n")
        print("| (Code and) Topic | Notebook  | Colab |")
        print("|---|---|---|")
        for nb in groups[part_dir]:
            print(make_row(nb, root))
        print()


if __name__ == "__main__":
    main()