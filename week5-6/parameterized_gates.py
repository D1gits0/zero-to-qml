import numpy as np
import sympy
import cirq

q0 = cirq.LineQubit(0)

# === Step 1: Create a symbolic parameter ===
# Define theta as a sympy.Symbol


# === Step 2: Build a parameterized Ry(theta) circuit ===
# Create a circuit with cirq.ry(theta) on q0


# === Step 3: Inspect the circuit ===
# Print the circuit and its parameter names


# === Step 4: Resolve theta to a specific value (e.g. pi/2) ===
# Use cirq.ParamResolver to bind theta, then cirq.resolve_parameters


# === Step 5: Get the unitary matrix ===
# Use cirq.unitary() on the resolved circuit


# === Step 6: Verify against hand-derived Ry matrix ===
# Ry(θ) = [[cos(θ/2), -sin(θ/2)],
#           [sin(θ/2),  cos(θ/2)]]
# Compute the expected matrix with numpy and assert np.allclose


# === Step 7: Simulate and check the state vector ===
# Use cirq.Simulator().simulate() on the resolved circuit
# Verify the result matches Ry(θ)|0⟩ = cos(θ/2)|0⟩ + sin(θ/2)|1⟩


# === Step 8 (bonus): Sweep theta from 0 to 2π ===
# Use cirq.Linspace to evaluate the circuit at multiple angles
# Print how the |0⟩ and |1⟩ amplitudes change — notice this moves population, unlike Rz
