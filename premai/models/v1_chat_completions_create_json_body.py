from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.v1_chat_completions_create_json_body_logit_bias_type_0 import (
    V1ChatCompletionsCreateJsonBodyLogitBiasType0,
)
from ..models.v1_chat_completions_create_json_body_messages_item import V1ChatCompletionsCreateJsonBodyMessagesItem
from ..models.v1_chat_completions_create_json_body_response_format_type_0 import (
    V1ChatCompletionsCreateJsonBodyResponseFormatType0,
)
from ..models.v1_chat_completions_create_json_body_tools_item import V1ChatCompletionsCreateJsonBodyToolsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1ChatCompletionsCreateJsonBody")


class V1ChatCompletionsCreateJsonBodyDict(TypedDict):
    project_id: int
    messages: List["V1ChatCompletionsCreateJsonBodyMessagesItem"]
    model: NotRequired[Union[Unset, str]]
    frequency_penalty: NotRequired[Union[Unset, float]]
    logit_bias: NotRequired[Union["V1ChatCompletionsCreateJsonBodyLogitBiasType0", None, Unset]]
    max_tokens: NotRequired[Union[None, Unset, int]]
    n: NotRequired[Union[Unset, int]]
    presence_penalty: NotRequired[Union[Unset, float]]
    response_format: NotRequired[Union["V1ChatCompletionsCreateJsonBodyResponseFormatType0", None, Unset]]
    seed: NotRequired[Union[None, Unset, int]]
    stop: NotRequired[Union[None, Unset, str]]
    stream: NotRequired[Union[Unset, bool]]
    temperature: NotRequired[Union[None, Unset, float]]
    top_p: NotRequired[Union[None, Unset, float]]
    tools: NotRequired[Union[Unset, List["V1ChatCompletionsCreateJsonBodyToolsItem"]]]
    user: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class V1ChatCompletionsCreateJsonBody:
    """
    Attributes:
        project_id (int): The ID of the project to use.
        messages (List['V1ChatCompletionsCreateJsonBodyMessagesItem']): A list of messages comprising the conversation
            so far.
        model (Union[Unset, str]): ID of the model to use. See the model endpoint compatibility table for details.
        frequency_penalty (Union[Unset, float]): Number between -2.0 and 2.0. Positive values penalize new tokens based
            on their existing frequency.
        logit_bias (Union['V1ChatCompletionsCreateJsonBodyLogitBiasType0', None, Unset]): JSON object that maps tokens
            to an associated bias value from -100 to 100.
        max_tokens (Union[None, Unset, int]): The maximum number of tokens to generate in the chat completion.
        n (Union[Unset, int]): How many chat completion choices to generate for each input message.
        presence_penalty (Union[Unset, float]): Number between -2.0 and 2.0. Positive values penalize new tokens based
            on whether they appear in the text so far.
        response_format (Union['V1ChatCompletionsCreateJsonBodyResponseFormatType0', None, Unset]): An object specifying
            the format that the model must output.
        seed (Union[None, Unset, int]): This feature is in Beta. If specified, our system will make a best effort to
            sample deterministically.
        stop (Union[None, Unset, str]): Up to 4 sequences where the API will stop generating further tokens.
        stream (Union[Unset, bool]): If set, partial message deltas will be sent, like in ChatGPT.
        temperature (Union[None, Unset, float]): What sampling temperature to use, between 0 and 2.
        top_p (Union[None, Unset, float]): An alternative to sampling with temperature, called nucleus sampling.
        tools (Union[Unset, List['V1ChatCompletionsCreateJsonBodyToolsItem']]): A list of tools the model may call.
            Currently, only functions are supported as a tool.
        user (Union[None, Unset, str]): A unique identifier representing your end-user.
    """

    project_id: int
    messages: List["V1ChatCompletionsCreateJsonBodyMessagesItem"]
    model: Union[Unset, str] = UNSET
    frequency_penalty: Union[Unset, float] = UNSET
    logit_bias: Union["V1ChatCompletionsCreateJsonBodyLogitBiasType0", None, Unset] = UNSET
    max_tokens: Union[None, Unset, int] = UNSET
    n: Union[Unset, int] = UNSET
    presence_penalty: Union[Unset, float] = UNSET
    response_format: Union["V1ChatCompletionsCreateJsonBodyResponseFormatType0", None, Unset] = UNSET
    seed: Union[None, Unset, int] = UNSET
    stop: Union[None, Unset, str] = UNSET
    stream: Union[Unset, bool] = UNSET
    temperature: Union[None, Unset, float] = UNSET
    top_p: Union[None, Unset, float] = UNSET
    tools: Union[Unset, List["V1ChatCompletionsCreateJsonBodyToolsItem"]] = UNSET
    user: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.v1_chat_completions_create_json_body_logit_bias_type_0 import (
            V1ChatCompletionsCreateJsonBodyLogitBiasType0,
        )
        from ..models.v1_chat_completions_create_json_body_response_format_type_0 import (
            V1ChatCompletionsCreateJsonBodyResponseFormatType0,
        )

        project_id = self.project_id

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        model = self.model

        frequency_penalty = self.frequency_penalty

        logit_bias: Union[Dict[str, Any], None, Unset]
        if isinstance(self.logit_bias, Unset):
            logit_bias = UNSET
        elif isinstance(self.logit_bias, V1ChatCompletionsCreateJsonBodyLogitBiasType0):
            logit_bias = self.logit_bias.to_dict()
        else:
            logit_bias = self.logit_bias

        max_tokens: Union[None, Unset, int]
        if isinstance(self.max_tokens, Unset):
            max_tokens = UNSET
        else:
            max_tokens = self.max_tokens

        n = self.n

        presence_penalty = self.presence_penalty

        response_format: Union[Dict[str, Any], None, Unset]
        if isinstance(self.response_format, Unset):
            response_format = UNSET
        elif isinstance(self.response_format, V1ChatCompletionsCreateJsonBodyResponseFormatType0):
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
        if model is not UNSET:
            field_dict["model"] = model
        if frequency_penalty is not UNSET:
            field_dict["frequency_penalty"] = frequency_penalty
        if logit_bias is not UNSET:
            field_dict["logit_bias"] = logit_bias
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if n is not UNSET:
            field_dict["n"] = n
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
        from ..models.v1_chat_completions_create_json_body_logit_bias_type_0 import (
            V1ChatCompletionsCreateJsonBodyLogitBiasType0,
        )
        from ..models.v1_chat_completions_create_json_body_messages_item import (
            V1ChatCompletionsCreateJsonBodyMessagesItem,
        )
        from ..models.v1_chat_completions_create_json_body_response_format_type_0 import (
            V1ChatCompletionsCreateJsonBodyResponseFormatType0,
        )
        from ..models.v1_chat_completions_create_json_body_tools_item import V1ChatCompletionsCreateJsonBodyToolsItem

        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = V1ChatCompletionsCreateJsonBodyMessagesItem.from_dict(messages_item_data)

            messages.append(messages_item)

        model = d.pop("model", UNSET)

        frequency_penalty = d.pop("frequency_penalty", UNSET)

        def _parse_logit_bias(data: object) -> Union["V1ChatCompletionsCreateJsonBodyLogitBiasType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logit_bias_type_0 = V1ChatCompletionsCreateJsonBodyLogitBiasType0.from_dict(data)

                return logit_bias_type_0
            except:  # noqa: E722
                pass
            return cast(Union["V1ChatCompletionsCreateJsonBodyLogitBiasType0", None, Unset], data)

        logit_bias = _parse_logit_bias(d.pop("logit_bias", UNSET))

        def _parse_max_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_tokens = _parse_max_tokens(d.pop("max_tokens", UNSET))

        n = d.pop("n", UNSET)

        presence_penalty = d.pop("presence_penalty", UNSET)

        def _parse_response_format(
            data: object,
        ) -> Union["V1ChatCompletionsCreateJsonBodyResponseFormatType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_format_type_0 = V1ChatCompletionsCreateJsonBodyResponseFormatType0.from_dict(data)

                return response_format_type_0
            except:  # noqa: E722
                pass
            return cast(Union["V1ChatCompletionsCreateJsonBodyResponseFormatType0", None, Unset], data)

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
            tools_item = V1ChatCompletionsCreateJsonBodyToolsItem.from_dict(tools_item_data)

            tools.append(tools_item)

        def _parse_user(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user = _parse_user(d.pop("user", UNSET))

        v1_chat_completions_create_json_body = cls(
            project_id=project_id,
            messages=messages,
            model=model,
            frequency_penalty=frequency_penalty,
            logit_bias=logit_bias,
            max_tokens=max_tokens,
            n=n,
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

        v1_chat_completions_create_json_body.additional_properties = d
        return v1_chat_completions_create_json_body

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
