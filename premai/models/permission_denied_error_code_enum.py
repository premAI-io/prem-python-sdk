from enum import Enum


class PermissionDeniedErrorCodeEnum(str, Enum):
    PERMISSIONDENIEDERROR = "PermissionDeniedError"

    def __str__(self) -> str:
        return str(self.value)
