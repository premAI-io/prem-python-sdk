from enum import Enum


class ModelNotFoundErrorCodeEnum(str, Enum):
    MODELNOTFOUNDERROR = "ModelNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
