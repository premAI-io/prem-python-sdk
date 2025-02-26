import datetime
from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.datapoint import Datapoint
from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
from ..models.fine_tuning_job_response_error import FineTuningJobResponseError
from ..models.fine_tuning_job_response_evaluation_scores import FineTuningJobResponseEvaluationScores
from ..models.fine_tuning_job_synthetic_datageneration_parameters import FineTuningJobSyntheticDatagenerationParameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningJobResponse")


class FineTuningJobResponseDict(TypedDict):
    name: str
    base_model: str
    status: str
    original_dataset: List["Datapoint"]
    augmented_dataset: List["Datapoint"]
    num_topics: int
    num_augmented_datapoints: int
    created_at: datetime.datetime
    finetuned_model_id: int
    id: int
    provider_job_id: str
    hyperparameters: "FineTuningJobHyperparameters"
    synthetic_datageneration_parameters: "FineTuningJobSyntheticDatagenerationParameters"
    evaluation_scores: NotRequired[Union[Unset, FineTuningJobResponseEvaluationScores]]
    error: NotRequired[Union[Unset, FineTuningJobResponseError]]
    pass


@_attrs_define
class FineTuningJobResponse:
    """
    Attributes:
        name (str):
        base_model (str):
        status (str):
        original_dataset (List['Datapoint']):
        augmented_dataset (List['Datapoint']):
        num_topics (int):
        num_augmented_datapoints (int):
        created_at (datetime.datetime):
        finetuned_model_id (int):
        id (int):
        provider_job_id (str):
        hyperparameters (FineTuningJobHyperparameters):
        synthetic_datageneration_parameters (FineTuningJobSyntheticDatagenerationParameters):
        evaluation_scores (Union[Unset, FineTuningJobResponseEvaluationScores]):
        error (Union[Unset, FineTuningJobResponseError]):
    """

    name: str
    base_model: str
    status: str
    original_dataset: List["Datapoint"]
    augmented_dataset: List["Datapoint"]
    num_topics: int
    num_augmented_datapoints: int
    created_at: datetime.datetime
    finetuned_model_id: int
    id: int
    provider_job_id: str
    hyperparameters: "FineTuningJobHyperparameters"
    synthetic_datageneration_parameters: "FineTuningJobSyntheticDatagenerationParameters"
    evaluation_scores: Union[Unset, "FineTuningJobResponseEvaluationScores"] = UNSET
    error: Union[Unset, "FineTuningJobResponseError"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        base_model = self.base_model

        status = self.status

        original_dataset = []
        for original_dataset_item_data in self.original_dataset:
            original_dataset_item = original_dataset_item_data.to_dict()
            original_dataset.append(original_dataset_item)

        augmented_dataset = []
        for augmented_dataset_item_data in self.augmented_dataset:
            augmented_dataset_item = augmented_dataset_item_data.to_dict()
            augmented_dataset.append(augmented_dataset_item)

        num_topics = self.num_topics

        num_augmented_datapoints = self.num_augmented_datapoints

        created_at = self.created_at.isoformat()

        finetuned_model_id = self.finetuned_model_id

        id = self.id

        provider_job_id = self.provider_job_id

        hyperparameters = self.hyperparameters.to_dict()

        synthetic_datageneration_parameters = self.synthetic_datageneration_parameters.to_dict()

        evaluation_scores: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.evaluation_scores, Unset):
            evaluation_scores = self.evaluation_scores.to_dict()

        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "baseModel": base_model,
                "status": status,
                "originalDataset": original_dataset,
                "augmentedDataset": augmented_dataset,
                "numTopics": num_topics,
                "numAugmentedDatapoints": num_augmented_datapoints,
                "createdAt": created_at,
                "finetunedModelId": finetuned_model_id,
                "id": id,
                "providerJobId": provider_job_id,
                "hyperparameters": hyperparameters,
                "syntheticDatagenerationParameters": synthetic_datageneration_parameters,
            }
        )
        if evaluation_scores is not UNSET:
            field_dict["evaluationScores"] = evaluation_scores
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.datapoint import Datapoint
        from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
        from ..models.fine_tuning_job_response_error import FineTuningJobResponseError
        from ..models.fine_tuning_job_response_evaluation_scores import FineTuningJobResponseEvaluationScores
        from ..models.fine_tuning_job_synthetic_datageneration_parameters import (
            FineTuningJobSyntheticDatagenerationParameters,
        )

        d = src_dict.copy() if src_dict else {}
        name = d.pop("name")

        base_model = d.pop("baseModel")

        status = d.pop("status")

        original_dataset = []
        _original_dataset = d.pop("originalDataset")
        for original_dataset_item_data in _original_dataset:
            original_dataset_item = Datapoint.from_dict(original_dataset_item_data)

            original_dataset.append(original_dataset_item)

        augmented_dataset = []
        _augmented_dataset = d.pop("augmentedDataset")
        for augmented_dataset_item_data in _augmented_dataset:
            augmented_dataset_item = Datapoint.from_dict(augmented_dataset_item_data)

            augmented_dataset.append(augmented_dataset_item)

        num_topics = d.pop("numTopics")

        num_augmented_datapoints = d.pop("numAugmentedDatapoints")

        created_at = isoparse(d.pop("createdAt"))

        finetuned_model_id = d.pop("finetunedModelId")

        id = d.pop("id")

        provider_job_id = d.pop("providerJobId")

        hyperparameters = FineTuningJobHyperparameters.from_dict(d.pop("hyperparameters"))

        synthetic_datageneration_parameters = FineTuningJobSyntheticDatagenerationParameters.from_dict(
            d.pop("syntheticDatagenerationParameters")
        )

        _evaluation_scores = d.pop("evaluationScores", UNSET)
        evaluation_scores: Union[Unset, FineTuningJobResponseEvaluationScores]
        if isinstance(_evaluation_scores, Unset):
            evaluation_scores = UNSET
        else:
            evaluation_scores = FineTuningJobResponseEvaluationScores.from_dict(_evaluation_scores)

        _error = d.pop("error", UNSET)
        error: Union[Unset, FineTuningJobResponseError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = FineTuningJobResponseError.from_dict(_error)

        fine_tuning_job_response = cls(
            name=name,
            base_model=base_model,
            status=status,
            original_dataset=original_dataset,
            augmented_dataset=augmented_dataset,
            num_topics=num_topics,
            num_augmented_datapoints=num_augmented_datapoints,
            created_at=created_at,
            finetuned_model_id=finetuned_model_id,
            id=id,
            provider_job_id=provider_job_id,
            hyperparameters=hyperparameters,
            synthetic_datageneration_parameters=synthetic_datageneration_parameters,
            evaluation_scores=evaluation_scores,
            error=error,
        )

        fine_tuning_job_response.additional_properties = d
        return fine_tuning_job_response

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
