from enum import Enum


class V1FinetuningRetrieveResponse400Code(str, Enum):
    VALIDATIONERROR = "ValidationError"

    def __str__(self) -> str:
        return str(self.value)
