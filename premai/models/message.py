from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.message_params import MessageParams
from ..models.message_role_enum import MessageRoleEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Message")


class MessageDict(TypedDict):
    role: MessageRoleEnum
    content: NotRequired[Union[Unset, str]]
    template_id: NotRequired[Union[Unset, str]]
    params: NotRequired[Union[Unset, MessageParams]]
    pass


@_attrs_define
class Message:
    """
    Attributes:
        role (MessageRoleEnum): * `user` - user
            * `assistant` - assistant
        content (Union[Unset, str]): The content of the message.
        template_id (Union[Unset, str]): The ID of the template to use.
        params (Union[Unset, MessageParams]): The parameters (key: value) to use with the given template.
    """

    role: MessageRoleEnum
    content: Union[Unset, str] = UNSET
    template_id: Union[Unset, str] = UNSET
    params: Union[Unset, "MessageParams"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        content = self.content

        template_id = self.template_id

        params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if template_id is not UNSET:
            field_dict["template_id"] = template_id
        if params is not UNSET:
            field_dict["params"] = params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_params import MessageParams

        d = src_dict.copy() if src_dict else {}
        role = MessageRoleEnum(d.pop("role"))

        content = d.pop("content", UNSET)

        template_id = d.pop("template_id", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, MessageParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = MessageParams.from_dict(_params)

        message = cls(
            role=role,
            content=content,
            template_id=template_id,
            params=params,
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
