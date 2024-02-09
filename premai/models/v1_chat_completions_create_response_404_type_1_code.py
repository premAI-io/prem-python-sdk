from enum import Enum


class V1ChatCompletionsCreateResponse404Type1Code(str, Enum):
    MODELNOTFOUNDERROR = "ModelNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
