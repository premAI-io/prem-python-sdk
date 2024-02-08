from enum import Enum


class AuthenticationErrorCode(str, Enum):
    AUTHENTICATIONERROR = "AuthenticationError"

    def __str__(self) -> str:
        return str(self.value)
