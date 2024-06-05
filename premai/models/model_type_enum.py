from enum import Enum


class ModelTypeEnum(str, Enum):
    AUTOPILOT = "autopilot"
    TEXT2IMAGE = "text2image"
    TEXT2TEXT = "text2text"
    TEXT2VECTOR = "text2vector"

    def __str__(self) -> str:
        return str(self.value)
