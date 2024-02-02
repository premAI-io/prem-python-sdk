from enum import Enum


class CatchAllErrorCode(str, Enum):
    CATCHALLERROR = "CatchAllError"

    def __str__(self) -> str:
        return str(self.value)
