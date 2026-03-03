from __future__ import annotations
import json, os
from pathlib import Path

def main() -> None:
    gemini = os.getenv("GEMINI_API_KEY")
    sources = Path("artifacts/sources.json")
    metrics = Path("artifacts/metrics.json")
    log = Path("docs/research_log.md")
    log.parent.mkdir(parents=True, exist_ok=True)
    src = json.loads(sources.read_text()) if sources.exists() else []
    met = json.loads(metrics.read_text()) if metrics.exists() else {}
    if gemini:
        note = f"## Gemini synthesis\nProcessed {len(src)} sources and metrics: {met}."
    else:
        note = "## Offline synthesis\nGEMINI_API_KEY missing; wrote placeholder narrative from local metrics."
    with log.open("a", encoding="utf-8") as f:
        f.write("\n" + note + "\n")

if __name__ == "__main__":
    main()
