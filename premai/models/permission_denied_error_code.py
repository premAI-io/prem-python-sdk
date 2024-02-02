from enum import Enum


class PermissionDeniedErrorCode(str, Enum):
    PERMISSIONDENIEDERROR = "PermissionDeniedError"

    def __str__(self) -> str:
        return str(self.value)
