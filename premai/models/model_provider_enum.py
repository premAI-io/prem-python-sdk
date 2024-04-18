from enum import Enum


class ModelProviderEnum(str, Enum):
    ANTHROPIC = "anthropic"
    ANYSCALE = "anyscale"
    AZURE = "azure"
    AZURE_MISTRAL = "azure-mistral"
    CLOUDFLARE = "cloudflare"
    COHERE = "cohere"
    DEEPINFRA = "deepinfra"
    FIREWORKSAI = "fireworksai"
    GROQ = "groq"
    LAMINI = "lamini"
    MISTRALAI = "mistralai"
    OCTOAI = "octoai"
    OPENAI = "openai"
    OPENROUTER = "openrouter"
    PERPLEXITY = "perplexity"
    PREM = "prem"
    REPLICATE = "replicate"
    TOGETHER = "together"

    def __str__(self) -> str:
        return str(self.value)
