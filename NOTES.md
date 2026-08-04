# Notes

## Completed
- (H⊗I)|00⟩ tensor product — paper math + NumPy verification
- CNOT applied to (H⊗I)|00⟩ → Bell state, entanglement proved by hand (contradiction) and in code (`entanglement/entanglement.py`)
- Cirq basics: qubit, gate, operation, circuit, moment, simulator (`entanglement/circuit_verification.py`)
- Symbolic parameterized gates: sympy.Symbol in Rz/Rx, resolve_parameters, sweep (`parameterized-gates/symbolic_gates.py`)

## Next session
Code Ry(theta) with sympy.Symbol in Cirq, verify cirq.unitary() at a specific angle matches the hand-derived matrix.

Context: `parameterized-gates/symbolic_gates.py` covers sympy.Symbol → resolve → simulate → verify. The sweep at the end shows how a single circuit template gets evaluated at many parameter values — that's the inner loop of variational QML training.
