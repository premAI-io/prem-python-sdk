from enum import Enum


class ModelProviderEnum(str, Enum):
    ANTHROPIC = "anthropic"
    AZURE = "azure"
    CLOUDFLARE = "cloudflare"
    COHERE = "cohere"
    DEEPINFRA = "deepinfra"
    FIREWORKSAI = "fireworksai"
    LAMINI = "lamini"
    MISTRALAI = "mistralai"
    OCTOAI = "octoai"
    OPENAI = "openai"
    PREM = "prem"
    REPLICATE = "replicate"
    TOGETHER = "together"

    def __str__(self) -> str:
        return str(self.value)
