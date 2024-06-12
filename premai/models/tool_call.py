from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.output_function import OutputFunction

T = TypeVar("T", bound="ToolCall")


class ToolCallDict(TypedDict):
    id: str
    function: "OutputFunction"
    type: str
    pass


@_attrs_define
class ToolCall:
    """
    Attributes:
        id (str): The ID of the tool call.
        function (OutputFunction):
        type (str): The type of tool call.
    """

    id: str
    function: "OutputFunction"
    type: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        function = self.function.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "function": function,
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.output_function import OutputFunction

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        function = OutputFunction.from_dict(d.pop("function"))

        type = d.pop("type")

        tool_call = cls(
            id=id,
            function=function,
            type=type,
        )

        tool_call.additional_properties = d
        return tool_call

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
