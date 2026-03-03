# supply-chain-anomaly-watch

![CI](https://github.com/ORG/supply-chain-anomaly-watch/actions/workflows/ci.yml/badge.svg)
![Pipeline](https://github.com/ORG/supply-chain-anomaly-watch/actions/workflows/pipeline.yml/badge.svg)
![Pages](https://img.shields.io/badge/pages-enabled-brightgreen)

Detect anomalies in supply-chain event streams with lightweight unsupervised models.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
make pipeline
```

## Reproducibility
- Fixed seed in `config.yaml`.
- End-to-end pipeline command: `python scripts/run_pipeline.py --config config.yaml`.

## Impact
- Positive impact: improves operational decision support with transparent lightweight ML.
- Risks: misuse of coarse predictions, fairness concerns, over-trust in synthetic signals.
- Mitigations: clear uncertainty notes, offline fallback transparency, human review requirement.

## Ethics and limitations
This repository uses small/synthetic data and should not be used for high-stakes deployment without domain validation.

## Local + CI
- `make lint test`
- `make pipeline`
- `make paper`
- `make report`
