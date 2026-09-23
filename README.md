# Classroom Flu Spread Simulation

A Python simulation modelling an infectious flu outbreak in an elementary classroom (51 students) using a stochastic S-I-R model across 1,000 Monte Carlo runs.

## Key Findings
* **No Vaccination:** ~18 kids infected over ~20 days.
* **60% Vaccination Rate:** ~2 kids infected over 2–3 days (demonstrating herd immunity).

## How It Works
* **Logic:** S-I-R model tracking states (`-1`: Immune, `0`: Healthy, `1–3`: Infectious, `4`: Recovered).
* **Risk:** Daily infection risk calculated via Bernoulli trials: `P(No Infection) = 0.99 ^ (infectious_count)`.

## Repository Files
* `main.py`: Full Python code and Matplotlib plots.
* `Pandemic Flu - Munzareen Kazi.pdf`: Academic paper with literature review and statistical proofs
