from enum import Enum


class V1FinetuningRetrieveResponse409Code(str, Enum):
    CONFLICTERROR = "ConflictError"

    def __str__(self) -> str:
        return str(self.value)
