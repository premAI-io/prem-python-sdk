from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="V1FinetuningJobDetailsCreateResponse404")


class V1FinetuningJobDetailsCreateResponse404Dict(TypedDict):
    error: NotRequired[Union[Unset, str]]
    pass


@_attrs_define
class V1FinetuningJobDetailsCreateResponse404:
    """
    Attributes:
        error (Union[Unset, str]):
    """

    error: Union[Unset, str] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        error = d.pop("error", UNSET)

        v1_finetuning_job_details_create_response_404 = cls(
            error=error,
        )

        v1_finetuning_job_details_create_response_404.additional_properties = d
        return v1_finetuning_job_details_create_response_404

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
