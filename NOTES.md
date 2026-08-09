# Notes

## Completed
- (H⊗I)|00⟩ tensor product — paper math + NumPy verification
- CNOT applied to (H⊗I)|00⟩ → Bell state, entanglement proved by hand (contradiction) and in code (`entanglement/entanglement.py`)
- Cirq basics: qubit, gate, operation, circuit, moment, simulator (`entanglement/circuit_verification.py`)
- Symbolic parameterized gates: sympy.Symbol in Rz/Rx, resolve_parameters, sweep
- Ry(theta) unitary + state vector verified against hand-derived formula (`parameterized-gates/parameterized_gates.py`)
- Gate protocols: has_unitary, unitary on CNOT, decompose on Toffoli (`parameterized-gates/gate_protocols.py`)

**Milestone 1 complete.**

- 2-feature angle encoding: Ry(x1) on q0, Ry(x2) on q1, verified against tensor-product cross-check (`feature-maps/angle_encoding_2feature.py`)

**Milestone 2 (feature maps) in progress.**

## Next session
Ansatz — build a parameterized trainable layer (Ry rotations + entangling CNOT) that follows the feature map.

Note: zero-to-qml sessions happen only after DSA/applications work is handled that day.
