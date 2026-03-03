from __future__ import annotations

import json
from pathlib import Path

import streamlit as st

from .pipeline import run_evaluation


st.set_page_config(page_title="safe-rag-benchmark", layout="wide")
st.title("safe-rag-benchmark demo")
st.caption("Tavily retrieval + Gemini structured answer + live fidelity metrics")

output_dir = Path(st.text_input("Artifact output directory", value="report"))
question_text = st.text_area(
    "Questions (one per line)",
    value="What are safety best practices for deploying AI assistants in healthcare?\nHow do risk frameworks reduce hallucinations in enterprise RAG systems?",
)
min_sources = st.slider("Minimum source threshold", min_value=1, max_value=6, value=3)

if st.button("Run evaluation"):
    questions = [line.strip() for line in question_text.splitlines() if line.strip()]
    metrics = run_evaluation(output_dir=output_dir, questions=questions, min_sources=min_sources)

    st.subheader("Metrics")
    st.json(metrics)

    retrieval_path = output_dir / "retrieval.jsonl"
    answers_path = output_dir / "answers.jsonl"

    st.subheader("Retrieval")
    if retrieval_path.exists():
        retrieval_rows = [json.loads(line) for line in retrieval_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        for row in retrieval_rows:
            with st.expander(row["question"]):
                st.write(f"min_sources_met={row['min_sources_met']} source_count={row['source_count']}")
                st.dataframe(row["sources"])

    st.subheader("Answers")
    if answers_path.exists():
        answer_rows = [json.loads(line) for line in answers_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        for row in answer_rows:
            with st.expander(row["question"]):
                st.write(row["answer"])
                st.write({"claims": row["claims"], "citations": row["citations"]})
