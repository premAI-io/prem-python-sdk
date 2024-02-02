from enum import Enum


class ConflictErrorCode(str, Enum):
    CONFLICTERROR = "ConflictError"

    def __str__(self) -> str:
        return str(self.value)
