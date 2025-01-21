from enum import Enum


class MessageContentType1ItemType(str, Enum):
    IMAGE_URL = "image_url"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
