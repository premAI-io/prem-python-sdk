from enum import Enum


class StatusD09Enum(str, Enum):
    DONE = "done"
    FAILED = "failed"
    FINETUNING = "finetuning"
    QUEUED = "queued"

    def __str__(self) -> str:
        return str(self.value)
