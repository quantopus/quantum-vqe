import pytest
from quantum_vqe.main import VQEAlgorithm, VQEParams

def test_vqe_execution():
    """Tests that the VQE mock algorithm executes correctly."""
    params = VQEParams(operator_pauli_string="Z Z")
    algorithm = VQEAlgorithm()
    result = algorithm.execute(params)
    
    assert result.energy == -1.137
    assert result.meta["provider"] == "qiskit_mock"

def test_vqe_validation_error():
    """Tests that a validation error is raised for invalid params."""
    with pytest.raises(Exception): # Pydantic v2 raises pydantic.ValidationError
        VQEParams(operator_pauli_string="") # This should be caught by our logic 