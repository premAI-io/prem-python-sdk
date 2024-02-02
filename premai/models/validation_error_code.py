from enum import Enum


class ValidationErrorCode(str, Enum):
    VALIDATIONERROR = "ValidationError"

    def __str__(self) -> str:
        return str(self.value)
