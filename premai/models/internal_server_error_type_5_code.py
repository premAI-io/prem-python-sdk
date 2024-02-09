from enum import Enum


class InternalServerErrorType5Code(str, Enum):
    CATCHALLERROR = "CatchAllError"

    def __str__(self) -> str:
        return str(self.value)
