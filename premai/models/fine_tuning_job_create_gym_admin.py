import datetime
import json
from typing import Dict, List, Tuple, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningJobCreateGymAdmin")


class FineTuningJobCreateGymAdminDict(TypedDict):
    id: int
    fine_tuning_request: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    training_dataset: NotRequired[Union[Unset, int]]
    validation_dataset: NotRequired[Union[Unset, int]]
    hyperparameters: NotRequired[Union[Unset, FineTuningJobHyperparameters]]
    pass


@_attrs_define
class FineTuningJobCreateGymAdmin:
    """
    Attributes:
        id (int):
        fine_tuning_request (int): Fine-tuning request id to be used for fine-tuning
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        training_dataset (Union[Unset, int]): Training dataset id to be used for fine-tuning. If omitted, the dataset
            from the finetuning_request will be used.
        validation_dataset (Union[Unset, int]): Validation dataset id to be used for fine-tuning
        hyperparameters (Union[Unset, FineTuningJobHyperparameters]):
    """

    id: int
    fine_tuning_request: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    training_dataset: Union[Unset, int] = UNSET
    validation_dataset: Union[Unset, int] = UNSET
    hyperparameters: Union[Unset, "FineTuningJobHyperparameters"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        fine_tuning_request = self.fine_tuning_request

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        training_dataset = self.training_dataset

        validation_dataset = self.validation_dataset

        hyperparameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hyperparameters, Unset):
            hyperparameters = self.hyperparameters.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fine_tuning_request": fine_tuning_request,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if training_dataset is not UNSET:
            field_dict["training_dataset"] = training_dataset
        if validation_dataset is not UNSET:
            field_dict["validation_dataset"] = validation_dataset
        if hyperparameters is not UNSET:
            field_dict["hyperparameters"] = hyperparameters

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        fine_tuning_request = (
            self.fine_tuning_request
            if isinstance(self.fine_tuning_request, Unset)
            else (None, str(self.fine_tuning_request).encode(), "text/plain")
        )

        created_at = self.created_at.isoformat().encode()

        updated_at = self.updated_at.isoformat().encode()

        training_dataset = (
            self.training_dataset
            if isinstance(self.training_dataset, Unset)
            else (None, str(self.training_dataset).encode(), "text/plain")
        )

        validation_dataset = (
            self.validation_dataset
            if isinstance(self.validation_dataset, Unset)
            else (None, str(self.validation_dataset).encode(), "text/plain")
        )

        hyperparameters: Union[Unset, Tuple[None, bytes, str]] = UNSET
        if not isinstance(self.hyperparameters, Unset):
            hyperparameters = (None, json.dumps(self.hyperparameters.to_dict()).encode(), "application/json")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "fine_tuning_request": fine_tuning_request,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if training_dataset is not UNSET:
            field_dict["training_dataset"] = training_dataset
        if validation_dataset is not UNSET:
            field_dict["validation_dataset"] = validation_dataset
        if hyperparameters is not UNSET:
            field_dict["hyperparameters"] = hyperparameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fine_tuning_job_hyperparameters import FineTuningJobHyperparameters

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        fine_tuning_request = d.pop("fine_tuning_request")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        training_dataset = d.pop("training_dataset", UNSET)

        validation_dataset = d.pop("validation_dataset", UNSET)

        _hyperparameters = d.pop("hyperparameters", UNSET)
        hyperparameters: Union[Unset, FineTuningJobHyperparameters]
        if isinstance(_hyperparameters, Unset):
            hyperparameters = UNSET
        else:
            hyperparameters = FineTuningJobHyperparameters.from_dict(_hyperparameters)

        fine_tuning_job_create_gym_admin = cls(
            id=id,
            fine_tuning_request=fine_tuning_request,
            created_at=created_at,
            updated_at=updated_at,
            training_dataset=training_dataset,
            validation_dataset=validation_dataset,
            hyperparameters=hyperparameters,
        )

        fine_tuning_job_create_gym_admin.additional_properties = d
        return fine_tuning_job_create_gym_admin

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
