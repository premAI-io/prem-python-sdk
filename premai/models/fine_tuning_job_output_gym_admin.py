import datetime
from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.status_c4a_enum import StatusC4AEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningJobOutputGymAdmin")


class FineTuningJobOutputGymAdminDict(TypedDict):
    id: int
    job_id: str
    finished_at: NotRequired[Union[None, Unset, datetime.datetime]]
    status: NotRequired[Union[Unset, StatusC4AEnum]]
    fine_tuned_model: NotRequired[Union[None, Unset, int]]
    fine_tuning_request: NotRequired[Union[None, Unset, int]]
    training_dataset: NotRequired[Union[None, Unset, int]]
    validation_dataset: NotRequired[Union[None, Unset, int]]
    pass


@_attrs_define
class FineTuningJobOutputGymAdmin:
    """
    Attributes:
        id (int):
        job_id (str):
        finished_at (Union[None, Unset, datetime.datetime]):
        status (Union[Unset, StatusC4AEnum]): * `unknown` - Unknown
            * `queued` - Queued
            * `running` - Running
            * `succeeded` - Succeeded
            * `failed` - Failed
            * `cancelled` - Cancelled
        fine_tuned_model (Union[None, Unset, int]):
        fine_tuning_request (Union[None, Unset, int]):
        training_dataset (Union[None, Unset, int]):
        validation_dataset (Union[None, Unset, int]):
    """

    id: int
    job_id: str
    finished_at: Union[None, Unset, datetime.datetime] = UNSET
    status: Union[Unset, StatusC4AEnum] = UNSET
    fine_tuned_model: Union[None, Unset, int] = UNSET
    fine_tuning_request: Union[None, Unset, int] = UNSET
    training_dataset: Union[None, Unset, int] = UNSET
    validation_dataset: Union[None, Unset, int] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        job_id = self.job_id

        finished_at: Union[None, Unset, str]
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        fine_tuned_model: Union[None, Unset, int]
        if isinstance(self.fine_tuned_model, Unset):
            fine_tuned_model = UNSET
        else:
            fine_tuned_model = self.fine_tuned_model

        fine_tuning_request: Union[None, Unset, int]
        if isinstance(self.fine_tuning_request, Unset):
            fine_tuning_request = UNSET
        else:
            fine_tuning_request = self.fine_tuning_request

        training_dataset: Union[None, Unset, int]
        if isinstance(self.training_dataset, Unset):
            training_dataset = UNSET
        else:
            training_dataset = self.training_dataset

        validation_dataset: Union[None, Unset, int]
        if isinstance(self.validation_dataset, Unset):
            validation_dataset = UNSET
        else:
            validation_dataset = self.validation_dataset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "job_id": job_id,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if status is not UNSET:
            field_dict["status"] = status
        if fine_tuned_model is not UNSET:
            field_dict["fine_tuned_model"] = fine_tuned_model
        if fine_tuning_request is not UNSET:
            field_dict["fine_tuning_request"] = fine_tuning_request
        if training_dataset is not UNSET:
            field_dict["training_dataset"] = training_dataset
        if validation_dataset is not UNSET:
            field_dict["validation_dataset"] = validation_dataset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        job_id = d.pop("job_id")

        def _parse_finished_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)

                return finished_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusC4AEnum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusC4AEnum(_status)

        def _parse_fine_tuned_model(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fine_tuned_model = _parse_fine_tuned_model(d.pop("fine_tuned_model", UNSET))

        def _parse_fine_tuning_request(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fine_tuning_request = _parse_fine_tuning_request(d.pop("fine_tuning_request", UNSET))

        def _parse_training_dataset(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        training_dataset = _parse_training_dataset(d.pop("training_dataset", UNSET))

        def _parse_validation_dataset(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        validation_dataset = _parse_validation_dataset(d.pop("validation_dataset", UNSET))

        fine_tuning_job_output_gym_admin = cls(
            id=id,
            job_id=job_id,
            finished_at=finished_at,
            status=status,
            fine_tuned_model=fine_tuned_model,
            fine_tuning_request=fine_tuning_request,
            training_dataset=training_dataset,
            validation_dataset=validation_dataset,
        )

        fine_tuning_job_output_gym_admin.additional_properties = d
        return fine_tuning_job_output_gym_admin

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
