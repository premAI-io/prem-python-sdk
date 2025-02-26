from enum import Enum


class ModelProviderEnum(str, Enum):
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    GROQ = "groq"
    OPENAI = "openai"
    PREM = "prem"
    PROXY_PREM_AI = "proxy-prem-ai"

    def __str__(self) -> str:
        return str(self.value)
