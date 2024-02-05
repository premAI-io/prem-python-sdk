from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.message_role import MessageRole

T = TypeVar("T", bound="Message")


class MessageDict(TypedDict):
    role: "MessageRole"
    content: str
    pass


@_attrs_define
class Message:
    """
    Attributes:
        role (MessageRole): The role of the sender (e.g., 'user' or 'system').

            * `user` - user
            * `system` - system
        content (str): The content of the message.
    """

    role: "MessageRole"
    content: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.to_dict()

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_role import MessageRole

        d = src_dict.copy()
        role = MessageRole.from_dict(d.pop("role"))

        content = d.pop("content")

        message = cls(
            role=role,
            content=content,
        )

        message.additional_properties = d
        return message

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