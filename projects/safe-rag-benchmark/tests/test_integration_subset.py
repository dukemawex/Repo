from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from safe_rag_benchmark.pipeline import run_evaluation


class IntegrationSubsetTests(unittest.TestCase):
    def test_full_pipeline_subset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            metrics = run_evaluation(
                output_dir=out,
                questions=["What are safe deployment practices for medical AI assistants?"],
                min_sources=2,
            )
            self.assertEqual(metrics["question_count"], 1)

            expected = [
                "retrieval.jsonl",
                "answers.jsonl",
                "fidelity_scores.json",
                "safety_flags.json",
                "sources.json",
                "metrics.json",
            ]
            for artifact in expected:
                self.assertTrue((out / artifact).exists(), f"Missing {artifact}")

            with (out / "metrics.json").open("r", encoding="utf-8") as handle:
                saved_metrics = json.load(handle)
            self.assertIn("avg_citation_precision", saved_metrics)


if __name__ == "__main__":
    unittest.main()
