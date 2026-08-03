# Notes

## Completed
- (H⊗I)|00⟩ tensor product — paper math + NumPy verification
- CNOT applied to (H⊗I)|00⟩ → Bell state, entanglement proved by hand (contradiction) and in code (`entanglement/entanglement.py`)
- Cirq basics: qubit, gate, operation, circuit, moment, simulator (`entanglement/circuit_verification.py`)
- Symbolic parameterized gates: sympy.Symbol in Rz/Rx, resolve_parameters, sweep (`parameterized-gates/symbolic_gates.py`)

## Next session
Study Cirq gate protocols — how Cirq uses Python protocols/mixins (_unitary_, _decompose_, etc.) to define gate behavior. This is what lets you build *custom* parameterized gates for QML.

Context: `parameterized-gates/symbolic_gates.py` covers sympy.Symbol → resolve → simulate → verify. The sweep at the end shows how a single circuit template gets evaluated at many parameter values — that's the inner loop of variational QML training.
