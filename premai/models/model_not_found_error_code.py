from enum import Enum


class ModelNotFoundErrorCode(str, Enum):
    MODELNOTFOUNDERROR = "ModelNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
