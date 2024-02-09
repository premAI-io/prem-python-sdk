from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChatCompletionResponseUsage")


class ChatCompletionResponseUsageDict(TypedDict):
    completion_tokens: NotRequired[Union[Unset, int]]
    prompt_tokens: NotRequired[Union[Unset, int]]
    total_tokens: NotRequired[Union[Unset, int]]
    pass


@_attrs_define
class ChatCompletionResponseUsage:
    """The usage statistics for the completion.

    Attributes:
        completion_tokens (Union[Unset, int]):
        prompt_tokens (Union[Unset, int]):
        total_tokens (Union[Unset, int]):
    """

    completion_tokens: Union[Unset, int] = UNSET
    prompt_tokens: Union[Unset, int] = UNSET
    total_tokens: Union[Unset, int] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        completion_tokens = self.completion_tokens

        prompt_tokens = self.prompt_tokens

        total_tokens = self.total_tokens

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        completion_tokens = d.pop("completion_tokens", UNSET)

        prompt_tokens = d.pop("prompt_tokens", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        chat_completion_response_usage = cls(
            completion_tokens=completion_tokens,
            prompt_tokens=prompt_tokens,
            total_tokens=total_tokens,
        )

        chat_completion_response_usage.additional_properties = d
        return chat_completion_response_usage

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
