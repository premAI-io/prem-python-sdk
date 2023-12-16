from typing import List, Optional

from pydantic import BaseModel


class Usage(BaseModel):
    """
    Represents token usage information in an embeddings response.

    Attributes:

    - prompt_tokens (int): The number of tokens used in the prompt.
    - total_tokens (int): The total number of tokens used.
    """

    prompt_tokens: int
    total_tokens: int


class EmbeddingsResponse(BaseModel):
    """
    Represents the response of an embeddings request.

    Attributes:

    - data (List[List[float]]): The list of embeddings data.
    - model (str): The model used for generating embeddings.
    - usage (Optional[Usage]): Token usage information (optional).
    - provider_name (str): The name of the provider.
    - provider_id (str): The identifier of the provider.
    """

    data: List[List[float]]
    model: str
    usage: Optional[Usage]
    provider_name: str
    provider_id: str
