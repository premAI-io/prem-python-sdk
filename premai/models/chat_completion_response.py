from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.document_chunks import DocumentChunks
from ..models.response_choice import ResponseChoice
from ..models.usage import Usage
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionResponse")


class ChatCompletionResponseDict(TypedDict):
    choices: List["ResponseChoice"]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: "Usage"
    trace_id: str
    document_chunks: NotRequired[Union[Unset, List["DocumentChunks"]]]
    pass


@_attrs_define
class ChatCompletionResponse:
    """
    Attributes:
        choices (List['ResponseChoice']): A list of chat completion choices. Can be more than one if n is greater than
            1.
        created (int): The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same
            timestamp.
        model (str): The model to generate the completion.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        usage (Usage):
        trace_id (str): The trace ID of the completion.
        document_chunks (Union[Unset, List['DocumentChunks']]): Chunks used to improve the completion
    """

    choices: List["ResponseChoice"]
    created: int
    model: str
    provider_name: str
    provider_id: str
    usage: "Usage"
    trace_id: str
    document_chunks: Union[Unset, List["DocumentChunks"]] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        created = self.created

        model = self.model

        provider_name = self.provider_name

        provider_id = self.provider_id

        usage = self.usage.to_dict()

        trace_id = self.trace_id

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
                "choices": choices,
                "created": created,
                "model": model,
                "provider_name": provider_name,
                "provider_id": provider_id,
                "usage": usage,
                "trace_id": trace_id,
            }
        )
        if document_chunks is not UNSET:
            field_dict["document_chunks"] = document_chunks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.document_chunks import DocumentChunks
        from ..models.response_choice import ResponseChoice
        from ..models.usage import Usage

        d = src_dict.copy() if src_dict else {}
        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = ResponseChoice.from_dict(choices_item_data)

            choices.append(choices_item)

        created = d.pop("created")

        model = d.pop("model")

        provider_name = d.pop("provider_name")

        provider_id = d.pop("provider_id")

        usage = Usage.from_dict(d.pop("usage"))

        trace_id = d.pop("trace_id")

        document_chunks = []
        _document_chunks = d.pop("document_chunks", UNSET)
        for document_chunks_item_data in _document_chunks or []:
            document_chunks_item = DocumentChunks.from_dict(document_chunks_item_data)

            document_chunks.append(document_chunks_item)

        chat_completion_response = cls(
            choices=choices,
            created=created,
            model=model,
            provider_name=provider_name,
            provider_id=provider_id,
            usage=usage,
            trace_id=trace_id,
            document_chunks=document_chunks,
        )

        chat_completion_response.additional_properties = d
        return chat_completion_response

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
