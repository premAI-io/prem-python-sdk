from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.v1_embeddings_create_response_400_details_additional_property import (
    V1EmbeddingsCreateResponse400DetailsAdditionalProperty,
)

T = TypeVar("T", bound="V1EmbeddingsCreateResponse400Details")


class V1EmbeddingsCreateResponse400DetailsDict(TypedDict):
    pass


@_attrs_define
class V1EmbeddingsCreateResponse400Details:
    """Detailed information about the validation errors."""

    additional_properties: Dict[str, "V1EmbeddingsCreateResponse400DetailsAdditionalProperty"] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v1_embeddings_create_response_400_details_additional_property import (
            V1EmbeddingsCreateResponse400DetailsAdditionalProperty,
        )

        d = src_dict.copy() if src_dict else {}
        v1_embeddings_create_response_400_details = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = V1EmbeddingsCreateResponse400DetailsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        v1_embeddings_create_response_400_details.additional_properties = additional_properties
        return v1_embeddings_create_response_400_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "V1EmbeddingsCreateResponse400DetailsAdditionalProperty":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "V1EmbeddingsCreateResponse400DetailsAdditionalProperty") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
