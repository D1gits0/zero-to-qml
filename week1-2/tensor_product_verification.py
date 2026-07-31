import numpy as np

# Basis States + Constant
zero = np.array([1, 0])
one = np.array([0, 1])
inv_sqrt2 = 1 / np.sqrt(2)

# Step 1 - Calculate ket of 00 with tensor of 'zero'
ket00 = np.kron(zero, zero)
print(f"ket00: {ket00}")

# Step 2 - Calculate tensor of Hadamard Gate and Identity Gate
H = inv_sqrt2 * np.array([[1, 1], [1, -1]])
I = np.eye(2)

H_tensor_I = np.kron(H, I)

print(f"Hadamard Gate tensor Identity Gate: {H_tensor_I}")

# Step 3 - dot 'H_tensor_I' and ket of 00
result = np.dot(H_tensor_I, ket00)

print(f"Result: {result}")

# Cross-Check - Easier way, find ket +
H_zero = np.dot(H, zero)
I_zero = np.dot(I, zero)

check_result = np.kron(H_zero, I_zero)
print(f"Check: {check_result}")