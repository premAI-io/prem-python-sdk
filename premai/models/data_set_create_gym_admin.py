import json
from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.data_point_create_gym_admin import DataPointCreateGymAdmin
from ..types import Unset

T = TypeVar("T", bound="DataSetCreateGymAdmin")


class DataSetCreateGymAdminDict(TypedDict):
    id: int
    project: int
    datapoints: List["DataPointCreateGymAdmin"]
    pass


@_attrs_define
class DataSetCreateGymAdmin:
    """
    Attributes:
        id (int):
        project (int):
        datapoints (List['DataPointCreateGymAdmin']):
    """

    id: int
    project: int
    datapoints: List["DataPointCreateGymAdmin"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        project = self.project

        datapoints = []
        for datapoints_item_data in self.datapoints:
            datapoints_item = datapoints_item_data.to_dict()
            datapoints.append(datapoints_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project": project,
                "datapoints": datapoints,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        project = self.project if isinstance(self.project, Unset) else (None, str(self.project).encode(), "text/plain")

        _temp_datapoints = []
        for datapoints_item_data in self.datapoints:
            datapoints_item = datapoints_item_data.to_dict()
            _temp_datapoints.append(datapoints_item)
        datapoints = (None, json.dumps(_temp_datapoints).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "project": project,
                "datapoints": datapoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_point_create_gym_admin import DataPointCreateGymAdmin

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        project = d.pop("project")

        datapoints = []
        _datapoints = d.pop("datapoints")
        for datapoints_item_data in _datapoints:
            datapoints_item = DataPointCreateGymAdmin.from_dict(datapoints_item_data)

            datapoints.append(datapoints_item)

        data_set_create_gym_admin = cls(
            id=id,
            project=project,
            datapoints=datapoints,
        )

        data_set_create_gym_admin.additional_properties = d
        return data_set_create_gym_admin

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
