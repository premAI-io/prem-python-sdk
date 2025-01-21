from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.message_content_type_1_item_image_url import MessageContentType1ItemImageUrl
from ..models.message_content_type_1_item_type import MessageContentType1ItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageContentType1Item")


class MessageContentType1ItemDict(TypedDict):
    type: MessageContentType1ItemType
    text: NotRequired[Union[Unset, str]]
    image_url: NotRequired[Union[Unset, MessageContentType1ItemImageUrl]]
    pass


@_attrs_define
class MessageContentType1Item:
    """
    Attributes:
        type (MessageContentType1ItemType):
        text (Union[Unset, str]):
        image_url (Union[Unset, MessageContentType1ItemImageUrl]):
    """

    type: MessageContentType1ItemType
    text: Union[Unset, str] = UNSET
    image_url: Union[Unset, "MessageContentType1ItemImageUrl"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        text = self.text

        image_url: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.image_url, Unset):
            image_url = self.image_url.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if text is not UNSET:
            field_dict["text"] = text
        if image_url is not UNSET:
            field_dict["image_url"] = image_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_content_type_1_item_image_url import MessageContentType1ItemImageUrl

        d = src_dict.copy() if src_dict else {}
        type = MessageContentType1ItemType(d.pop("type"))

        text = d.pop("text", UNSET)

        _image_url = d.pop("image_url", UNSET)
        image_url: Union[Unset, MessageContentType1ItemImageUrl]
        if isinstance(_image_url, Unset):
            image_url = UNSET
        else:
            image_url = MessageContentType1ItemImageUrl.from_dict(_image_url)

        message_content_type_1_item = cls(
            type=type,
            text=text,
            image_url=image_url,
        )

        message_content_type_1_item.additional_properties = d
        return message_content_type_1_item

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
