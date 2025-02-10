from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.messages import Messages
from ..models.trace_feedback import TraceFeedback
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceList")


class TraceListDict(TypedDict):
    trace_id: str
    project_id: int
    model_id: int
    feedback: Union["TraceFeedback", None]
    messages: NotRequired[Union[Unset, List["Messages"]]]
    pass


@_attrs_define
class TraceList:
    """
    Attributes:
        trace_id (str):
        project_id (int):
        model_id (int):
        feedback (Union['TraceFeedback', None]):
        messages (Union[Unset, List['Messages']]):
    """

    trace_id: str
    project_id: int
    model_id: int
    feedback: Union["TraceFeedback", None]
    messages: Union[Unset, List["Messages"]] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trace_feedback import TraceFeedback

        trace_id = self.trace_id

        project_id = self.project_id

        model_id = self.model_id

        feedback: Union[Dict[str, Any], None]
        if isinstance(self.feedback, TraceFeedback):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "project_id": project_id,
                "model_id": model_id,
                "feedback": feedback,
            }
        )
        if messages is not UNSET:
            field_dict["messages"] = messages

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages import Messages
        from ..models.trace_feedback import TraceFeedback

        d = src_dict.copy() if src_dict else {}
        trace_id = d.pop("trace_id")

        project_id = d.pop("project_id")

        model_id = d.pop("model_id")

        def _parse_feedback(data: object) -> Union["TraceFeedback", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_1 = TraceFeedback.from_dict(data)

                return feedback_type_1
            except:  # noqa: E722
                pass
            return cast(Union["TraceFeedback", None], data)

        feedback = _parse_feedback(d.pop("feedback"))

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Messages.from_dict(messages_item_data)

            messages.append(messages_item)

        trace_list = cls(
            trace_id=trace_id,
            project_id=project_id,
            model_id=model_id,
            feedback=feedback,
            messages=messages,
        )

        trace_list.additional_properties = d
        return trace_list

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
