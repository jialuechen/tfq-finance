import tensorflow as tf
import tensorflow_quantum as tfq
import cirq
import sympy
import numpy as np

def generate_hull_white(T, N, kappa, theta, sigma):
    qubits = [cirq.GridQubit(0, i) for i in range(N)]
    circuit = cirq.Circuit()
    for i in range(N):
        phi = sympy.Symbol(f'phi_{i}')
        circuit.append(cirq.rx(phi)(qubits[i]))
    return circuit

def simulate_hull_white(T, N, kappa, theta, sigma, samples=1000):
    circuit = generate_hull_white(T, N, kappa, theta, sigma)
    param_resolver = cirq.ParamResolver({f'phi_{i}': theta + sigma * np.sqrt(theta) * np.random.randn() for i in range(N)})
    simulator = cirq.Simulator()
    result = simulator.run(circuit, param_resolver=param_resolver, repetitions=samples)
    return result