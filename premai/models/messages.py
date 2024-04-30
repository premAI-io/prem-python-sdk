from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.messages_role_enum import MessagesRoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Messages")


class MessagesDict(TypedDict):
    role: NotRequired[Union[Unset, MessagesRoleEnum]]
    content: NotRequired[Union[Unset, str]]
    pass


@_attrs_define
class Messages:
    """
    Attributes:
        role (Union[Unset, MessagesRoleEnum]): * `user` - user
            * `assistant` - assistant
            * `system` - system
        content (Union[Unset, str]):
    """

    role: Union[Unset, MessagesRoleEnum] = UNSET
    content: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        _role = d.pop("role", UNSET)
        role: Union[Unset, MessagesRoleEnum]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = MessagesRoleEnum(_role)

        content = d.pop("content", UNSET)

        messages = cls(
            role=role,
            content=content,
        )

        messages.additional_properties = d
        return messages

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
