import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Symbolic Error Corrector", layout="wide")
st.title("🧠 Recursive Symbolic Error Corrector")

st.markdown("""
This tool simulates **recursive symbolic correction** in noisy identity structures. 
It analyzes symbolic drift and applies feedback logic to restore coherence over time.
""")

# Sidebar controls
st.sidebar.header("Input Parameters")
sequence_length = st.sidebar.slider("Sequence Length", 20, 100, 50)
error_rate = st.sidebar.slider("Symbolic Noise Rate", 0.0, 1.0, 0.2)
correction_strength = st.sidebar.slider("Correction Feedback Strength", 0.1, 2.0, 1.0)

# Simulate symbolic sequence with noise
np.random.seed(0)
true_signal = np.sin(np.linspace(0, 3 * np.pi, sequence_length))
noise = np.random.normal(0, error_rate, sequence_length)
noisy_signal = true_signal + noise

# Apply recursive correction
corrected_signal = []
current = 0
for i in range(sequence_length):
    correction = correction_strength * (true_signal[i] - current)
    current += correction
    corrected_signal.append(current)

df = pd.DataFrame({
    "Token": np.arange(sequence_length),
    "True Signal": true_signal,
    "Noisy Signal": noisy_signal,
    "Corrected Signal": corrected_signal
})

# Plot
fig = px.line(df, x="Token", y=["True Signal", "Noisy Signal", "Corrected Signal"],
              title="Recursive Symbolic Error Correction", labels={"value": "Signal Strength"})
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Interpretation")
st.markdown("""
This simulation shows how recursive feedback logic can stabilize symbolic trajectories corrupted by drift.
Useful for modeling identity repair, memory reinforcement, or belief revision.
""")
