from enum import Enum


class UnprocessableEntityErrorCode(str, Enum):
    UNPROCESSABLEENTITYERROR = "UnprocessableEntityError"

    def __str__(self) -> str:
        return str(self.value)
