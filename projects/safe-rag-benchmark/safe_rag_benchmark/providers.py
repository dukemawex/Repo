from __future__ import annotations

import json
import os
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .models import Source


class TavilyRetriever:
    def __init__(self, api_key: str | None = None, min_sources: int = 3) -> None:
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")
        self.min_sources = min_sources

    def retrieve(self, question: str) -> list[Source]:
        if not self.api_key:
            return self._mock_retrieve(question)

        payload = {
            "api_key": self.api_key,
            "query": question,
            "search_depth": "advanced",
            "max_results": 8,
        }
        results = _post_json("https://api.tavily.com/search", payload).get("results", [])
        sources: list[Source] = []
        for idx, item in enumerate(results):
            url = item.get("url", "")
            domain = urlparse(url).netloc
            sources.append(
                Source(
                    source_id=f"S{idx + 1}",
                    title=item.get("title", "untitled"),
                    url=url,
                    snippet=item.get("content", ""),
                    domain=domain,
                )
            )
        return sources

    def _mock_retrieve(self, question: str) -> list[Source]:
        seed = question.lower()
        canned = [
            Source("S1", "NIST AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework", "NIST AI RMF discusses governance, mapping, measurement, and management for AI risks.", "www.nist.gov"),
            Source("S2", "OECD AI Principles", "https://oecd.ai/en/ai-principles", "OECD principles emphasize transparency, robustness, and accountability.", "oecd.ai"),
            Source("S3", "WHO AI Ethics", "https://www.who.int/publications/i/item/9789240029200", "WHO guidance highlights patient safety and human oversight in AI systems.", "www.who.int"),
            Source("S4", "EU AI Act overview", "https://artificialintelligenceact.eu/high-level-summary/", "EU AI Act summary describes risk tiers and obligations for high-risk systems.", "artificialintelligenceact.eu"),
        ]
        if "medical" in seed:
            return canned[:3]
        return canned


class GeminiGenerator:
    def __init__(self, api_key: str | None = None, model: str = "gemini-1.5-pro") -> None:
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model = model

    def generate_structured(self, question: str, sources: list[Source]) -> dict[str, object]:
        if not self.api_key:
            return self._mock_generate(question, sources)

        snippet_block = "\n".join(
            f"[{src.source_id}] {src.title}: {src.snippet} ({src.url})" for src in sources
        )
        prompt = (
            "You are a safety-focused RAG assistant. Return JSON only with keys answer, claims, citations. "
            "Claims must be sentence-level and citations must be source IDs such as S1. "
            f"Question: {question}\nSources:\n{snippet_block}"
        )
        endpoint = (
            f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent"
            f"?key={self.api_key}"
        )
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"temperature": 0.1},
        }
        raw = _post_json(endpoint, payload)
        text = raw["candidates"][0]["content"]["parts"][0]["text"]
        return json.loads(text)

    def _mock_generate(self, question: str, sources: list[Source]) -> dict[str, object]:
        claims = [
            "Risk frameworks recommend governance and continuous monitoring for AI systems.",
            "Safety guidance emphasizes transparency and human oversight for high-impact deployments.",
        ]
        answer = " ".join(claims)
        citations = [s.source_id for s in sources[:2]]
        return {"answer": answer, "claims": claims, "citations": citations}


def _post_json(url: str, payload: dict[str, object]) -> dict[str, object]:
    req = Request(
        url=url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(req, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)
