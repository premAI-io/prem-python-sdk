from __future__ import annotations

from typing import Dict, List, Optional, Union

from pydantic import BaseModel

from ..resource import SyncAPIResource
from ..utils import filter_none_values, required_args


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


class Completions(SyncAPIResource):
    def __init__(self, client) -> None:
        """
        Initializes the Completions resource.

        Parameters:
        - client (PremAI): The client for making API requests.
        """
        super().__init__(client)

    @required_args(["project_id", "messages"])
    def create(
        self,
        project_id: int,
        messages: List[Dict[str, Union[str, int]]],
        model: Optional[str] = None,
        frequency_penalty: Optional[float] = None,
        logit_bias: Optional[Dict[str, int]] = {},
        max_tokens: Optional[int] = None,
        n: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        response_format: Optional[Dict[str, Union[str, int]]] = None,
        seed: Optional[int] = None,
        stop: Union[Optional[str], List[str]] = None,
        temperature: Optional[float] = None,
        tool_choice: Optional[Dict[str, Union[str, int]]] = None,
        tools: Optional[List[Dict[str, Union[str, int]]]] = None,
        top_p: Optional[float] = None,
        user: Optional[str] = None,
    ) -> Dict[str, Union[str, int]]:
        body = {
            "project_id": project_id,
            "messages": messages,
            "model": model,
            "frequency_penalty": frequency_penalty,
            "logit_bias": logit_bias,
            "max_tokens": max_tokens,
            "n": n,
            "presence_penalty": presence_penalty,
            "response_format": response_format,
            "seed": seed,
            "stop": stop,
            "temperature": temperature,
            "tool_choice": tool_choice,
            "tools": tools,
            "top_p": top_p,
            "user": user,
        }
        response = self._post(
            "v1/chat/completions",
            body=filter_none_values(body),
        )
        return ChatCompletionResponse(**response)
