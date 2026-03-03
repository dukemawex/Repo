from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Source:
    source_id: str
    title: str
    url: str
    snippet: str
    domain: str


@dataclass
class RetrievalRecord:
    question: str
    min_sources_met: bool
    sources: list[Source] = field(default_factory=list)


@dataclass
class AnswerRecord:
    question: str
    answer: str
    claims: list[str]
    citations: list[str]


@dataclass
class ClaimScore:
    claim: str
    supported: bool
    supporting_source_ids: list[str]


@dataclass
class FidelityScore:
    question: str
    claim_scores: list[ClaimScore]
    citation_precision: float
    citation_recall: float
    hallucination_proxy_rate: float
    retrieval_grounding_rate: float
