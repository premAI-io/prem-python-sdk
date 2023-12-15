from typing import List, Optional

from pydantic import BaseModel


class Usage(BaseModel):
    prompt_tokens: int
    total_tokens: int


class EmbeddingsResponse(BaseModel):
    data: List[List[float]]
    model: str
    usage: Optional[Usage]
    provider_name: str
    provider_id: str
