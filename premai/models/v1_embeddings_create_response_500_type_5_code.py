from enum import Enum


class V1EmbeddingsCreateResponse500Type5Code(str, Enum):
    CATCHALLERROR = "CatchAllError"

    def __str__(self) -> str:
        return str(self.value)
