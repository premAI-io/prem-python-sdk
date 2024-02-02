from enum import Enum


class ProviderAPITimeoutErrorCodeEnum(str, Enum):
    PROVIDERAPITIMEOUTERROR = "ProviderAPITimeoutError"

    def __str__(self) -> str:
        return str(self.value)
