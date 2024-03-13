import json
from typing import Dict, List, Tuple, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.chat_completion_input_logit_bias_type_0 import ChatCompletionInputLogitBiasType0
from ..models.chat_completion_input_response_format_type_0 import ChatCompletionInputResponseFormatType0
from ..models.chat_completion_input_tools_item import ChatCompletionInputToolsItem
from ..models.enhancement import Enhancement
from ..models.message import Message
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionInput")


class ChatCompletionInputDict(TypedDict):
    project_id: int
    messages: List["Message"]
    session_id: NotRequired[Union[Unset, str]]
    repositories: NotRequired[Union[Unset, Enhancement]]
    model: NotRequired[Union[Unset, str]]
    system_prompt: NotRequired[Union[Unset, str]]
    frequency_penalty: NotRequired[Union[Unset, float]]
    logit_bias: NotRequired[Union["ChatCompletionInputLogitBiasType0", None, Unset]]
    max_tokens: NotRequired[Union[None, Unset, int]]
    presence_penalty: NotRequired[Union[Unset, float]]
    response_format: NotRequired[Union["ChatCompletionInputResponseFormatType0", None, Unset]]
    seed: NotRequired[Union[None, Unset, int]]
    stop: NotRequired[Union[None, Unset, str]]
    stream: NotRequired[Union[Unset, bool]]
    temperature: NotRequired[Union[None, Unset, float]]
    top_p: NotRequired[Union[None, Unset, float]]
    tools: NotRequired[Union[Unset, List["ChatCompletionInputToolsItem"]]]
    user: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class ChatCompletionInput:
    """
    Attributes:
        project_id (int): The ID of the project to use.
        messages (List['Message']): A list of messages comprising the conversation so far.
        session_id (Union[Unset, str]): The ID of the session to use. It helps to track the chat history.
        repositories (Union[Unset, Enhancement]):
        model (Union[Unset, str]): ID of the model to use. See the model endpoint compatibility table for details.
        system_prompt (Union[Unset, str]): The system prompt to use.
        frequency_penalty (Union[Unset, float]): Number between -2.0 and 2.0. Positive values penalize new tokens based
            on their existing frequency.
        logit_bias (Union['ChatCompletionInputLogitBiasType0', None, Unset]): JSON object that maps tokens to an
            associated bias value from -100 to 100.
        max_tokens (Union[None, Unset, int]): The maximum number of tokens to generate in the chat completion.
        presence_penalty (Union[Unset, float]): Number between -2.0 and 2.0. Positive values penalize new tokens based
            on whether they appear in the text so far.
        response_format (Union['ChatCompletionInputResponseFormatType0', None, Unset]): An object specifying the format
            that the model must output.
        seed (Union[None, Unset, int]): This feature is in Beta. If specified, our system will make a best effort to
            sample deterministically.
        stop (Union[None, Unset, str]): Up to 4 sequences where the API will stop generating further tokens.
        stream (Union[Unset, bool]): If set, partial message deltas will be sent, like in ChatGPT.
        temperature (Union[None, Unset, float]): What sampling temperature to use, between 0 and 2.
        top_p (Union[None, Unset, float]): An alternative to sampling with temperature, called nucleus sampling.
        tools (Union[Unset, List['ChatCompletionInputToolsItem']]): A list of tools the model may call. Currently, only
            functions are supported as a tool.
        user (Union[None, Unset, str]): A unique identifier representing your end-user.
    """

    project_id: int
    messages: List["Message"]
    session_id: Union[Unset, str] = UNSET
    repositories: Union[Unset, "Enhancement"] = UNSET
    model: Union[Unset, str] = UNSET
    system_prompt: Union[Unset, str] = UNSET
    frequency_penalty: Union[Unset, float] = UNSET
    logit_bias: Union["ChatCompletionInputLogitBiasType0", None, Unset] = UNSET
    max_tokens: Union[None, Unset, int] = UNSET
    presence_penalty: Union[Unset, float] = UNSET
    response_format: Union["ChatCompletionInputResponseFormatType0", None, Unset] = UNSET
    seed: Union[None, Unset, int] = UNSET
    stop: Union[None, Unset, str] = UNSET
    stream: Union[Unset, bool] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    top_p: Union[None, Unset, float] = UNSET
    tools: Union[Unset, List["ChatCompletionInputToolsItem"]] = UNSET
    user: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.chat_completion_input_logit_bias_type_0 import ChatCompletionInputLogitBiasType0
        from ..models.chat_completion_input_response_format_type_0 import ChatCompletionInputResponseFormatType0

        project_id = self.project_id

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        session_id = self.session_id

        repositories: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = self.repositories.to_dict()

        model = self.model

        system_prompt = self.system_prompt

        frequency_penalty = self.frequency_penalty

        logit_bias: Union[Dict[str, Any], None, Unset]
        if isinstance(self.logit_bias, Unset):
            logit_bias = UNSET
        elif isinstance(self.logit_bias, ChatCompletionInputLogitBiasType0):
            logit_bias = self.logit_bias.to_dict()
        else:
            logit_bias = self.logit_bias

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        presence_penalty = self.presence_penalty

        response_format: Union[Dict[str, Any], None, Unset]
        if isinstance(self.response_format, Unset):
            response_format = UNSET
        elif isinstance(self.response_format, ChatCompletionInputResponseFormatType0):
            response_format = self.response_format.to_dict()
        else:
            response_format = self.response_format

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        stop: Union[None, Unset, str]
        if isinstance(self.stop, Unset):
            stop = UNSET
        else:
            stop = self.stop

        stream = self.stream

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: Union[None, Unset, float]
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        tools: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
            tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                tools.append(tools_item)

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "messages": messages,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if model is not UNSET:
            field_dict["model"] = model
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if frequency_penalty is not UNSET:
            field_dict["frequency_penalty"] = frequency_penalty
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if presence_penalty is not UNSET:
            field_dict["presence_penalty"] = presence_penalty
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if seed is not UNSET:
            field_dict["seed"] = seed
        if stop is not UNSET:
            field_dict["stop"] = stop
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if tools is not UNSET:
            field_dict["tools"] = tools
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        project_id = (
            self.project_id
            if isinstance(self.project_id, Unset)
            else (None, str(self.project_id).encode(), "text/plain")
        )

        _temp_messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            _temp_messages.append(messages_item)
        messages = (None, json.dumps(_temp_messages).encode(), "application/json")

        session_id = (
            self.session_id
            if isinstance(self.session_id, Unset)
            else (None, str(self.session_id).encode(), "text/plain")
        )

        repositories: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.repositories, Unset):
            repositories = (None, json.dumps(self.repositories.to_dict()).encode(), "application/json")

        model = self.model if isinstance(self.model, Unset) else (None, str(self.model).encode(), "text/plain")

        system_prompt = (
            self.system_prompt
            if isinstance(self.system_prompt, Unset)
            else (None, str(self.system_prompt).encode(), "text/plain")
        )

        frequency_penalty = (
            self.frequency_penalty
            if isinstance(self.frequency_penalty, Unset)
            else (None, str(self.frequency_penalty).encode(), "text/plain")
        )

        logit_bias: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.logit_bias, Unset):
            logit_bias = UNSET
        elif isinstance(self.logit_bias, ChatCompletionInputLogitBiasType0):
            logit_bias = (None, json.dumps(self.logit_bias.to_dict()).encode(), "application/json")
        else:
            logit_bias = self.logit_bias

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        presence_penalty = (
            self.presence_penalty
            if isinstance(self.presence_penalty, Unset)
            else (None, str(self.presence_penalty).encode(), "text/plain")
        )

        response_format: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.response_format, Unset):
            response_format = UNSET
        elif isinstance(self.response_format, ChatCompletionInputResponseFormatType0):
            response_format = (None, json.dumps(self.response_format.to_dict()).encode(), "application/json")
        else:
            response_format = self.response_format

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        stop: Union[None, Unset, str]
        if isinstance(self.stop, Unset):
            stop = UNSET
        else:
            stop = self.stop

        stream = self.stream if isinstance(self.stream, Unset) else (None, str(self.stream).encode(), "text/plain")

        temperature: Union[None, Unset, float]
        if isinstance(self.temperature, Unset):
            temperature = UNSET
        else:
            temperature = self.temperature

        top_p: Union[None, Unset, float]
        if isinstance(self.top_p, Unset):
            top_p = UNSET
        else:
            top_p = self.top_p

        tools: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.tools, Unset):
            _temp_tools = []
            for tools_item_data in self.tools:
                tools_item = tools_item_data.to_dict()
                _temp_tools.append(tools_item)
            tools = (None, json.dumps(_temp_tools).encode(), "application/json")

        user: Union[None, Unset, str]
        if isinstance(self.user, Unset):
            user = UNSET
        else:
            user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "project_id": project_id,
                "messages": messages,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if model is not UNSET:
            field_dict["model"] = model
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if frequency_penalty is not UNSET:
            field_dict["frequency_penalty"] = frequency_penalty
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if presence_penalty is not UNSET:
            field_dict["presence_penalty"] = presence_penalty
        if response_format is not UNSET:
            field_dict["response_format"] = response_format
        if seed is not UNSET:
            field_dict["seed"] = seed
        if stop is not UNSET:
            field_dict["stop"] = stop
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p
        if tools is not UNSET:
            field_dict["tools"] = tools
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_input_logit_bias_type_0 import ChatCompletionInputLogitBiasType0
        from ..models.chat_completion_input_response_format_type_0 import ChatCompletionInputResponseFormatType0
        from ..models.chat_completion_input_tools_item import ChatCompletionInputToolsItem
        from ..models.enhancement import Enhancement
        from ..models.message import Message

        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Message.from_dict(messages_item_data)

            messages.append(messages_item)

        session_id = d.pop("session_id", UNSET)

        _repositories = d.pop("repositories", UNSET)
        repositories: Union[Unset, Enhancement]
        if isinstance(_repositories, Unset):
            repositories = UNSET
        else:
            repositories = Enhancement.from_dict(_repositories)

        model = d.pop("model", UNSET)

        system_prompt = d.pop("system_prompt", UNSET)

        frequency_penalty = d.pop("frequency_penalty", UNSET)

        def _parse_logit_bias(data: object) -> Union["ChatCompletionInputLogitBiasType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logit_bias_type_0 = ChatCompletionInputLogitBiasType0.from_dict(data)

                return logit_bias_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChatCompletionInputLogitBiasType0", None, Unset], data)

        logit_bias = _parse_logit_bias(d.pop("logit_bias", UNSET))

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        presence_penalty = d.pop("presence_penalty", UNSET)

        def _parse_response_format(data: object) -> Union["ChatCompletionInputResponseFormatType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_type_0 = ChatCompletionInputResponseFormatType0.from_dict(data)

                return response_format_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChatCompletionInputResponseFormatType0", None, Unset], data)

        response_format = _parse_response_format(d.pop("response_format", UNSET))

        def _parse_seed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_stop(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stop = _parse_stop(d.pop("stop", UNSET))

        stream = d.pop("stream", UNSET)

        def _parse_temperature(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature = _parse_temperature(d.pop("temperature", UNSET))

        def _parse_top_p(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        top_p = _parse_top_p(d.pop("top_p", UNSET))

        tools = []
        _tools = d.pop("tools", UNSET)
        for tools_item_data in _tools or []:
            tools_item = ChatCompletionInputToolsItem.from_dict(tools_item_data)

            tools.append(tools_item)

        def _parse_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        chat_completion_input = cls(
            project_id=project_id,
            messages=messages,
            session_id=session_id,
            repositories=repositories,
            model=model,
            system_prompt=system_prompt,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            max_tokens=max_tokens,
            presence_penalty=presence_penalty,
            response_format=response_format,
            seed=seed,
            stop=stop,
            stream=stream,
            temperature=temperature,
            top_p=top_p,
            tools=tools,
            user=user,
        )

        chat_completion_input.additional_properties = d
        return chat_completion_input

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
