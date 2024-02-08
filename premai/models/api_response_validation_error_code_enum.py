from enum import Enum


class APIResponseValidationErrorCodeEnum(str, Enum):
    APIRESPONSEVALIDATIONERROR = "APIResponseValidationError"

    def __str__(self) -> str:
        return str(self.value)
