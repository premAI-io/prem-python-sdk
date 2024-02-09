from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="V1ChatCompletionsCreateResponse200ChoicesItem")


class V1ChatCompletionsCreateResponse200ChoicesItemDict(TypedDict):
    message: str
    finish_reason: str
    pass


@_attrs_define
class V1ChatCompletionsCreateResponse200ChoicesItem:
    """
    Attributes:
        message (str): The generated message in the chat completion choice.
        finish_reason (str): The reason the chat completion finished, e.g., 'stop' or 'length'.
    """

    message: str
    finish_reason: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "finish_reason": finish_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        message = d.pop("message")

        finish_reason = d.pop("finish_reason")

        v1_chat_completions_create_response_200_choices_item = cls(
            message=message,
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