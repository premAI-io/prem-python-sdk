from enum import Enum


class StatusEnum(str, Enum):
    CHUNKING = "CHUNKING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PARSING = "PARSING"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    UPLOADED = "UPLOADED"
    WAITING_FOR_CHUNKS_COMPLETION = "WAITING_FOR_CHUNKS_COMPLETION"

    def __str__(self) -> str:
        return str(self.value)
