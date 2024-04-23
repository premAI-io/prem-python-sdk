from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.data_point_gym_admin import DataPointGymAdmin
from ..models.data_set_fine_tuning_job_gym_admin import DataSetFineTuningJobGymAdmin
from ..models.data_set_fine_tuning_request import DataSetFineTuningRequest
from ..models.data_set_project import DataSetProject

T = TypeVar("T", bound="DataSetGymAdmin")


class DataSetGymAdminDict(TypedDict):
    id: int
    project: "DataSetProject"
    training_finetuning_requests: List["DataSetFineTuningRequest"]
    training_finetuningjobs: List["DataSetFineTuningJobGymAdmin"]
    datapoints: List["DataPointGymAdmin"]
    pass


@_attrs_define
class DataSetGymAdmin:
    """
    Attributes:
        id (int):
        project (DataSetProject):
        training_finetuning_requests (List['DataSetFineTuningRequest']):
        training_finetuningjobs (List['DataSetFineTuningJobGymAdmin']):
        datapoints (List['DataPointGymAdmin']):
    """

    id: int
    project: "DataSetProject"
    training_finetuning_requests: List["DataSetFineTuningRequest"]
    training_finetuningjobs: List["DataSetFineTuningJobGymAdmin"]
    datapoints: List["DataPointGymAdmin"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        project = self.project.to_dict()

        training_finetuning_requests = []
        for training_finetuning_requests_item_data in self.training_finetuning_requests:
            training_finetuning_requests_item = training_finetuning_requests_item_data.to_dict()
            training_finetuning_requests.append(training_finetuning_requests_item)

        training_finetuningjobs = []
        for training_finetuningjobs_item_data in self.training_finetuningjobs:
            training_finetuningjobs_item = training_finetuningjobs_item_data.to_dict()
            training_finetuningjobs.append(training_finetuningjobs_item)

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
                "training_finetuning_requests": training_finetuning_requests,
                "training_finetuningjobs": training_finetuningjobs,
                "datapoints": datapoints,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.data_point_gym_admin import DataPointGymAdmin
        from ..models.data_set_fine_tuning_job_gym_admin import DataSetFineTuningJobGymAdmin
        from ..models.data_set_fine_tuning_request import DataSetFineTuningRequest
        from ..models.data_set_project import DataSetProject

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        project = DataSetProject.from_dict(d.pop("project"))

        training_finetuning_requests = []
        _training_finetuning_requests = d.pop("training_finetuning_requests")
        for training_finetuning_requests_item_data in _training_finetuning_requests:
            training_finetuning_requests_item = DataSetFineTuningRequest.from_dict(
                training_finetuning_requests_item_data
            )

            training_finetuning_requests.append(training_finetuning_requests_item)

        training_finetuningjobs = []
        _training_finetuningjobs = d.pop("training_finetuningjobs")
        for training_finetuningjobs_item_data in _training_finetuningjobs:
            training_finetuningjobs_item = DataSetFineTuningJobGymAdmin.from_dict(training_finetuningjobs_item_data)

            training_finetuningjobs.append(training_finetuningjobs_item)

        datapoints = []
        _datapoints = d.pop("datapoints")
        for datapoints_item_data in _datapoints:
            datapoints_item = DataPointGymAdmin.from_dict(datapoints_item_data)

            datapoints.append(datapoints_item)

        data_set_gym_admin = cls(
            id=id,
            project=project,
            training_finetuning_requests=training_finetuning_requests,
            training_finetuningjobs=training_finetuningjobs,
            datapoints=datapoints,
        )

        data_set_gym_admin.additional_properties = d
        return data_set_gym_admin

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
