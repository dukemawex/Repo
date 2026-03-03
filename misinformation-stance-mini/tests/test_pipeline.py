from misinformation_stance_mini.pipeline import run_experiment

def test_run_experiment_has_accuracy():
    metrics = run_experiment(seed=42, n=120)
    assert 0.0 <= metrics["accuracy"] <= 1.0
