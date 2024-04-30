import json
from typing import Dict, List, Tuple, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.feedback_create_feedback import FeedbackCreateFeedback
from ..types import UNSET, Unset

T = TypeVar("T", bound="FeedbackCreate")


class FeedbackCreateDict(TypedDict):
    trace_id: str
    feedback: NotRequired[Union["FeedbackCreateFeedback", None, Unset]]
    pass


@_attrs_define
class FeedbackCreate:
    """
    Attributes:
        trace_id (str):
        feedback (Union['FeedbackCreateFeedback', None, Unset]):
    """

    trace_id: str
    feedback: Union["FeedbackCreateFeedback", None, Unset] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.feedback_create_feedback import FeedbackCreateFeedback

        trace_id = self.trace_id

        feedback: Union[Dict[str, Any], None, Unset]
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        elif isinstance(self.feedback, FeedbackCreateFeedback):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
            }
        )
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        trace_id = (
            self.trace_id if isinstance(self.trace_id, Unset) else (None, str(self.trace_id).encode(), "text/plain")
        )

        feedback: Union[None, Tuple[None, bytes, str], Unset]
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        elif isinstance(self.feedback, FeedbackCreateFeedback):
            feedback = (None, json.dumps(self.feedback.to_dict()).encode(), "application/json")
        else:
            feedback = self.feedback

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "trace_id": trace_id,
            }
        )
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.feedback_create_feedback import FeedbackCreateFeedback

        d = src_dict.copy() if src_dict else {}
        trace_id = d.pop("trace_id")

        def _parse_feedback(data: object) -> Union["FeedbackCreateFeedback", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_type_1 = FeedbackCreateFeedback.from_dict(data)

                return feedback_type_1
            except:  # noqa: E722
                pass
            return cast(Union["FeedbackCreateFeedback", None, Unset], data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))

        feedback_create = cls(
            trace_id=trace_id,
            feedback=feedback,
        )

        feedback_create.additional_properties = d
        return feedback_create

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
