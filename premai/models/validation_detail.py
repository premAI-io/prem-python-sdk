from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.validation_detail_error_messages_item import ValidationDetailErrorMessagesItem

T = TypeVar("T", bound="ValidationDetail")


class ValidationDetailDict(TypedDict):
    error_messages: List["ValidationDetailErrorMessagesItem"]
    pass


@_attrs_define
class ValidationDetail:
    """
    Attributes:
        error_messages (List['ValidationDetailErrorMessagesItem']): Error messages for the field.
    """

    error_messages: List["ValidationDetailErrorMessagesItem"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_messages = []
        for error_messages_item_data in self.error_messages:
            error_messages_item = error_messages_item_data.to_dict()
            error_messages.append(error_messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error_messages": error_messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_detail_error_messages_item import ValidationDetailErrorMessagesItem

        d = src_dict.copy() if src_dict else {}
        error_messages = []
        _error_messages = d.pop("error_messages")
        for error_messages_item_data in _error_messages:
            error_messages_item = ValidationDetailErrorMessagesItem.from_dict(error_messages_item_data)

            error_messages.append(error_messages_item)

        validation_detail = cls(
            error_messages=error_messages,
        )

        validation_detail.additional_properties = d
        return validation_detail

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
