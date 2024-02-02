from enum import Enum


class V1FinetuningRetrieveResponse500Type1Code(str, Enum):
    APIRESPONSEVALIDATIONERROR = "APIResponseValidationError"

    def __str__(self) -> str:
        return str(self.value)
