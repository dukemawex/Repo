from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def run_experiment(seed: int = 42, n: int = 240) -> dict:
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(n, 5))
    y = (x[:, 0] + 0.2 * x[:, 1] + rng.normal(scale=0.8, size=n) > 0).astype(int)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=seed)
    model = LogisticRegression(max_iter=300)
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    acc = float(accuracy_score(y_test, pred))
    return {"accuracy": round(acc, 4), "n_test": int(len(y_test)), "project": "fairness-monitor-lite"}

def save_metrics(path: Path, metrics: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(metrics, indent=2))
