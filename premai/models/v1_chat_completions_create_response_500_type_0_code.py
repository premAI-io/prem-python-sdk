from enum import Enum


class V1ChatCompletionsCreateResponse500Type0Code(str, Enum):
    PROVIDERINTERNALSERVERERROR = "ProviderInternalServerError"

    def __str__(self) -> str:
        return str(self.value)
