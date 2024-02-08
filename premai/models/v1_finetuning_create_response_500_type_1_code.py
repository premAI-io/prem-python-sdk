from enum import Enum


class V1FinetuningCreateResponse500Type1Code(str, Enum):
    APIRESPONSEVALIDATIONERROR = "APIResponseValidationError"

    def __str__(self) -> str:
        return str(self.value)
