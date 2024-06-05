from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="Repository")


class RepositoryDict(TypedDict):
    id: int
    name: str
    organization: str
    description: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class Repository:
    """
    Attributes:
        id (int):
        name (str):
        organization (str):
        description (Union[None, Unset, str]):
    """

    id: int
    name: str
    organization: str
    description: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        organization = self.organization

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        organization = (
            self.organization
            if isinstance(self.organization, Unset)
            else (None, str(self.organization).encode(), "text/plain")
        )

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "name": name,
                "organization": organization,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        name = d.pop("name")

        organization = d.pop("organization")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        repository = cls(
            id=id,
            name=name,
            organization=organization,
            description=description,
        )

        repository.additional_properties = d
        return repository

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
