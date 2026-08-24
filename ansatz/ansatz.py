import numpy as np
import cirq

q0, q1 = cirq.LineQubit.range(2)
theta1 = 0.5
theta2 = 0.5

# === Step 1: Build the ansatz circuit ===
# Ry(theta1) on q0, Ry(theta2) on q1, then CNOT(q0, q1)
op_q0 = cirq.ry(theta1).on(q0)
op_q1 = cirq.ry(theta2).on(q1)

circuit = cirq.Circuit(op_q0, op_q1, cirq.CNOT(q0, q1))


# === Step 2: Simulate and get the 4-entry state vector ===
# Compare against hand-derived [0.939, 0.239, 0.061, 0.239]

state_vector = cirq.Simulator().simulate(circuit).final_state_vector
print(state_vector) 


# === Step 3: Compute expectation value on qubit 0 ===
# P(0) = |entry1|^2 + |entry2|^2, P(1) = |entry3|^2 + |entry4|^2
# expectation = P(0) - P(1)
# Compare against hand-derived ~0.878

p0 = np.abs(state_vector[0])**2 + np.abs(state_vector[1])**2
p1 = np.abs(state_vector[2])**2 + np.abs(state_vector[3])**2

expectation = p0 - p1
print(expectation)