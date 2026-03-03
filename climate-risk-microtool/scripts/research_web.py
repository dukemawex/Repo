from __future__ import annotations
import json, os
from pathlib import Path
import requests

def main() -> None:
    out = Path("artifacts/sources.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    key = os.getenv("TAVILY_API_KEY")
    if not key:
        seed = Path("data/sample/sources_seed.json")
        out.write_text(seed.read_text())
        return
    payload = {"api_key": key, "query": "lightweight machine learning evaluation reproducibility", "max_results": 3}
    r = requests.post("https://api.tavily.com/search", json=payload, timeout=30)
    r.raise_for_status()
    data = r.json().get("results", [])
    out.write_text(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
