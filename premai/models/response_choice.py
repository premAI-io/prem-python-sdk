from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.message import Message
from ..models.tool_call import ToolCall
from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseChoice")


class ResponseChoiceDict(TypedDict):
    index: int
    message: "Message"
    finish_reason: str
    tool_calls: NotRequired[Union[List["ToolCall"], None, Unset]]
    pass


@_attrs_define
class ResponseChoice:
    """
    Attributes:
        index (int): The index of the choice in the list of choices.
        message (Message):
        finish_reason (str): The reason the chat completion finished, e.g., 'stop' or 'length'.
        tool_calls (Union[List['ToolCall'], None, Unset]): The tool calls made.
    """

    index: int
    message: "Message"
    finish_reason: str
    tool_calls: Union[List["ToolCall"], None, Unset] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        message = self.message.to_dict()

        finish_reason = self.finish_reason

        tool_calls: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)

        else:
            tool_calls = self.tool_calls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "message": message,
                "finish_reason": finish_reason,
            }
        )
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message import Message
        from ..models.tool_call import ToolCall

        d = src_dict.copy() if src_dict else {}
        index = d.pop("index")

        message = Message.from_dict(d.pop("message"))

        finish_reason = d.pop("finish_reason")

        def _parse_tool_calls(data: object) -> Union[List["ToolCall"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in _tool_calls_type_0:
                    tool_calls_type_0_item = ToolCall.from_dict(tool_calls_type_0_item_data)

                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ToolCall"], None, Unset], data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))

        response_choice = cls(
            index=index,
            message=message,
            finish_reason=finish_reason,
            tool_calls=tool_calls,
        )

        response_choice.additional_properties = d
        return response_choice

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
