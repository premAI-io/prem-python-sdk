from enum import Enum


class V1FinetuningRetrieveResponse500Type2Code(str, Enum):
    PROVIDERAPISTATUSERROR = "ProviderAPIStatusError"

    def __str__(self) -> str:
        return str(self.value)