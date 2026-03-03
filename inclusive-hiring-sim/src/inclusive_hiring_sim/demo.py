import streamlit as st
from .pipeline import run_experiment
st.title("Demo")
seed = st.number_input("seed", value=42)
n = st.slider("dataset size", 120, 500, 240)
st.json(run_experiment(seed=int(seed), n=int(n)))
