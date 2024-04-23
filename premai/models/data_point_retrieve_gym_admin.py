from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataPointRetrieveGymAdmin")


class DataPointRetrieveGymAdminDict(TypedDict):
    id: int
    positive: bool
    override_input: str = "False"
    override_output: str = "False"
    input_: NotRequired[Union[None, Unset, str]]
    output: NotRequired[Union[None, Unset, str]]
    trace: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class DataPointRetrieveGymAdmin:
    """
    Attributes:
        id (int):
        positive (bool):
        override_input (str):  Default: 'False'.
        override_output (str):  Default: 'False'.
        input_ (Union[None, Unset, str]):
        output (Union[None, Unset, str]):
        trace (Union[None, Unset, str]):
    """

    id: int
    positive: bool
    override_input: str = "False"
    override_output: str = "False"
    input_: Union[None, Unset, str] = UNSET
    output: Union[None, Unset, str] = UNSET
    trace: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        positive = self.positive

        override_input = self.override_input

        override_output = self.override_output

        input_: Union[None, Unset, str]
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        output: Union[None, Unset, str]
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        trace: Union[None, Unset, str]
        if isinstance(self.trace, Unset):
            trace = UNSET
        else:
            trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "positive": positive,
                "override_input": override_input,
                "override_output": override_output,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        positive = d.pop("positive")

        override_input = d.pop("override_input")

        override_output = d.pop("override_output")

        def _parse_input_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_output(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        output = _parse_output(d.pop("output", UNSET))

        def _parse_trace(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        trace = _parse_trace(d.pop("trace", UNSET))

        data_point_retrieve_gym_admin = cls(
            id=id,
            positive=positive,
            override_input=override_input,
            override_output=override_output,
            input_=input_,
            output=output,
            trace=trace,
        )

        data_point_retrieve_gym_admin.additional_properties = d
        return data_point_retrieve_gym_admin

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
