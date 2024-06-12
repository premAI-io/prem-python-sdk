from typing import Dict, List, Type, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.parameters_properties import ParametersProperties

T = TypeVar("T", bound="Parameters")


class ParametersDict(TypedDict):
    type: str
    properties: "ParametersProperties"
    required: List[str]
    pass


@_attrs_define
class Parameters:
    """
    Attributes:
        type (str):
        properties (ParametersProperties):
        required (List[str]):
    """

    type: str
    properties: "ParametersProperties"
    required: List[str]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        properties = self.properties.to_dict()

        required = self.required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "properties": properties,
                "required": required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parameters_properties import ParametersProperties

        d = src_dict.copy() if src_dict else {}
        type = d.pop("type")

        properties = ParametersProperties.from_dict(d.pop("properties"))

        required = cast(List[str], d.pop("required"))

        parameters = cls(
            type=type,
            properties=properties,
            required=required,
        )

        parameters.additional_properties = d
        return parameters

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
