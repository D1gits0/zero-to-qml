import numpy as np
import cirq

# === Step 1: Check has_unitary on known gates ===
# Try cirq.has_unitary(cirq.H) and cirq.has_unitary(cirq.ry(0.5))
# Both should return True

print(cirq.has_unitary(cirq.H))
print(cirq.has_unitary(cirq.ry(0.5)))


# === Step 2: Extract CNOT's unitary matrix ===
# Use cirq.unitary(cirq.CNOT) — compare to your hand-derived CNOT matrix from Week 1-2

print(cirq.has_unitary(cirq.CNOT))

# === Step 3 (reading, optional): Explore _decompose_ ===
# Try cirq.decompose() on a more complex gate and see what simpler gates it breaks into

q0, q1, q2 = cirq.LineQubit.range(3)
print(cirq.decompose(cirq.TOFFOLI.on(q0, q1, q2)))