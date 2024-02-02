from enum import Enum


class ProviderAPIConnectionErrorCodeEnum(str, Enum):
    PROVIDERAPICONNECTIONERROR = "ProviderAPIConnectionError"

    def __str__(self) -> str:
        return str(self.value)
