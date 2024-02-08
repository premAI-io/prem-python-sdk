from enum import Enum


class RateLimitErrorCode(str, Enum):
    RATELIMITERROR = "RateLimitError"

    def __str__(self) -> str:
        return str(self.value)
