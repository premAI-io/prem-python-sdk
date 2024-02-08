from enum import Enum


class V1ChatCompletionsCreateResponse500Type3Code(str, Enum):
    PROVIDERAPITIMEOUTERROR = "ProviderAPITimeoutError"

    def __str__(self) -> str:
        return str(self.value)
