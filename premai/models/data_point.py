import datetime
from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataPoint")


class DataPointDict(TypedDict):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    positive: bool
    input_: NotRequired[Union[None, Unset, str]]
    output: NotRequired[Union[None, Unset, str]]
    trace: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class DataPoint:
    """
    Attributes:
        id (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        positive (bool):
        input_ (Union[None, Unset, str]):
        output (Union[None, Unset, str]):
        trace (Union[None, Unset, str]):
    """

    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    positive: bool
    input_: Union[None, Unset, str] = UNSET
    output: Union[None, Unset, str] = UNSET
    trace: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        positive = self.positive

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
                "created_at": created_at,
                "updated_at": updated_at,
                "positive": positive,
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

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        positive = d.pop("positive")

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

        data_point = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            positive=positive,
            input_=input_,
            output=output,
            trace=trace,
        )

        data_point.additional_properties = d
        return data_point

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
