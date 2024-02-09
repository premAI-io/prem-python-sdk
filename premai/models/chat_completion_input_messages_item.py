from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.chat_completion_input_messages_item_role import ChatCompletionInputMessagesItemRole

T = TypeVar("T", bound="ChatCompletionInputMessagesItem")


class ChatCompletionInputMessagesItemDict(TypedDict):
    role: "ChatCompletionInputMessagesItemRole"
    content: str
    pass


@_attrs_define
class ChatCompletionInputMessagesItem:
    """
    Attributes:
        role (ChatCompletionInputMessagesItemRole): The role of the sender (e.g., 'user', 'assistant' or 'system').

            * `user` - user
            * `system` - system
            * `assistant` - assistant
        content (str): The content of the message.
    """

    role: "ChatCompletionInputMessagesItemRole"
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
        from ..models.chat_completion_input_messages_item_role import ChatCompletionInputMessagesItemRole

        d = src_dict.copy() if src_dict else {}
        role = ChatCompletionInputMessagesItemRole.from_dict(d.pop("role"))

        content = d.pop("content")

        chat_completion_input_messages_item = cls(
            role=role,
            content=content,
        )

        chat_completion_input_messages_item.additional_properties = d
        return chat_completion_input_messages_item

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
