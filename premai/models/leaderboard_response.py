from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.leaderboard_response_leaderboard_item import LeaderboardResponseLeaderboardItem

T = TypeVar("T", bound="LeaderboardResponse")


class LeaderboardResponseDict(TypedDict):
    days: int
    leaderboard: List["LeaderboardResponseLeaderboardItem"]
    pass


@_attrs_define
class LeaderboardResponse:
    """
    Attributes:
        days (int):
        leaderboard (List['LeaderboardResponseLeaderboardItem']):
    """

    days: int
    leaderboard: List["LeaderboardResponseLeaderboardItem"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        days = self.days

        leaderboard = []
        for leaderboard_item_data in self.leaderboard:
            leaderboard_item = leaderboard_item_data.to_dict()
            leaderboard.append(leaderboard_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "days": days,
                "leaderboard": leaderboard,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.leaderboard_response_leaderboard_item import LeaderboardResponseLeaderboardItem

        d = src_dict.copy()
        days = d.pop("days")

        leaderboard = []
        _leaderboard = d.pop("leaderboard")
        for leaderboard_item_data in _leaderboard:
            leaderboard_item = LeaderboardResponseLeaderboardItem.from_dict(leaderboard_item_data)

            leaderboard.append(leaderboard_item)

        leaderboard_response = cls(
            days=days,
            leaderboard=leaderboard,
        )

        leaderboard_response.additional_properties = d
        return leaderboard_response

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
