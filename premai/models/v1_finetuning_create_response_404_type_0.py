from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.v1_finetuning_create_response_404_type_0_code import V1FinetuningCreateResponse404Type0Code

T = TypeVar("T", bound="V1FinetuningCreateResponse404Type0")


class V1FinetuningCreateResponse404Type0Dict(TypedDict):
    message: str
    code: V1FinetuningCreateResponse404Type0Code
    pass


@_attrs_define
class V1FinetuningCreateResponse404Type0:
    """
    Attributes:
        message (str):
        code (V1FinetuningCreateResponse404Type0Code): * `ProviderNotFoundError` - ProviderNotFoundError
    """

    message: str
    code: V1FinetuningCreateResponse404Type0Code

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

        code = V1FinetuningCreateResponse404Type0Code(d.pop("code"))

        v1_finetuning_create_response_404_type_0 = cls(
            message=message,
            code=code,
        )

        v1_finetuning_create_response_404_type_0.additional_properties = d
        return v1_finetuning_create_response_404_type_0

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