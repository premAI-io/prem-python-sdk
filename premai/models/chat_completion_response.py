from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.chat_completion_response_choices_item import ChatCompletionResponseChoicesItem
from ..models.chat_completion_response_usage import ChatCompletionResponseUsage
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionResponse")


class ChatCompletionResponseDict(TypedDict):
    id: str
    choices: List["ChatCompletionResponseChoicesItem"]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: NotRequired[Union[Unset, ChatCompletionResponseUsage]]
    pass


@_attrs_define
class ChatCompletionResponse:
    """
    Attributes:
        id (str): A unique identifier for the chat completion. Each chunk has the same ID.
        choices (List['ChatCompletionResponseChoicesItem']): A list of chat completion choices. Can be more than one if
            n is greater than 1.
        created (int): The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same
            timestamp.
        model (str): The model to generate the completion.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        usage (Union[Unset, ChatCompletionResponseUsage]): The usage statistics for the completion.
    """

    id: str
    choices: List["ChatCompletionResponseChoicesItem"]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: Union[Unset, "ChatCompletionResponseUsage"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        created = self.created

        model = self.model

        provider_name = self.provider_name

        provider_id = self.provider_id

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
                "provider_name": provider_name,
                "provider_id": provider_id,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_response_choices_item import ChatCompletionResponseChoicesItem
        from ..models.chat_completion_response_usage import ChatCompletionResponseUsage

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = ChatCompletionResponseChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        created = d.pop("created")

        model = d.pop("model")

        provider_name = d.pop("provider_name")

        provider_id = d.pop("provider_id")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ChatCompletionResponseUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ChatCompletionResponseUsage.from_dict(_usage)

        chat_completion_response = cls(
            id=id,
            choices=choices,
            created=created,
            model=model,
            provider_name=provider_name,
            provider_id=provider_id,
            usage=usage,
        )

        chat_completion_response.additional_properties = d
        return chat_completion_response

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
