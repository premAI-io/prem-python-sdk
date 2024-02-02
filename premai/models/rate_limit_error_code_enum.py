from enum import Enum


class RateLimitErrorCodeEnum(str, Enum):
    RATELIMITERROR = "RateLimitError"

    def __str__(self) -> str:
        return str(self.value)
