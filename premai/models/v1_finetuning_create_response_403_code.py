from enum import Enum


class V1FinetuningCreateResponse403Code(str, Enum):
    PERMISSIONDENIEDERROR = "PermissionDeniedError"

    def __str__(self) -> str:
        return str(self.value)
