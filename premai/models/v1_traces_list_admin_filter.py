from enum import Enum


class V1TracesListAdminFilter(str, Enum):
    ADMIN_ONLY = "ADMIN_ONLY"

    def __str__(self) -> str:
        return str(self.value)
