from enum import Enum


class V1FinetuningCreateResponse500Type3Code(str, Enum):
    PROVIDERAPITIMEOUTERROR = "ProviderAPITimeoutError"

    def __str__(self) -> str:
        return str(self.value)
