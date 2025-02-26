import json
from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.datapoint import Datapoint
from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
from ..models.fine_tuning_job_synthetic_datageneration_parameters import FineTuningJobSyntheticDatagenerationParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningJobCreate")


class FineTuningJobCreateDict(TypedDict):
    project_id: int
    base_model: str
    datapoints: List["Datapoint"]
    hyperparameters: "FineTuningJobHyperparameters"
    synthetic_datageneration_parameters: "FineTuningJobSyntheticDatagenerationParameters"
    name: Union[Unset, str] = ""
    pass


@_attrs_define
class FineTuningJobCreate:
    """
    Attributes:
        project_id (int): The id of the project to use for finetuning
        base_model (str): The slug of the base model to use for finetuning
        datapoints (List['Datapoint']): The datapoints to use for finetuning
        hyperparameters (FineTuningJobHyperparameters):
        synthetic_datageneration_parameters (FineTuningJobSyntheticDatagenerationParameters):
        name (Union[Unset, str]): Name of the fine-tuning job Default: ''.
    """

    project_id: int
    base_model: str
    datapoints: List["Datapoint"]
    hyperparameters: "FineTuningJobHyperparameters"
    synthetic_datageneration_parameters: "FineTuningJobSyntheticDatagenerationParameters"
    name: Union[Unset, str] = ""

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id

        base_model = self.base_model

        datapoints = []
        for datapoints_item_data in self.datapoints:
            datapoints_item = datapoints_item_data.to_dict()
            datapoints.append(datapoints_item)

        hyperparameters = self.hyperparameters.to_dict()

        synthetic_datageneration_parameters = self.synthetic_datageneration_parameters.to_dict()

        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "base_model": base_model,
                "datapoints": datapoints,
                "hyperparameters": hyperparameters,
                "synthetic_datageneration_parameters": synthetic_datageneration_parameters,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        project_id = (
            self.project_id
            if isinstance(self.project_id, Unset)
            else (None, str(self.project_id).encode(), "text/plain")
        )

        base_model = (
            self.base_model
            if isinstance(self.base_model, Unset)
            else (None, str(self.base_model).encode(), "text/plain")
        )

        _temp_datapoints = []
        for datapoints_item_data in self.datapoints:
            datapoints_item = datapoints_item_data.to_dict()
            _temp_datapoints.append(datapoints_item)
        datapoints = (None, json.dumps(_temp_datapoints).encode(), "application/json")

        hyperparameters = (None, json.dumps(self.hyperparameters.to_dict()).encode(), "application/json")

        synthetic_datageneration_parameters = (
            None,
            json.dumps(self.synthetic_datageneration_parameters.to_dict()).encode(),
            "application/json",
        )

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "project_id": project_id,
                "base_model": base_model,
                "datapoints": datapoints,
                "hyperparameters": hyperparameters,
                "synthetic_datageneration_parameters": synthetic_datageneration_parameters,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.datapoint import Datapoint
        from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
        from ..models.fine_tuning_job_synthetic_datageneration_parameters import (
            FineTuningJobSyntheticDatagenerationParameters,
        )

        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        base_model = d.pop("base_model")

        datapoints = []
        _datapoints = d.pop("datapoints")
        for datapoints_item_data in _datapoints:
            datapoints_item = Datapoint.from_dict(datapoints_item_data)

            datapoints.append(datapoints_item)

        hyperparameters = FineTuningJobHyperparameters.from_dict(d.pop("hyperparameters"))

        synthetic_datageneration_parameters = FineTuningJobSyntheticDatagenerationParameters.from_dict(
            d.pop("synthetic_datageneration_parameters")
        )

        name = d.pop("name", UNSET)

        fine_tuning_job_create = cls(
            project_id=project_id,
            base_model=base_model,
            datapoints=datapoints,
            hyperparameters=hyperparameters,
            synthetic_datageneration_parameters=synthetic_datageneration_parameters,
            name=name,
        )

        fine_tuning_job_create.additional_properties = d
        return fine_tuning_job_create

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
