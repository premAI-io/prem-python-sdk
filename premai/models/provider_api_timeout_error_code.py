from enum import Enum


class ProviderAPITimeoutErrorCode(str, Enum):
    PROVIDERAPITIMEOUTERROR = "ProviderAPITimeoutError"

    def __str__(self) -> str:
        return str(self.value)
