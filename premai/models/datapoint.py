from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.messages import Messages

T = TypeVar("T", bound="Datapoint")


class DatapointDict(TypedDict):
    messages: List["Messages"]
    pass


@_attrs_define
class Datapoint:
    """
    Attributes:
        messages (List['Messages']):
    """

    messages: List["Messages"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages import Messages

        d = src_dict.copy() if src_dict else {}
        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = Messages.from_dict(messages_item_data)

            messages.append(messages_item)

        datapoint = cls(
            messages=messages,
        )

        datapoint.additional_properties = d
        return datapoint

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
