"""
Symbolic Parameterized Gates
=============================
Goal: Understand how Cirq uses sympy.Symbol to create parameterized circuits,
resolve symbols to numeric values, simulate, and verify state vectors.

Key concepts:
- sympy.Symbol('theta') creates a free parameter in a gate
- cirq.resolve_parameters() binds symbols to numeric values
- A parameterized circuit is the backbone of variational/hybrid QML
"""

import numpy as np
import sympy
import cirq

# --- Step 1: Create a symbolic parameter ---
theta = sympy.Symbol('theta')
print(f"Symbolic parameter: {theta} (type: {type(theta)})")

# --- Step 2: Build a parameterized circuit ---
# Rz(theta) on qubit 0, then measure-free simulation
q0 = cirq.LineQubit(0)

# cirq.rz(rads) creates an Rz gate — pass a sympy.Symbol to keep it symbolic
circuit = cirq.Circuit([
    cirq.rz(theta).on(q0),
])

print("\nParameterized circuit (symbolic):")
print(circuit)

# --- Step 3: Inspect — the circuit can't be simulated yet (theta is unresolved) ---
print(f"\nParameters in circuit: {sorted(cirq.parameter_names(circuit))}")

# --- Step 4: Resolve the parameter to a numeric value ---
# Let's try theta = pi/2
resolver = cirq.ParamResolver({'theta': np.pi / 2})
resolved_circuit = cirq.resolve_parameters(circuit, resolver)

print(f"\nResolved circuit (theta = π/2):")
print(resolved_circuit)

# --- Step 5: Simulate the resolved circuit ---
sim = cirq.Simulator()
result = sim.simulate(resolved_circuit)
state = result.final_state_vector

print(f"\nState vector after Rz(π/2)|0⟩:")
print(f"  {state}")
print(f"  |0⟩ amplitude: {state[0]:.4f}")
print(f"  |1⟩ amplitude: {state[1]:.4f}")

# --- Step 6: Verify by hand ---
# Rz(θ) = [[e^{-iθ/2}, 0], [0, e^{iθ/2}]]
# Rz(π/2)|0⟩ = e^{-iπ/4} |0⟩
# So state should be [e^{-iπ/4}, 0]
expected = np.array([np.exp(-1j * np.pi / 4), 0], dtype=np.complex64)
print(f"\nExpected (manual calc):")
print(f"  {expected}")

assert np.allclose(state, expected, atol=1e-6), "Mismatch!"
print("\n✓ Simulation matches hand calculation.")


# =============================================================================
# Part 2: Multi-parameter circuit — Rx(α) → Rz(β) → measure state
# =============================================================================
print("\n" + "=" * 60)
print("Part 2: Two-parameter circuit Rx(α) → Rz(β)")
print("=" * 60)

alpha = sympy.Symbol('alpha')
beta = sympy.Symbol('beta')

circuit2 = cirq.Circuit([
    cirq.rx(alpha).on(q0),
    cirq.rz(beta).on(q0),
])

print(f"\nParameterized circuit:")
print(circuit2)
print(f"Parameters: {sorted(cirq.parameter_names(circuit2))}")

# Resolve: alpha = pi/2, beta = pi
resolver2 = cirq.ParamResolver({'alpha': np.pi / 2, 'beta': np.pi})
resolved2 = cirq.resolve_parameters(circuit2, resolver2)

result2 = sim.simulate(resolved2)
state2 = result2.final_state_vector

print(f"\nState vector after Rx(π/2) → Rz(π) on |0⟩:")
print(f"  {state2}")

# Manual verification:
# Rx(π/2)|0⟩ = cos(π/4)|0⟩ - i·sin(π/4)|1⟩ = (1/√2)|0⟩ - (i/√2)|1⟩
# Then Rz(π) applied: Rz(π) = [[e^{-iπ/2}, 0], [0, e^{iπ/2}]]
#   = [[-i, 0], [0, i]]  (i.e. diag(-i, i))
# Rz(π) · (1/√2)(|0⟩ - i|1⟩) = (1/√2)(-i|0⟩ - i·i|1⟩) = (1/√2)(-i|0⟩ + |1⟩)
expected2 = np.array([-1j / np.sqrt(2), 1.0 / np.sqrt(2)], dtype=np.complex64)

print(f"\nExpected (manual calc):")
print(f"  {expected2}")

assert np.allclose(state2, expected2, atol=1e-6), "Mismatch!"
print("\n✓ Two-parameter simulation matches hand calculation.")


# =============================================================================
# Part 3: Sweep — evaluate the same circuit at multiple parameter values
# =============================================================================
print("\n" + "=" * 60)
print("Part 3: Parameter sweep (varying theta in Rz)")
print("=" * 60)

sweep_circuit = cirq.Circuit([cirq.rz(theta).on(q0)])

# Sweep theta from 0 to 2π in 8 steps
sweep = cirq.Linspace('theta', start=0, stop=2 * np.pi, length=8)

print(f"\nSweeping theta over {len(list(sweep))} values:")
print(f"{'theta':>10} | {'|0⟩ amp':>20} | {'|1⟩ amp':>20}")
print("-" * 55)

for resolver in sweep:
    resolved = cirq.resolve_parameters(sweep_circuit, resolver)
    res = sim.simulate(resolved)
    sv = res.final_state_vector
    theta_val = resolver.param_dict['theta']
    print(f"{theta_val:>10.4f} | {sv[0]:>20} | {sv[1]:>20}")

print("\nNote: |0⟩ amplitude rotates in phase (e^{-iθ/2}), |1⟩ stays 0.")
print("This is a *phase* rotation — no population transfer. That's Rz.")
