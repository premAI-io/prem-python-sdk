from enum import Enum


class AuthenticationErrorCodeEnum(str, Enum):
    AUTHENTICATIONERROR = "AuthenticationError"

    def __str__(self) -> str:
        return str(self.value)
