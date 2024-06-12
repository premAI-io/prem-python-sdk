from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.parameter_properties import ParameterProperties

T = TypeVar("T", bound="ParametersProperties")


class ParametersPropertiesDict(TypedDict):
    pass


@_attrs_define
class ParametersProperties:
    """ """

    additional_properties: Dict[str, "ParameterProperties"] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parameter_properties import ParameterProperties

        d = src_dict.copy() if src_dict else {}
        parameters_properties = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = ParameterProperties.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        parameters_properties.additional_properties = additional_properties
        return parameters_properties

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> "ParameterProperties":
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: "ParameterProperties") -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
