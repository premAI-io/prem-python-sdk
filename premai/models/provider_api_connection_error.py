from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.provider_api_connection_error_code_enum import ProviderAPIConnectionErrorCodeEnum

T = TypeVar("T", bound="ProviderAPIConnectionError")


class ProviderAPIConnectionErrorDict(TypedDict):
    message: str
    code: ProviderAPIConnectionErrorCodeEnum
    pass


@_attrs_define
class ProviderAPIConnectionError:
    """
    Attributes:
        message (str):
        code (ProviderAPIConnectionErrorCodeEnum): * `ProviderAPIConnectionError` - ProviderAPIConnectionError
    """

    message: str
    code: ProviderAPIConnectionErrorCodeEnum

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        code = self.code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        message = d.pop("message")

        code = ProviderAPIConnectionErrorCodeEnum(d.pop("code"))

        provider_api_connection_error = cls(
            message=message,
            code=code,
        )

        provider_api_connection_error.additional_properties = d
        return provider_api_connection_error

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
