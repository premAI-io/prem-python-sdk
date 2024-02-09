from enum import Enum


class ProviderAPIConnectionErrorCode(str, Enum):
    PROVIDERAPICONNECTIONERROR = "ProviderAPIConnectionError"

    def __str__(self) -> str:
        return str(self.value)
