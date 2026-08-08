import numpy as np
import cirq

# Data points to encode
x1 = 0.75
x2 = 0.3

q0, q1 = cirq.LineQubit.range(2)

# === Step 1: Hand-derive the single-qubit states ===
# Ry(x)|0⟩ = cos(x/2)|0⟩ + sin(x/2)|1⟩
# Compute state_q0 = [cos(x1/2), sin(x1/2)]
# Compute state_q1 = [cos(x2/2), sin(x2/2)]

state_q0 = cirq.ry(x1).on(q0)
state_q1 = cirq.ry(x2).on(q1)


# === Step 2: Build the 2-qubit angle-encoding circuit ===
# Ry(x1) on q0, Ry(x2) on q1, both in one Circuit

circuit = cirq.Circuit(state_q0, state_q1)
print(circuit)
# === Step 3: Simulate and extract the 4-entry state vector ===
# Use cirq.Simulator().simulate(circuit).final_state_vector

simulated_state = cirq.Simulator().simulate(circuit).final_state_vector
print(simulated_state)

# === Step 4: Compute the expected 4-vector via tensor product ===
# Since the qubits are independent: full_state = np.kron(state_q0, state_q1)

state_q0 = np.array([np.cos(x1/2), np.sin(x1/2)])
state_q1 = np.array([np.cos(x2/2), np.sin(x2/2)])
expected_state = np.kron(state_q0, state_q1)

# === Step 5: Assert they match ===
# np.allclose(simulated_state, expected_state)
# Print both vectors and confirm

print(np.allclose(simulated_state, expected_state))