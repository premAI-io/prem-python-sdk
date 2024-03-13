from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.document_type_enum import DocumentTypeEnum
from ..types import Unset

T = TypeVar("T", bound="DocumentInput")


class DocumentInputDict(TypedDict):
    name: str
    content: str
    document_type: DocumentTypeEnum
    pass


@_attrs_define
class DocumentInput:
    """
    Attributes:
        name (str):
        content (str):
        document_type (DocumentTypeEnum): * `text` - text
    """

    name: str
    content: str
    document_type: DocumentTypeEnum

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        content = self.content

        document_type = self.document_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "content": content,
                "document_type": document_type,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        content = self.content if isinstance(self.content, Unset) else (None, str(self.content).encode(), "text/plain")

        document_type = (None, str(self.document_type.value).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "name": name,
                "content": content,
                "document_type": document_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        name = d.pop("name")

        content = d.pop("content")

        document_type = DocumentTypeEnum(d.pop("document_type"))

        document_input = cls(
            name=name,
            content=content,
            document_type=document_type,
        )

        document_input.additional_properties = d
        return document_input

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
