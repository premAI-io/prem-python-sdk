from enum import Enum


class CatchAllErrorCodeEnum(str, Enum):
    CATCHALLERROR = "CatchAllError"

    def __str__(self) -> str:
        return str(self.value)
