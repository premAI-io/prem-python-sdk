from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.status_d09_enum import StatusD09Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSetFineTuningRequest")


class DataSetFineTuningRequestDict(TypedDict):
    id: int
    status: NotRequired[Union[Unset, StatusD09Enum]]
    pass


@_attrs_define
class DataSetFineTuningRequest:
    """
    Attributes:
        id (int):
        status (Union[Unset, StatusD09Enum]): * `queued` - Queued
            * `finetuning` - Fine tuning
            * `done` - Done
            * `failed` - Failed
    """

    id: int
    status: Union[Unset, StatusD09Enum] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusD09Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusD09Enum(_status)

        data_set_fine_tuning_request = cls(
            id=id,
            status=status,
        )

        data_set_fine_tuning_request.additional_properties = d
        return data_set_fine_tuning_request

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
