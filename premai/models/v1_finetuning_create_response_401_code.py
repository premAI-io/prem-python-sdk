from enum import Enum


class V1FinetuningCreateResponse401Code(str, Enum):
    AUTHENTICATIONERROR = "AuthenticationError"

    def __str__(self) -> str:
        return str(self.value)
