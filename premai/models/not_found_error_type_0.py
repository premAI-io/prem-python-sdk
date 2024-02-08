from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.not_found_error_type_0_code import NotFoundErrorType0Code

T = TypeVar("T", bound="NotFoundErrorType0")


class NotFoundErrorType0Dict(TypedDict):
    message: str
    code: NotFoundErrorType0Code
    pass


@_attrs_define
class NotFoundErrorType0:
    """
    Attributes:
        message (str):
        code (NotFoundErrorType0Code): * `ProviderNotFoundError` - ProviderNotFoundError
    """

    message: str
    code: NotFoundErrorType0Code

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

        code = NotFoundErrorType0Code(d.pop("code"))

        not_found_error_type_0 = cls(
            message=message,
            code=code,
        )

        not_found_error_type_0.additional_properties = d
        return not_found_error_type_0

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
