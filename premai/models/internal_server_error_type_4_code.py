from enum import Enum


class InternalServerErrorType4Code(str, Enum):
    PROVIDERAPICONNECTIONERROR = "ProviderAPIConnectionError"

    def __str__(self) -> str:
        return str(self.value)
