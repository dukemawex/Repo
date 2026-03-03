from __future__ import annotations
import argparse
import json
from pathlib import Path
import yaml
import matplotlib.pyplot as plt
from actionlab_ablation_runner.pipeline import run_experiment, save_metrics

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    metrics = run_experiment(seed=int(cfg.get("seed", 42)), n=int(cfg.get("dataset_size", 240)))
    save_metrics(Path("artifacts/metrics.json"), metrics)
    fig_dir = Path("artifacts/figures")
    fig_dir.mkdir(parents=True, exist_ok=True)
    plt.figure()
    plt.bar(["accuracy"], [metrics["accuracy"]])
    plt.ylim(0, 1)
    plt.title("Evaluation Metric")
    plt.savefig(fig_dir / "metric_plot.png", dpi=120)
    Path("report/docs/results.md").write_text("# Results\n\n```json\n"+json.dumps(metrics, indent=2)+"\n```\n")

if __name__ == "__main__":
    main()
