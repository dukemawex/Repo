# safe-rag-benchmark

Reproducible safety evaluation framework for RAG systems with:

- **Citation fidelity**
- **Retrieval grounding**
- **Hallucination proxy rate**
- **Harm risk indicators**

## Architecture

- Retrieval provider: **Tavily only** (`TavilyRetriever`)
- Generation provider: **Gemini only** (`GeminiGenerator`)
- Structured answer contract:

```json
{
  "answer": "...",
  "claims": ["..."],
  "citations": ["S1", "S2"]
}
```

## Artifact outputs

Running the pipeline writes:

- `retrieval.jsonl`
- `answers.jsonl`
- `fidelity_scores.json`
- `safety_flags.json`
- `sources.json`
- `metrics.json`

## Run evaluation

```bash
cd projects/safe-rag-benchmark
python -m safe_rag_benchmark.pipeline --output-dir report
```

Set API keys for live providers:

```bash
export TAVILY_API_KEY=...
export GEMINI_API_KEY=...
```

If keys are missing, deterministic mock providers are used for reproducible local testing.

## Demo

```bash
cd projects/safe-rag-benchmark
streamlit run safe_rag_benchmark/demo.py
```

The demo displays retrieval rows, structured answers, and live fidelity metrics.

## Testing

```bash
cd projects/safe-rag-benchmark
python -m unittest discover -s tests -v
```
