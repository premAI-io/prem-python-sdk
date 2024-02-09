from enum import Enum


class V1EmbeddingsCreateResponse404Type0Code(str, Enum):
    PROVIDERNOTFOUNDERROR = "ProviderNotFoundError"

    def __str__(self) -> str:
        return str(self.value)
