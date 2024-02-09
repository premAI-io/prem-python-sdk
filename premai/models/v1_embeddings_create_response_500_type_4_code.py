from enum import Enum


class V1EmbeddingsCreateResponse500Type4Code(str, Enum):
    PROVIDERAPICONNECTIONERROR = "ProviderAPIConnectionError"

    def __str__(self) -> str:
        return str(self.value)
