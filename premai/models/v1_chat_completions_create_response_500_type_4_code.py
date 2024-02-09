from enum import Enum


class V1ChatCompletionsCreateResponse500Type4Code(str, Enum):
    PROVIDERAPICONNECTIONERROR = "ProviderAPIConnectionError"

    def __str__(self) -> str:
        return str(self.value)
