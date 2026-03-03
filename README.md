# Multi-repo scaffolds

Contains 15 production-oriented repository scaffolds as requested.
# ml-engineering-15-lab

Monorepo with 15 ML engineering mini-project subpackages. Each project contains its own `paper/`, `report/`, and `config.yaml`, while shared automation lives in root `tooling/`.

## Repository layout

- `projects/<project_name>/paper/` reference notes
- `projects/<project_name>/report/` experiment/report outputs
- `projects/<project_name>/config.yaml` project metadata/config
- `tooling/` shared pipeline tooling

## Run a single project locally

```bash
python -m tooling.runner --project <project_name>
```

## Project index and commands

- [`01_feature_store_bootstrap`](projects/01_feature_store_bootstrap/README.md): `python -m tooling.runner --project 01_feature_store_bootstrap`
- [`02_batch_inference_quality_gate`](projects/02_batch_inference_quality_gate/README.md): `python -m tooling.runner --project 02_batch_inference_quality_gate`
- [`03_drift_detection_monitor`](projects/03_drift_detection_monitor/README.md): `python -m tooling.runner --project 03_drift_detection_monitor`
- [`04_llm_rag_eval_harness`](projects/04_llm_rag_eval_harness/README.md): `python -m tooling.runner --project 04_llm_rag_eval_harness`
- [`05_time_series_forecasting_baseline`](projects/05_time_series_forecasting_baseline/README.md): `python -m tooling.runner --project 05_time_series_forecasting_baseline`
- [`06_recommender_offline_eval`](projects/06_recommender_offline_eval/README.md): `python -m tooling.runner --project 06_recommender_offline_eval`
- [`07_ab_test_analysis_template`](projects/07_ab_test_analysis_template/README.md): `python -m tooling.runner --project 07_ab_test_analysis_template`
- [`08_data_quality_contracts`](projects/08_data_quality_contracts/README.md): `python -m tooling.runner --project 08_data_quality_contracts`
- [`09_model_card_generator`](projects/09_model_card_generator/README.md): `python -m tooling.runner --project 09_model_card_generator`
- [`10_retraining_orchestrator`](projects/10_retraining_orchestrator/README.md): `python -m tooling.runner --project 10_retraining_orchestrator`
- [`11_synthetic_data_benchmark`](projects/11_synthetic_data_benchmark/README.md): `python -m tooling.runner --project 11_synthetic_data_benchmark`
- [`12_privacy_risk_scanner`](projects/12_privacy_risk_scanner/README.md): `python -m tooling.runner --project 12_privacy_risk_scanner`
- [`13_cost_latency_profiler`](projects/13_cost_latency_profiler/README.md): `python -m tooling.runner --project 13_cost_latency_profiler`
- [`14_prompt_versioning_pipeline`](projects/14_prompt_versioning_pipeline/README.md): `python -m tooling.runner --project 14_prompt_versioning_pipeline`
- [`15_multimodal_ingestion_starter`](projects/15_multimodal_ingestion_starter/README.md): `python -m tooling.runner --project 15_multimodal_ingestion_starter`

## CI behavior

- One matrix workflow at `.github/workflows/project-pipelines.yml` runs selected projects.
- Default `push` / `pull_request` runs only the first **3** projects (keeps runtime under 10 minutes).
- Manual `workflow_dispatch` inputs:
  - `run_mode=default` → first 3 projects
  - `run_mode=all` → all 15 projects
  - `run_mode=custom` + `projects="p1,p2,..."` → selected projects only
