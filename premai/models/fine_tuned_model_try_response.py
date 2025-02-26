from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="FineTunedModelTryResponse")


class FineTunedModelTryResponseDict(TypedDict):
    success: str
    playground_url: str
    pass


@_attrs_define
class FineTunedModelTryResponse:
    """
    Attributes:
        success (str):
        playground_url (str):
    """

    success: str
    playground_url: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        success = self.success

        playground_url = self.playground_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "playground_url": playground_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        success = d.pop("success")

        playground_url = d.pop("playground_url")

        fine_tuned_model_try_response = cls(
            success=success,
            playground_url=playground_url,
        )

        fine_tuned_model_try_response.additional_properties = d
        return fine_tuned_model_try_response

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
