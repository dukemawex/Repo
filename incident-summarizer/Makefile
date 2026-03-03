.PHONY: lint test pipeline paper report
lint:
	ruff check src tests scripts

test:
	pytest -q

pipeline:
	python scripts/run_pipeline.py --config config.yaml

paper:
	bash scripts/build_paper.sh

report:
	bash scripts/build_report.sh
