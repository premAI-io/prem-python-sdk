from enum import Enum


class DocumentTypeEnum(str, Enum):
    DOCX = "docx"
    PDF = "pdf"
    TXT = "txt"

    def __str__(self) -> str:
        return str(self.value)
