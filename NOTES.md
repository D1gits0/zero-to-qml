# Notes

## Completed
- (H⊗I)|00⟩ tensor product — paper math + NumPy verification
- CNOT applied to (H⊗I)|00⟩ → Bell state, entanglement proved by hand (contradiction) and in code (`entanglement/entanglement.py`)

## Next session
Weeks 3-4: replicate the H⊗I → CNOT → Bell state circuit in Cirq, verify it matches the NumPy `phi` from `entanglement/entanglement.py`.

Core objects to learn: `cirq.Qubit` (use `cirq.LineQubit`), `cirq.Gate`, `cirq.Operation`. Build a `cirq.Circuit` by appending operations, print it and look at the `cirq.Moment` structure before running it. Pull the state vector with `cirq.Simulator().simulate().state_vector()` and check it against `phi`.

Setup: cirq is already installed (`pip install numpy cirq` — done). File ready: `entanglement/circuit_verification.py` (empty, look up Cirq's qubit/gate/operation basics before writing).
