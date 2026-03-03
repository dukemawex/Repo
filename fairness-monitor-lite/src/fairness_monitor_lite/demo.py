from fastapi import FastAPI
from .pipeline import run_experiment
app = FastAPI()

@app.get("/predict")
def predict(seed: int = 42, n: int = 240):
    return run_experiment(seed=seed, n=n)
