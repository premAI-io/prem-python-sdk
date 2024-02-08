from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="V1FinetuningCreateResponse400DetailsAdditionalPropertyErrorMessagesItem")


class V1FinetuningCreateResponse400DetailsAdditionalPropertyErrorMessagesItemDict(TypedDict):
    pass


@_attrs_define
class V1FinetuningCreateResponse400DetailsAdditionalPropertyErrorMessagesItem:
    """ """

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        v1_finetuning_create_response_400_details_additional_property_error_messages_item = cls()

        v1_finetuning_create_response_400_details_additional_property_error_messages_item.additional_properties = d
        return v1_finetuning_create_response_400_details_additional_property_error_messages_item

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
