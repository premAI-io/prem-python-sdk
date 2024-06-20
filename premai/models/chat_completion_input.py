import json
from typing import Dict, List, Tuple, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.enhancement import Enhancement
from ..models.message import Message
from ..models.tool import Tool
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionInput")


class ChatCompletionInputDict(TypedDict):
    project_id: int
    messages: List["Message"]
    session_id: NotRequired[Union[Unset, str]]
    repositories: NotRequired[Union[Unset, Enhancement]]
    model: NotRequired[Union[Unset, str]]
    system_prompt: NotRequired[Union[Unset, str]]
    max_tokens: NotRequired[Union[None, Unset, int]]
    stream: NotRequired[Union[Unset, bool]]
    temperature: Union[Unset, float] = 1.0
    tools: NotRequired[Union[List["Tool"], None, Unset]]
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
        max_tokens (Union[None, Unset, int]): The maximum number of tokens to generate in the chat completion.
        stream (Union[Unset, bool]): If set, partial message deltas will be sent, like in ChatGPT.
        temperature (Union[Unset, float]): What sampling temperature to use, between 0 and 2. Default: 1.0.
        tools (Union[List['Tool'], None, Unset]): The tools to use in the completion.
    """

    project_id: int
    messages: List["Message"]
    session_id: Union[Unset, str] = UNSET
    repositories: Union[Unset, "Enhancement"] = UNSET
    model: Union[Unset, str] = UNSET
    system_prompt: Union[Unset, str] = UNSET
    max_tokens: Union[None, Unset, int] = UNSET
    stream: Union[Unset, bool] = UNSET
    temperature: Union[Unset, float] = 1.0
    tools: Union[List["Tool"], None, Unset] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
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

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        stream = self.stream

        temperature = self.temperature

        tools: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            tools = []
            for tools_type_0_item_data in self.tools:
                tools_type_0_item = tools_type_0_item_data.to_dict()
                tools.append(tools_type_0_item)

        else:
            tools = self.tools

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
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if tools is not UNSET:
            field_dict["tools"] = tools

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

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        stream = self.stream if isinstance(self.stream, Unset) else (None, str(self.stream).encode(), "text/plain")

        temperature = (
            self.temperature
            if isinstance(self.temperature, Unset)
            else (None, str(self.temperature).encode(), "text/plain")
        )

        tools: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.tools, Unset):
            tools = UNSET
        elif isinstance(self.tools, list):
            _temp_tools = []
            for tools_type_0_item_data in self.tools:
                tools_type_0_item = tools_type_0_item_data.to_dict()
                _temp_tools.append(tools_type_0_item)
            tools = (None, json.dumps(_temp_tools).encode(), "application/json")

        else:
            tools = self.tools

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
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if stream is not UNSET:
            field_dict["stream"] = stream
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if tools is not UNSET:
            field_dict["tools"] = tools

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.enhancement import Enhancement
        from ..models.message import Message
        from ..models.tool import Tool

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

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        stream = d.pop("stream", UNSET)

        temperature = d.pop("temperature", UNSET)

        def _parse_tools(data: object) -> Union[List["Tool"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tools_type_0 = []
                _tools_type_0 = data
                for tools_type_0_item_data in _tools_type_0:
                    tools_type_0_item = Tool.from_dict(tools_type_0_item_data)

                    tools_type_0.append(tools_type_0_item)

                return tools_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["Tool"], None, Unset], data)

        tools = _parse_tools(d.pop("tools", UNSET))

        chat_completion_input = cls(
            project_id=project_id,
            messages=messages,
            session_id=session_id,
            repositories=repositories,
            model=model,
            system_prompt=system_prompt,
            max_tokens=max_tokens,
            stream=stream,
            temperature=temperature,
            tools=tools,
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
