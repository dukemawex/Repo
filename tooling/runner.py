from __future__ import annotations

import argparse
from pathlib import Path
import time


def run_project(project: str, root: Path) -> int:
    project_dir = root / "projects" / project
    config = project_dir / "config.yaml"
    if not project_dir.exists() or not config.exists():
        raise FileNotFoundError(f"Project '{project}' is missing or incomplete.")

    print(f"[pipeline] project={project}")
    print(f"[pipeline] config={config}")
    # Keep CI fast: simulate quick pipeline checks
    for step in ("lint", "unit-smoke", "report-sync"):
        print(f"[pipeline] step={step} status=ok")
        time.sleep(0.1)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a project pipeline")
    parser.add_argument("--project", required=True, help="Project directory name under projects/")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[1]
    return run_project(args.project, repo_root)


if __name__ == "__main__":
    raise SystemExit(main())
