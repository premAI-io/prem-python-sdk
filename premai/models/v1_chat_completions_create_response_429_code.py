from enum import Enum


class V1ChatCompletionsCreateResponse429Code(str, Enum):
    RATELIMITERROR = "RateLimitError"

    def __str__(self) -> str:
        return str(self.value)
