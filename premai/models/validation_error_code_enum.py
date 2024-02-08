from enum import Enum


class ValidationErrorCodeEnum(str, Enum):
    VALIDATIONERROR = "ValidationError"

    def __str__(self) -> str:
        return str(self.value)
