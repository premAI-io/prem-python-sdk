from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.message import Message

T = TypeVar("T", bound="ResponseChoice")


class ResponseChoiceDict(TypedDict):
    index: int
    message: "Message"
    finish_reason: str
    pass


@_attrs_define
class ResponseChoice:
    """
    Attributes:
        index (int): The index of the choice in the list of choices.
        message (Message):
        finish_reason (str): The reason the chat completion finished, e.g., 'stop' or 'length'.
    """

    index: int
    message: "Message"
    finish_reason: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        message = self.message.to_dict()

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "message": message,
                "finish_reason": finish_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message

        d = src_dict.copy() if src_dict else {}
        index = d.pop("index")

        message = Message.from_dict(d.pop("message"))

        finish_reason = d.pop("finish_reason")

        response_choice = cls(
            index=index,
            message=message,
            finish_reason=finish_reason,
        )

        response_choice.additional_properties = d
        return response_choice

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
