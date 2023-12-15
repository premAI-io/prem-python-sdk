from typing import List, Optional

from pydantic import BaseModel


class Message(BaseModel):
    content: str
    role: str


class Choice(BaseModel):
    finish_reason: str
    index: int
    message: Message


class Usage(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int


class ChatCompletionResponse(BaseModel):
    id: str
    choices: List[Choice]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: Optional[Usage]


class Delta(BaseModel):
    content: Optional[str]
    role: Optional[str]


class Choices(BaseModel):
    delta: Delta
    finish_reason: Optional[str]


class ChatCompletionChunk(BaseModel):
    id: str
    model: str
    object: str
    created: int
    choices: List[Choices]
