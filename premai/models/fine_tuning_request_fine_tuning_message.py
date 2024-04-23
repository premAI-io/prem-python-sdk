from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningRequestFineTuningMessage")


class FineTuningRequestFineTuningMessageDict(TypedDict):
    id: int
    title: str
    message: str
    user_prompt: NotRequired[Union[None, Unset, str]]
    pass


@_attrs_define
class FineTuningRequestFineTuningMessage:
    """
    Attributes:
        id (int):
        title (str):
        message (str):
        user_prompt (Union[None, Unset, str]):
    """

    id: int
    title: str
    message: str
    user_prompt: Union[None, Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        title = self.title

        message = self.message

        user_prompt: Union[None, Unset, str]
        if isinstance(self.user_prompt, Unset):
            user_prompt = UNSET
        else:
            user_prompt = self.user_prompt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "message": message,
            }
        )
        if user_prompt is not UNSET:
            field_dict["user_prompt"] = user_prompt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        title = d.pop("title")

        message = d.pop("message")

        def _parse_user_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_prompt = _parse_user_prompt(d.pop("user_prompt", UNSET))

        fine_tuning_request_fine_tuning_message = cls(
            id=id,
            title=title,
            message=message,
            user_prompt=user_prompt,
        )

        fine_tuning_request_fine_tuning_message.additional_properties = d
        return fine_tuning_request_fine_tuning_message

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
