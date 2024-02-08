from enum import Enum


class ProviderInternalServerErrorCodeEnum(str, Enum):
    PROVIDERINTERNALSERVERERROR = "ProviderInternalServerError"

    def __str__(self) -> str:
        return str(self.value)
