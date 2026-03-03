
from __future__ import annotations
import argparse
from .pipeline import run_experiment

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--n", type=int, default=240)
    args = parser.parse_args()
    print(run_experiment(seed=args.seed, n=args.n))

if __name__ == "__main__":
    main()
