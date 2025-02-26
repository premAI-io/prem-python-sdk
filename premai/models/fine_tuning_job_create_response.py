from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="FineTuningJobCreateResponse")


class FineTuningJobCreateResponseDict(TypedDict):
    successful: str
    job_id: int
    job_status: str
    pass


@_attrs_define
class FineTuningJobCreateResponse:
    """
    Attributes:
        successful (str):
        job_id (int):
        job_status (str):
    """

    successful: str
    job_id: int
    job_status: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        successful = self.successful

        job_id = self.job_id

        job_status = self.job_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "successful": successful,
                "job_id": job_id,
                "job_status": job_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        successful = d.pop("successful")

        job_id = d.pop("job_id")

        job_status = d.pop("job_status")

        fine_tuning_job_create_response = cls(
            successful=successful,
            job_id=job_id,
            job_status=job_status,
        )

        fine_tuning_job_create_response.additional_properties = d
        return fine_tuning_job_create_response

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
