import cirq

# Setup for qubits 0 and 1
q0 = cirq.LineQubit(0)
q1 = cirq.LineQubit(1)

# Define operations of Hadamard gate to qubit 0, and cnot of qubit 0 and qubit 1 
h_op = cirq.H(q0)
cnot = cirq.CNOT(q0, q1)

# Create the circuit from the operation and cnot
circuit = cirq.Circuit([h_op, cnot])

# print the circuit diagram to see the moment structure
print(circuit)

# Simulate the circuit and check if it matches phi
simulator = cirq.Simulator()
result_sim = simulator.simulate(circuit)
print(result_sim.final_state_vector)