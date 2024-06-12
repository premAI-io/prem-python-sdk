from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.function import Function
from ..models.type_enum import TypeEnum

T = TypeVar("T", bound="Tool")


class ToolDict(TypedDict):
    type: TypeEnum
    function: "Function"
    pass


@_attrs_define
class Tool:
    """
    Attributes:
        type (TypeEnum): * `function` - function
        function (Function):
    """

    type: TypeEnum
    function: "Function"

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        function = self.function.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "function": function,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.function import Function

        d = src_dict.copy() if src_dict else {}
        type = TypeEnum(d.pop("type"))

        function = Function.from_dict(d.pop("function"))

        tool = cls(
            type=type,
            function=function,
        )

        tool.additional_properties = d
        return tool

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
