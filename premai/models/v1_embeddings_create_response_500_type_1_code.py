from enum import Enum


class V1EmbeddingsCreateResponse500Type1Code(str, Enum):
    APIRESPONSEVALIDATIONERROR = "APIResponseValidationError"

    def __str__(self) -> str:
        return str(self.value)
