from enum import Enum


class V1FinetuningCreateResponse422Code(str, Enum):
    UNPROCESSABLEENTITYERROR = "UnprocessableEntityError"

    def __str__(self) -> str:
        return str(self.value)
