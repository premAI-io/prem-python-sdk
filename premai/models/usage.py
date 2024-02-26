from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="Usage")


class UsageDict(TypedDict):
    prompt_tokens: int
    total_tokens: int
    completion_tokens: NotRequired[Union[Unset, int]]
    pass


@_attrs_define
class Usage:
    """
    Attributes:
        prompt_tokens (int):
        total_tokens (int):
        completion_tokens (Union[Unset, int]):
    """

    prompt_tokens: int
    total_tokens: int
    completion_tokens: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        prompt_tokens = self.prompt_tokens

        total_tokens = self.total_tokens

        completion_tokens = self.completion_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
            }
        )
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        prompt_tokens = d.pop("prompt_tokens")

        total_tokens = d.pop("total_tokens")

        completion_tokens = d.pop("completion_tokens", UNSET)

        usage = cls(
            prompt_tokens=prompt_tokens,
            total_tokens=total_tokens,
            completion_tokens=completion_tokens,
        )

        usage.additional_properties = d
        return usage

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
