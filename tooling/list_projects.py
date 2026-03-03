from __future__ import annotations

from pathlib import Path


def list_projects(repo_root: Path) -> list[str]:
    projects_dir = repo_root / "projects"
    return sorted(p.name for p in projects_dir.iterdir() if p.is_dir())


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    for name in list_projects(root):
        print(name)
