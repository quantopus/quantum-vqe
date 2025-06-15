# Quantum VQE

Variational Quantum Eigensolver (VQE) algorithm implementation using Qiskit.

## Overview

VQE is a hybrid quantum-classical algorithm for finding the ground state energy of quantum systems. This implementation provides:

- Qiskit-based quantum circuit simulation
- Typed parameters with Pydantic validation
- Flexible ansatz and optimizer configurations
- Integration with Quantopus ecosystem

## Installation

```bash
make dev-install
```

## Usage

```python
from quantum_vqe import VQEAlgorithm, VQEParams

# Create VQE instance
vqe = VQEAlgorithm()

# Set parameters
params = VQEParams(
    operator_pauli_string="Z Z",
    ansatz_type="UCCSD",
    optimizer="SLSQP",
    max_iterations=100
)

# Execute algorithm
result = vqe.execute(params)
print(f"Ground state energy: {result.energy}")
```

## Demo

```bash
make demo
```

## Development

```bash
make test     # Run tests
make lint     # Check code quality
make format   # Format code
```

Part of the [Quantopus](https://github.com/quantopus) quantum computing ecosystem.
