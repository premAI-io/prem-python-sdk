from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.document_type_enum import DocumentTypeEnum
from ..models.status_enum import StatusEnum

T = TypeVar("T", bound="DocumentOutput")


class DocumentOutputDict(TypedDict):
    repository_id: int
    document_id: int
    name: str
    document_type: DocumentTypeEnum
    status: StatusEnum
    error: Union[None, str]
    chunk_count: int = 0
    pass


@_attrs_define
class DocumentOutput:
    """
    Attributes:
        repository_id (int):
        document_id (int):
        name (str):
        document_type (DocumentTypeEnum): * `pdf` - PDF
            * `docx` - Word
            * `txt` - Text
        status (StatusEnum): * `PENDING` - Pending
            * `UPLOADED` - Uploaded
            * `PARSING` - Parsing
            * `CHUNKING` - Chunking
            * `WAITING_FOR_CHUNKS_COMPLETION` - Waiting for chunks completion
            * `PROCESSING` - Processing
            * `COMPLETED` - Completed
            * `FAILED` - Failed
        error (Union[None, str]):
        chunk_count (int):  Default: 0.
    """

    repository_id: int
    document_id: int
    name: str
    document_type: DocumentTypeEnum
    status: StatusEnum
    error: Union[None, str]
    chunk_count: int = 0

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repository_id = self.repository_id

        document_id = self.document_id

        name = self.name

        document_type = self.document_type.value

        status = self.status.value

        error: Union[None, str]
        error = self.error

        chunk_count = self.chunk_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "repository_id": repository_id,
                "document_id": document_id,
                "name": name,
                "document_type": document_type,
                "status": status,
                "error": error,
                "chunk_count": chunk_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        repository_id = d.pop("repository_id")

        document_id = d.pop("document_id")

        name = d.pop("name")

        document_type = DocumentTypeEnum(d.pop("document_type"))

        status = StatusEnum(d.pop("status"))

        def _parse_error(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        error = _parse_error(d.pop("error"))

        chunk_count = d.pop("chunk_count")

        document_output = cls(
            repository_id=repository_id,
            document_id=document_id,
            name=name,
            document_type=document_type,
            status=status,
            error=error,
            chunk_count=chunk_count,
        )

        document_output.additional_properties = d
        return document_output

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
