import numpy as np
import cirq

q0, q1 = cirq.LineQubit.range(2)
theta1 = 0.5
theta2 = 0.5

# === Step 1: Build the ansatz circuit ===
# Ry(theta1) on q0, Ry(theta2) on q1, then CNOT(q0, q1)


# === Step 2: Simulate and get the 4-entry state vector ===
# Compare against hand-derived [0.939, 0.239, 0.061, 0.239]


# === Step 3: Compute expectation value on qubit 0 ===
# P(0) = |entry1|^2 + |entry2|^2, P(1) = |entry3|^2 + |entry4|^2
# expectation = P(0) - P(1)
# Compare against hand-derived ~0.878
