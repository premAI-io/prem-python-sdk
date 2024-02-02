from enum import Enum


class V1FinetuningRetrieveResponse401Code(str, Enum):
    AUTHENTICATIONERROR = "AuthenticationError"

    def __str__(self) -> str:
        return str(self.value)
