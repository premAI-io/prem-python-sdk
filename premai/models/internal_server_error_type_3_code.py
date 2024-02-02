from enum import Enum


class InternalServerErrorType3Code(str, Enum):
    PROVIDERAPITIMEOUTERROR = "ProviderAPITimeoutError"

    def __str__(self) -> str:
        return str(self.value)
