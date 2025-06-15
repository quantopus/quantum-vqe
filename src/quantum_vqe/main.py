from pydantic import Field

from quantum_interfaces import (
    AlgorithmParams,
    AlgorithmResult,
    BaseAlgorithm,
    ValidationError,
)

# 1. Определяем типизированные параметры для VQE
class VQEParams(AlgorithmParams):
    operator_pauli_string: str = Field(
        ...,
        description="The Pauli string representation of the operator (e.g., 'Z Z').",
        min_length=1,
    )

# 2. Определяем типизированный результат для VQE
class VQEResult(AlgorithmResult):
    energy: float = Field(..., description="The final ground state energy.")

# 3. Реализуем сам алгоритм
class VQEAlgorithm(BaseAlgorithm[VQEParams, VQEResult]):
    def validate_params(self, params: VQEParams) -> None:
        # Pydantic's `min_length=1` now handles this validation on creation.
        # This method can be used for more complex, cross-field validation.
        pass

    def execute(self, params: VQEParams) -> VQEResult:
        # No need to call validate_params if it's empty
        
        # Мок реализация
        print(f"Mock VQE execution for operator: {params.operator_pauli_string}")
        
        return VQEResult(
            energy=-1.137,
            meta={"algorithm": "VQE", "provider": "qiskit_mock"}
        )

# Создаем __init__.py для корректной работы entry_point 