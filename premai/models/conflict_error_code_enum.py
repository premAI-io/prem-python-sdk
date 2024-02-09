from enum import Enum


class ConflictErrorCodeEnum(str, Enum):
    CONFLICTERROR = "ConflictError"

    def __str__(self) -> str:
        return str(self.value)
