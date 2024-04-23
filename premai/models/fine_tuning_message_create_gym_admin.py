from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..types import Unset

T = TypeVar("T", bound="FineTuningMessageCreateGymAdmin")


class FineTuningMessageCreateGymAdminDict(TypedDict):
    id: int
    fine_tuning_request: int
    title: str
    message: str
    pass


@_attrs_define
class FineTuningMessageCreateGymAdmin:
    """
    Attributes:
        id (int):
        fine_tuning_request (int):
        title (str):
        message (str):
    """

    id: int
    fine_tuning_request: int
    title: str
    message: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        fine_tuning_request = self.fine_tuning_request

        title = self.title

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fine_tuning_request": fine_tuning_request,
                "title": title,
                "message": message,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        id = self.id if isinstance(self.id, Unset) else (None, str(self.id).encode(), "text/plain")

        fine_tuning_request = (
            self.fine_tuning_request
            if isinstance(self.fine_tuning_request, Unset)
            else (None, str(self.fine_tuning_request).encode(), "text/plain")
        )

        title = self.title if isinstance(self.title, Unset) else (None, str(self.title).encode(), "text/plain")

        message = self.message if isinstance(self.message, Unset) else (None, str(self.message).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "id": id,
                "fine_tuning_request": fine_tuning_request,
                "title": title,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        fine_tuning_request = d.pop("fine_tuning_request")

        title = d.pop("title")

        message = d.pop("message")

        fine_tuning_message_create_gym_admin = cls(
            id=id,
            fine_tuning_request=fine_tuning_request,
            title=title,
            message=message,
        )

        fine_tuning_message_create_gym_admin.additional_properties = d
        return fine_tuning_message_create_gym_admin

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
