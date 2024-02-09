from enum import Enum


class ProviderNotFoundErrorCode(str, Enum):
    PROVIDERNOTFOUNDERROR = "ProviderNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
