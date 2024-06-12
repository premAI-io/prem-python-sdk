from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.parameters import Parameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="Function")


class FunctionDict(TypedDict):
    name: str
    parameters: "Parameters"
    description: NotRequired[Union[Unset, str]]
    pass


@_attrs_define
class Function:
    """
    Attributes:
        name (str):
        parameters (Parameters):
        description (Union[Unset, str]):
    """

    name: str
    parameters: "Parameters"
    description: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        parameters = self.parameters.to_dict()

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.parameters import Parameters

        d = src_dict.copy() if src_dict else {}
        name = d.pop("name")

        parameters = Parameters.from_dict(d.pop("parameters"))

        description = d.pop("description", UNSET)

        function = cls(
            name=name,
            parameters=parameters,
            description=description,
        )

        function.additional_properties = d
        return function

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
