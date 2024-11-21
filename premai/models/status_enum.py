from enum import Enum


class StatusEnum(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    INDEXING = "INDEXING"
    PENDING = "PENDING"
    UPLOADED = "UPLOADED"

    def __str__(self) -> str:
        return str(self.value)
