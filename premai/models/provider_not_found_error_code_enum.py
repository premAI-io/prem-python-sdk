from enum import Enum


class ProviderNotFoundErrorCodeEnum(str, Enum):
    PROVIDERNOTFOUNDERROR = "ProviderNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
