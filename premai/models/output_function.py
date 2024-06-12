from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.output_function_arguments import OutputFunctionArguments
from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputFunction")


class OutputFunctionDict(TypedDict):
    name: str
    arguments: NotRequired[Union[Unset, OutputFunctionArguments]]
    pass


@_attrs_define
class OutputFunction:
    """
    Attributes:
        name (str): The name of the function to be called.
        arguments (Union[Unset, OutputFunctionArguments]): The arguments passed to the function.
    """

    name: str
    arguments: Union[Unset, "OutputFunctionArguments"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        arguments: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.arguments, Unset):
            arguments = self.arguments.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if arguments is not UNSET:
            field_dict["arguments"] = arguments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.output_function_arguments import OutputFunctionArguments

        d = src_dict.copy() if src_dict else {}
        name = d.pop("name")

        _arguments = d.pop("arguments", UNSET)
        arguments: Union[Unset, OutputFunctionArguments]
        if isinstance(_arguments, Unset):
            arguments = UNSET
        else:
            arguments = OutputFunctionArguments.from_dict(_arguments)

        output_function = cls(
            name=name,
            arguments=arguments,
        )

        output_function.additional_properties = d
        return output_function

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
