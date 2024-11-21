from enum import Enum


class ModelProviderEnum(str, Enum):
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    GROQ = "groq"
    OPENAI = "openai"
    PREM = "prem"

    def __str__(self) -> str:
        return str(self.value)
