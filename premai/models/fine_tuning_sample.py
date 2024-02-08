from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="FineTuningSample")


class FineTuningSampleDict(TypedDict):
    input_: str
    output: str
    pass


@_attrs_define
class FineTuningSample:
    """
    Attributes:
        input_ (str): The input text.
        output (str): The output text.
    """

    input_: str
    output: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_ = self.input_

        output = self.output

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
                "output": output,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        input_ = d.pop("input")

        output = d.pop("output")

        fine_tuning_sample = cls(
            input_=input_,
            output=output,
        )

        fine_tuning_sample.additional_properties = d
        return fine_tuning_sample

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
