from typing import Dict, Union , List, Type, TypeVar
from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, Unpack
import re
import httpx
import json

from ...models.v1_chat_completions_create_json_body import V1ChatCompletionsCreateJsonBody
from ...models.v1_chat_completions_create_response_200 import V1ChatCompletionsCreateResponse200, V1ChatCompletionsCreateResponse200ChoicesItem
from ...models.v1_chat_completions_create_response_200_usage import V1ChatCompletionsCreateResponse200Usage
from ...types import UNSET, Unset

T = TypeVar("T", bound="V1ChatCompletionsCreateResponse200ChoicesItem")


def _get_kwargs(
    **body: Unpack[V1ChatCompletionsCreateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/chat/completions",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def v1_chat_completions_create_wrapper(client):
    def v1_chat_completions_create_wrapped(
        **body: Unpack[V1ChatCompletionsCreateJsonBody],
    ) -> Union[V1ChatCompletionsCreateResponse200, V1ChatCompletionsCreateResponse200StreamContainer]:
        """Creates a model response for the given chat conversation.

        Args:
            body (V1ChatCompletionsCreateJsonBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Union[V1ChatCompletionsCreateResponse200, V1ChatCompletionsCreateResponse200StreamContainer]
        """
        kwargs = _get_kwargs(
            **body,
        )
        httpx_client = client.get_httpx_client()
        if ('stream' in body) and (body['stream']):
            stream = httpx_client.stream(**kwargs)
            return V1ChatCompletionsCreateResponse200StreamContainer(stream)
        else:
            response = httpx_client.request(
                **kwargs,
            )
            return V1ChatCompletionsCreateResponse200.from_dict(response.json())
    return v1_chat_completions_create_wrapped


END_STREAM = 'done'
class V1ChatCompletionsCreateResponse200StreamContainer:
    _pattern = '(?<={key}: )(.*)'
    trace_id: str = None

    def __init__(self, stream: httpx.Response):  
        self._stream = stream

    def _parse_data(self, text: str):
        match = re.search(self._pattern.format(key='data'), text)
        if match:
            data = json.loads(match.group(1))
            parsed_data: V1ChatCompletionsCreateResponse200Stream = V1ChatCompletionsCreateResponse200Stream.from_dict(data)
            return parsed_data
        else:   return None

    def _parse_event(self, text: str):
        match = re.search(self._pattern.format(key='event'), text)
        if match: return match.group(1)
        else:   return None

    def _parse_trace_id(self, text: str):
        match = re.search(self._pattern.format(key='trace_id'), text)
        if match: return match.group(1)
        else:   return None
    
    def __iter__(self):
        def generator():
            with self._stream as stream:
                for text in stream.iter_text():
                    event = self._parse_event(text)
                    self.trace_id = self._parse_trace_id(text)
                    if event == END_STREAM:
                        break
                    data = self._parse_data(text)

                    yield data
        return generator()
    

@_attrs_define
class V1ChatCompletionsCreateResponse200Stream:
    """
    Attributes:
        id (str): A unique identifier for the chat completion. Each chunk has the same ID.
        choices (List['V1ChatCompletionsCreateResponse200ChoicesItem']): A list of chat completion choices. Can be more
            than one if n is greater than 1.
        created (int): The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same
            timestamp.
        model (str): The model to generate the completion.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        usage (Union[Unset, V1ChatCompletionsCreateResponse200Usage]): The usage statistics for the completion.
    """

    id: str
    choices: List["V1ChatCompletionsCreateResponse200ChoicesItemStream"]
    created: int
    model: str
    usage: Union[Unset, "V1ChatCompletionsCreateResponse200Usage"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        created = self.created

        model = self.model
        

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "choices": choices,
                "created": created,
                "model": model,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()
        id = d.pop("id")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = V1ChatCompletionsCreateResponse200ChoicesItemStream.from_dict(choices_item_data)

            choices.append(choices_item)

        created = d.pop("created")

        model = d.pop("model")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, V1ChatCompletionsCreateResponse200Usage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = V1ChatCompletionsCreateResponse200Usage.from_dict(_usage)

        v1_chat_completions_create_response_200 = cls(
            id=id,
            choices=choices,
            created=created,
            model=model,
            usage=usage,
        )

        v1_chat_completions_create_response_200.additional_properties = d
        return v1_chat_completions_create_response_200

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


@_attrs_define
class V1ChatCompletionsCreateResponse200ChoicesItemStream:
    """
    Attributes:
        message (str): The generated message in the chat completion choice.
        finish_reason (str): The reason the chat completion finished, e.g., 'stop' or 'length'.
    """

    delta: str
    finish_reason: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delta = self.delta

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delta": delta,
                "finish_reason": finish_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delta = d.pop("delta")

        finish_reason = d.pop("finish_reason")

        v1_chat_completions_create_response_200_choices_item = cls(
            delta=delta,
            finish_reason=finish_reason,
        )

        v1_chat_completions_create_response_200_choices_item.additional_properties = d
        return v1_chat_completions_create_response_200_choices_item

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