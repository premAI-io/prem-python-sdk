from enum import Enum


class V1ChatCompletionsCreateResponse422Code(str, Enum):
    UNPROCESSABLEENTITYERROR = "UnprocessableEntityError"

    def __str__(self) -> str:
        return str(self.value)
