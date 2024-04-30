from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.messages import Messages
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackCreateFeedback")


class FeedbackCreateFeedbackDict(TypedDict):
    positive: Union[Unset, bool] = False
    messages: NotRequired[Union[Unset, List["Messages"]]]
    pass


@_attrs_define
class FeedbackCreateFeedback:
    """
    Attributes:
        positive (Union[Unset, bool]):  Default: False.
        messages (Union[Unset, List['Messages']]):
    """

    positive: Union[Unset, bool] = False
    messages: Union[Unset, List["Messages"]] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positive = self.positive

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if positive is not UNSET:
            field_dict["positive"] = positive
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages import Messages

        d = src_dict.copy() if src_dict else {}
        positive = d.pop("positive", UNSET)

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Messages.from_dict(messages_item_data)

            messages.append(messages_item)

        feedback_create_feedback = cls(
            positive=positive,
            messages=messages,
        )

        feedback_create_feedback.additional_properties = d
        return feedback_create_feedback

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
