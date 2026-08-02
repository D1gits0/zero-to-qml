import numpy as np

# Basis States + Constant (from Week 1)
zero = np.array([1, 0])
one = np.array([0, 1])
inv_sqrt2 = 1 / np.sqrt(2)

# Recreate H, I, and yesterday's result
H = inv_sqrt2 * np.array([[1, 1], [1, -1]])
I = np.eye(2)
ket00 = np.kron(zero, zero)
result = np.dot(np.kron(H, I), ket00)

print(f"Starting state (result from Week 1): {result}")

# Step 1 - Build CNOT as a 4x4 matrix (identity with bottom-right block swapped)
# ket00 is defined above
ket01 = np.kron(zero, one)
ket10 = np.kron(one, zero)
ket11 = np.kron(one, one)

# If qubit 1 (control) is 1, qubit 2 (target) switches
CNOT = np.array([ket00, ket01, ket11, ket10])
print(f"CNOT: {CNOT}")

# Step 2 - Apply CNOT to 'result' using np.dot, store as 'phi' (or 'bell_state')

phi = np.dot(CNOT, result)

# Print phi and confirm it matches your hand answer: [0.707, 0, 0, 0.707]
print(f"phi: {phi}")

# Step 3 - Entanglement check: try a plausible candidate (a = H|0>, b = |0>),
# tensor them with np.kron, and confirm the result does NOT match phi

H_zero = np.dot(H, zero)

check = np.kron(H_zero, zero)
print(f"Check if this plausible candidate can match phi: {check}")