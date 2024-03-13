from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="Enhancement")


class EnhancementDict(TypedDict):
    ids: NotRequired[Union[Unset, List[int]]]
    limit: NotRequired[Union[Unset, int]]
    similarity_threshold: NotRequired[Union[Unset, float]]
    pass


@_attrs_define
class Enhancement:
    """
    Attributes:
        ids (Union[Unset, List[int]]): The IDs of the repositories to use.
        limit (Union[Unset, int]):
        similarity_threshold (Union[Unset, float]):
    """

    ids: Union[Unset, List[int]] = UNSET
    limit: Union[Unset, int] = UNSET
    similarity_threshold: Union[Unset, float] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        limit = self.limit

        similarity_threshold = self.similarity_threshold

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if limit is not UNSET:
            field_dict["limit"] = limit
        if similarity_threshold is not UNSET:
            field_dict["similarity_threshold"] = similarity_threshold

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        ids = cast(List[int], d.pop("ids", UNSET))

        limit = d.pop("limit", UNSET)

        similarity_threshold = d.pop("similarity_threshold", UNSET)

        enhancement = cls(
            ids=ids,
            limit=limit,
            similarity_threshold=similarity_threshold,
        )

        enhancement.additional_properties = d
        return enhancement

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
