from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.messages import Messages
from ..models.model import Model
from ..models.project import Project
from ..models.trace_feedback import TraceFeedback
from ..models.trace_retrieve_document_chunk import TraceRetrieveDocumentChunk
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceRetrieve")


class TraceRetrieveDict(TypedDict):
    trace_id: str
    project: "Project"
    model: "Model"
    feedback: Union["TraceFeedback", None]
    session_id: NotRequired[Union[None, Unset, str]]
    messages: NotRequired[Union[Unset, List["Messages"]]]
    document_chunks: NotRequired[Union[Unset, List["TraceRetrieveDocumentChunk"]]]
    pass


@_attrs_define
class TraceRetrieve:
    """
    Attributes:
        trace_id (str):
        project (Project):
        model (Model):
        feedback (Union['TraceFeedback', None]):
        session_id (Union[None, Unset, str]):
        messages (Union[Unset, List['Messages']]):
        document_chunks (Union[Unset, List['TraceRetrieveDocumentChunk']]):
    """

    trace_id: str
    project: "Project"
    model: "Model"
    feedback: Union["TraceFeedback", None]
    session_id: Union[None, Unset, str] = UNSET
    messages: Union[Unset, List["Messages"]] = UNSET
    document_chunks: Union[Unset, List["TraceRetrieveDocumentChunk"]] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trace_feedback import TraceFeedback

        trace_id = self.trace_id

        project = self.project.to_dict()

        model = self.model.to_dict()

        feedback: Union[Dict[str, Any], None]
        if isinstance(self.feedback, TraceFeedback):
            feedback = self.feedback.to_dict()
        else:
            feedback = self.feedback

        session_id: Union[None, Unset, str]
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()
                messages.append(messages_item)

        document_chunks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.document_chunks, Unset):
            document_chunks = []
            for document_chunks_item_data in self.document_chunks:
                document_chunks_item = document_chunks_item_data.to_dict()
                document_chunks.append(document_chunks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trace_id": trace_id,
                "project": project,
                "model": model,
                "feedback": feedback,
            }
        )
        if session_id is not UNSET:
            field_dict["session_id"] = session_id
        if messages is not UNSET:
            field_dict["messages"] = messages
        if document_chunks is not UNSET:
            field_dict["document_chunks"] = document_chunks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.messages import Messages
        from ..models.model import Model
        from ..models.project import Project
        from ..models.trace_feedback import TraceFeedback
        from ..models.trace_retrieve_document_chunk import TraceRetrieveDocumentChunk

        d = src_dict.copy() if src_dict else {}
        trace_id = d.pop("trace_id")

        project = Project.from_dict(d.pop("project"))

        model = Model.from_dict(d.pop("model"))

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

        def _parse_session_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        session_id = _parse_session_id(d.pop("session_id", UNSET))

        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = Messages.from_dict(messages_item_data)

            messages.append(messages_item)

        document_chunks = []
        _document_chunks = d.pop("document_chunks", UNSET)
        for document_chunks_item_data in _document_chunks or []:
            document_chunks_item = TraceRetrieveDocumentChunk.from_dict(document_chunks_item_data)

            document_chunks.append(document_chunks_item)

        trace_retrieve = cls(
            trace_id=trace_id,
            project=project,
            model=model,
            feedback=feedback,
            session_id=session_id,
            messages=messages,
            document_chunks=document_chunks,
        )

        trace_retrieve.additional_properties = d
        return trace_retrieve

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
