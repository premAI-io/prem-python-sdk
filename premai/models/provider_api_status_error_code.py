from enum import Enum


class ProviderAPIStatusErrorCode(str, Enum):
    PROVIDERAPISTATUSERROR = "ProviderAPIStatusError"

    def __str__(self) -> str:
        return str(self.value)
