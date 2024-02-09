from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.v1_chat_completions_create_data_body_messages_item_role import (
    V1ChatCompletionsCreateDataBodyMessagesItemRole,
)

T = TypeVar("T", bound="V1ChatCompletionsCreateDataBodyMessagesItem")


class V1ChatCompletionsCreateDataBodyMessagesItemDict(TypedDict):
    role: "V1ChatCompletionsCreateDataBodyMessagesItemRole"
    content: str
    pass


@_attrs_define
class V1ChatCompletionsCreateDataBodyMessagesItem:
    """
    Attributes:
        role (V1ChatCompletionsCreateDataBodyMessagesItemRole): The role of the sender (e.g., 'user', 'assistant' or
            'system').

            * `user` - user
            * `system` - system
            * `assistant` - assistant
        content (str): The content of the message.
    """

    role: "V1ChatCompletionsCreateDataBodyMessagesItemRole"
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
        from ..models.v1_chat_completions_create_data_body_messages_item_role import (
            V1ChatCompletionsCreateDataBodyMessagesItemRole,
        )

        d = src_dict.copy() if src_dict else {}
        role = V1ChatCompletionsCreateDataBodyMessagesItemRole.from_dict(d.pop("role"))

        content = d.pop("content")

        v1_chat_completions_create_data_body_messages_item = cls(
            role=role,
            content=content,
        )

        v1_chat_completions_create_data_body_messages_item.additional_properties = d
        return v1_chat_completions_create_data_body_messages_item

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
