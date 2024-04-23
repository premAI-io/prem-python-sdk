from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.status_c4a_enum import StatusC4AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="DataSetFineTuningJobGymAdmin")


class DataSetFineTuningJobGymAdminDict(TypedDict):
    id: int
    status: NotRequired[Union[Unset, StatusC4AEnum]]
    pass


@_attrs_define
class DataSetFineTuningJobGymAdmin:
    """
    Attributes:
        id (int):
        status (Union[Unset, StatusC4AEnum]): * `unknown` - Unknown
            * `queued` - Queued
            * `running` - Running
            * `succeeded` - Succeeded
            * `failed` - Failed
            * `cancelled` - Cancelled
    """

    id: int
    status: Union[Unset, StatusC4AEnum] = UNSET

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
        status: Union[Unset, StatusC4AEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusC4AEnum(_status)

        data_set_fine_tuning_job_gym_admin = cls(
            id=id,
            status=status,
        )

        data_set_fine_tuning_job_gym_admin.additional_properties = d
        return data_set_fine_tuning_job_gym_admin

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
