from enum import Enum


class V1ChatCompletionsCreateResponse500Type1Code(str, Enum):
    APIRESPONSEVALIDATIONERROR = "APIResponseValidationError"

    def __str__(self) -> str:
        return str(self.value)
