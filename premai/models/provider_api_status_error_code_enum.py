from enum import Enum


class ProviderAPIStatusErrorCodeEnum(str, Enum):
    PROVIDERAPISTATUSERROR = "ProviderAPIStatusError"

    def __str__(self) -> str:
        return str(self.value)
