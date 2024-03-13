from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentChunks")


class DocumentChunksDict(TypedDict):
    repository_id: NotRequired[Union[Unset, int]]
    document_id: NotRequired[Union[Unset, int]]
    chunk_id: NotRequired[Union[Unset, int]]
    document_name: NotRequired[Union[Unset, str]]
    similarity_score: NotRequired[Union[Unset, float]]
    content: NotRequired[Union[Unset, str]]
    pass


@_attrs_define
class DocumentChunks:
    """
    Attributes:
        repository_id (Union[Unset, int]):
        document_id (Union[Unset, int]):
        chunk_id (Union[Unset, int]):
        document_name (Union[Unset, str]):
        similarity_score (Union[Unset, float]):
        content (Union[Unset, str]):
    """

    repository_id: Union[Unset, int] = UNSET
    document_id: Union[Unset, int] = UNSET
    chunk_id: Union[Unset, int] = UNSET
    document_name: Union[Unset, str] = UNSET
    similarity_score: Union[Unset, float] = UNSET
    content: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository_id = self.repository_id

        document_id = self.document_id

        chunk_id = self.chunk_id

        document_name = self.document_name

        similarity_score = self.similarity_score

        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repository_id is not UNSET:
            field_dict["repository_id"] = repository_id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if chunk_id is not UNSET:
            field_dict["chunk_id"] = chunk_id
        if document_name is not UNSET:
            field_dict["document_name"] = document_name
        if similarity_score is not UNSET:
            field_dict["similarity_score"] = similarity_score
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        repository_id = d.pop("repository_id", UNSET)

        document_id = d.pop("document_id", UNSET)

        chunk_id = d.pop("chunk_id", UNSET)

        document_name = d.pop("document_name", UNSET)

        similarity_score = d.pop("similarity_score", UNSET)

        content = d.pop("content", UNSET)

        document_chunks = cls(
            repository_id=repository_id,
            document_id=document_id,
            chunk_id=chunk_id,
            document_name=document_name,
            similarity_score=similarity_score,
            content=content,
        )

        document_chunks.additional_properties = d
        return document_chunks

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
