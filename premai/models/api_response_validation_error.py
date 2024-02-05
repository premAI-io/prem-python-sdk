from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.api_response_validation_error_code import APIResponseValidationErrorCode

T = TypeVar("T", bound="APIResponseValidationError")


class APIResponseValidationErrorDict(TypedDict):
    message: str
    code: APIResponseValidationErrorCode
    pass


@_attrs_define
class APIResponseValidationError:
    """
    Attributes:
        message (str):
        code (APIResponseValidationErrorCode): * `APIResponseValidationError` - APIResponseValidationError
    """

    message: str
    code: APIResponseValidationErrorCode

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
        d = src_dict.copy()
        message = d.pop("message")

        code = APIResponseValidationErrorCode(d.pop("code"))

        api_response_validation_error = cls(
            message=message,
            code=code,
        )

        api_response_validation_error.additional_properties = d
        return api_response_validation_error

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