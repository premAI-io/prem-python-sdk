from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="InputDataPoint")


class InputDataPointDict(TypedDict):
    positive: bool
    project: int
    input_: NotRequired[Union[None, Unset, str]]
    output: NotRequired[Union[None, Unset, str]]
    trace: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class InputDataPoint:
    """
    Attributes:
        positive (bool):
        project (int):
        input_ (Union[None, Unset, str]):
        output (Union[None, Unset, str]):
        trace (Union[None, Unset, str]):
    """

    positive: bool
    project: int
    input_: Union[None, Unset, str] = UNSET
    output: Union[None, Unset, str] = UNSET
    trace: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        positive = self.positive

        project = self.project

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
                "positive": positive,
                "project": project,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        positive = (
            self.positive if isinstance(self.positive, Unset) else (None, str(self.positive).encode(), "text/plain")
        )

        project = self.project if isinstance(self.project, Unset) else (None, str(self.project).encode(), "text/plain")

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
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "positive": positive,
                "project": project,
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
        positive = d.pop("positive")

        project = d.pop("project")

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

        input_data_point = cls(
            positive=positive,
            project=project,
            input_=input_,
            output=output,
            trace=trace,
        )

        input_data_point.additional_properties = d
        return input_data_point

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
