from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..types import Unset

T = TypeVar("T", bound="DeleteFinetuningJobRequest")


class DeleteFinetuningJobRequestDict(TypedDict):
    project_id: int
    fine_tuning_job_id: int
    pass


@_attrs_define
class DeleteFinetuningJobRequest:
    """
    Attributes:
        project_id (int): The ID of the project
        fine_tuning_job_id (int): The ID of the finetuning job to delete
    """

    project_id: int
    fine_tuning_job_id: int

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id

        fine_tuning_job_id = self.fine_tuning_job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "fine_tuning_job_id": fine_tuning_job_id,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        project_id = (
            self.project_id
            if isinstance(self.project_id, Unset)
            else (None, str(self.project_id).encode(), "text/plain")
        )

        fine_tuning_job_id = (
            self.fine_tuning_job_id
            if isinstance(self.fine_tuning_job_id, Unset)
            else (None, str(self.fine_tuning_job_id).encode(), "text/plain")
        )

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "project_id": project_id,
                "fine_tuning_job_id": fine_tuning_job_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        fine_tuning_job_id = d.pop("fine_tuning_job_id")

        delete_finetuning_job_request = cls(
            project_id=project_id,
            fine_tuning_job_id=fine_tuning_job_id,
        )

        delete_finetuning_job_request.additional_properties = d
        return delete_finetuning_job_request

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
