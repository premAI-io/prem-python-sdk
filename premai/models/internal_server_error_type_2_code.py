from enum import Enum


class InternalServerErrorType2Code(str, Enum):
    PROVIDERAPISTATUSERROR = "ProviderAPIStatusError"

    def __str__(self) -> str:
        return str(self.value)
