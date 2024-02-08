from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveFineTuningResponse")


class RetrieveFineTuningResponseDict(TypedDict):
    id: str
    fine_tuned_model: str
    created_at: int
    status: str
    provider_name: str
    provider_id: str
    status_code: int
    finished_at: NotRequired[Union[Unset, int]]
    error: NotRequired[Union[Unset, str]]
    pass


@_attrs_define
class RetrieveFineTuningResponse:
    """
    Attributes:
        id (str): The ID of the fine-tuning job.
        fine_tuned_model (str): The ID of the fine-tuned model.
        created_at (int): The Unix timestamp (in seconds) of when the fine-tuning job was created.
        status (str): The status of the fine-tuning job.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        status_code (int): The status code of the fine-tuning job.
        finished_at (Union[Unset, int]): The Unix timestamp (in seconds) of when the fine-tuning job was finished.
        error (Union[Unset, str]): The error message of the fine-tuning job.
    """

    id: str
    fine_tuned_model: str
    created_at: int
    status: str
    provider_name: str
    provider_id: str
    status_code: int
    finished_at: Union[Unset, int] = UNSET
    error: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        fine_tuned_model = self.fine_tuned_model

        created_at = self.created_at

        status = self.status

        provider_name = self.provider_name

        provider_id = self.provider_id

        status_code = self.status_code

        finished_at = self.finished_at

        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fine_tuned_model": fine_tuned_model,
                "created_at": created_at,
                "status": status,
                "provider_name": provider_name,
                "provider_id": provider_id,
                "status_code": status_code,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        fine_tuned_model = d.pop("fine_tuned_model")

        created_at = d.pop("created_at")

        status = d.pop("status")

        provider_name = d.pop("provider_name")

        provider_id = d.pop("provider_id")

        status_code = d.pop("status_code")

        finished_at = d.pop("finished_at", UNSET)

        error = d.pop("error", UNSET)

        retrieve_fine_tuning_response = cls(
            id=id,
            fine_tuned_model=fine_tuned_model,
            created_at=created_at,
            status=status,
            provider_name=provider_name,
            provider_id=provider_id,
            status_code=status_code,
            finished_at=finished_at,
            error=error,
        )

        retrieve_fine_tuning_response.additional_properties = d
        return retrieve_fine_tuning_response

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
