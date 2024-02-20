from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.validation_error_code_enum import ValidationErrorCodeEnum
from ..models.validation_error_details import ValidationErrorDetails

T = TypeVar("T", bound="ValidationError")


class ValidationErrorDict(TypedDict):
    message: str
    details: "ValidationErrorDetails"
    code: ValidationErrorCodeEnum
    pass


@_attrs_define
class ValidationError:
    """
    Attributes:
        message (str): A description of the validation error.
        details (ValidationErrorDetails): Detailed information about the validation errors.
        code (ValidationErrorCodeEnum): * `ValidationError` - ValidationError
    """

    message: str
    details: "ValidationErrorDetails"
    code: ValidationErrorCodeEnum

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message

        details = self.details.to_dict()

        code = self.code.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
                "details": details,
                "code": code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.validation_error_details import ValidationErrorDetails

        d = src_dict.copy() if src_dict else {}
        message = d.pop("message")

        details = ValidationErrorDetails.from_dict(d.pop("details"))

        code = ValidationErrorCodeEnum(d.pop("code"))

        validation_error = cls(
            message=message,
            details=details,
            code=code,
        )

        validation_error.additional_properties = d
        return validation_error

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
