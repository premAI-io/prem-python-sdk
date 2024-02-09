from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.v1_finetuning_create_response_400_code import V1FinetuningCreateResponse400Code
from ..models.v1_finetuning_create_response_400_details import V1FinetuningCreateResponse400Details

T = TypeVar("T", bound="V1FinetuningCreateResponse400")


class V1FinetuningCreateResponse400Dict(TypedDict):
    message: str
    details: "V1FinetuningCreateResponse400Details"
    code: V1FinetuningCreateResponse400Code
    pass


@_attrs_define
class V1FinetuningCreateResponse400:
    """
    Attributes:
        message (str): A description of the validation error.
        details (V1FinetuningCreateResponse400Details): Detailed information about the validation errors.
        code (V1FinetuningCreateResponse400Code): * `ValidationError` - ValidationError
    """

    message: str
    details: "V1FinetuningCreateResponse400Details"
    code: V1FinetuningCreateResponse400Code

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
        from ..models.v1_finetuning_create_response_400_details import V1FinetuningCreateResponse400Details

        d = src_dict.copy() if src_dict else {}
        message = d.pop("message")

        details = V1FinetuningCreateResponse400Details.from_dict(d.pop("details"))

        code = V1FinetuningCreateResponse400Code(d.pop("code"))

        v1_finetuning_create_response_400 = cls(
            message=message,
            details=details,
            code=code,
        )

        v1_finetuning_create_response_400.additional_properties = d
        return v1_finetuning_create_response_400

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
