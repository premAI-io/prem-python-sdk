from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..types import Unset

T = TypeVar("T", bound="FineTuningRequestChangeStateGymAdmin")


class FineTuningRequestChangeStateGymAdminDict(TypedDict):
    fine_tuning_request: int
    id: int
    pass


@_attrs_define
class FineTuningRequestChangeStateGymAdmin:
    """
    Attributes:
        fine_tuning_request (int): Finetuning_request id to be updated
        id (int): Updated Fine-tuning request id
    """

    fine_tuning_request: int
    id: int

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fine_tuning_request = self.fine_tuning_request

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fine_tuning_request": fine_tuning_request,
                "id": id,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        fine_tuning_request = (
            self.fine_tuning_request
            if isinstance(self.fine_tuning_request, Unset)
            else (None, str(self.fine_tuning_request).encode(), "text/plain")
        )

        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "fine_tuning_request": fine_tuning_request,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        fine_tuning_request = d.pop("fine_tuning_request")

        id = d.pop("id")

        fine_tuning_request_change_state_gym_admin = cls(
            fine_tuning_request=fine_tuning_request,
            id=id,
        )

        fine_tuning_request_change_state_gym_admin.additional_properties = d
        return fine_tuning_request_change_state_gym_admin

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
