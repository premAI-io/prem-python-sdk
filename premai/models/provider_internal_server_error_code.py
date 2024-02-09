from enum import Enum


class ProviderInternalServerErrorCode(str, Enum):
    PROVIDERINTERNALSERVERERROR = "ProviderInternalServerError"

    def __str__(self) -> str:
        return str(self.value)
