from __future__ import annotations

from typing import Dict, List, Optional, Union

from ...resource import SyncAPIResource
from ...utils import filter_none_values, required_args
from .models import ChatCompletionChunk, ChatCompletionResponse


class Completions(SyncAPIResource):
    def __init__(self, client) -> None:
        """
        Initializes the Completions resource.

        Parameters:

        - client (Prem): The client for making API requests.
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
        stream: Optional[bool] = False,
    ) -> Union[ChatCompletionResponse, List[ChatCompletionChunk]]:
        """
        Create chat completions based on the provided parameters.

        Parameters:

        - project_id (int): The ID of the project.
        - messages (List[Dict[str, Union[str, int]]]): A list of messages containing user and/or assistant inputs.
        - model (Optional[str]): The language model to use for generating completions.
        - frequency_penalty (Optional[float]): The frequency penalty to be applied during generation.
        - logit_bias (Optional[Dict[str, int]]): Logit bias to influence the model's behavior.
        - max_tokens (Optional[int]): The maximum number of tokens in the generated completions.
        - n (Optional[int]): The number of completions to generate.
        - presence_penalty (Optional[float]): The presence penalty to be applied during generation.
        - response_format (Optional[Dict[str, Union[str, int]]]): The format of the generated completion response.
        - seed (Optional[int]): The seed to control randomness during generation.
        - stop (Union[Optional[str], List[str]]): Stop criteria for generation.
        - temperature (Optional[float]): The temperature parameter to control randomness in generation.
        - tool_choice (Optional[Dict[str, Union[str, int]]]): The tool choice to be used during generation.
        - tools (Optional[List[Dict[str, Union[str, int]]]]): List of tools to be used during generation.
        - top_p (Optional[float]): Top-p sampling parameter for generation.
        - user (Optional[str]): The user identifier.
        - stream (Optional[bool]): If True, return results as a stream.

        Returns:

        - Union[ChatCompletionResponse, List[ChatCompletionChunk]]: The generated chat completion response
          or a list of chat completion chunks.
        """
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
            "stream": stream,
        }
        response = self._post(
            "v1/chat/completions",
            body=filter_none_values(body),
            stream=stream,
        )
        if not stream:
            return ChatCompletionResponse(**response)
        else:
            return [ChatCompletionChunk(**event) for event in response]
