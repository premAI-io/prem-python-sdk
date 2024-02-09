from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.api_providers_leaderboard_retrieve_response_200_leaderboard_item import (
    ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem,
)

T = TypeVar("T", bound="ApiProvidersLeaderboardRetrieveResponse200")


class ApiProvidersLeaderboardRetrieveResponse200Dict(TypedDict):
    days: int
    leaderboard: List["ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem"]
    pass


@_attrs_define
class ApiProvidersLeaderboardRetrieveResponse200:
    """
    Attributes:
        days (int):
        leaderboard (List['ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem']):
    """

    days: int
    leaderboard: List["ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem"]

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
        from ..models.api_providers_leaderboard_retrieve_response_200_leaderboard_item import (
            ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem,
        )

        d = src_dict.copy() if src_dict else {}
        days = d.pop("days")

        leaderboard = []
        _leaderboard = d.pop("leaderboard")
        for leaderboard_item_data in _leaderboard:
            leaderboard_item = ApiProvidersLeaderboardRetrieveResponse200LeaderboardItem.from_dict(
                leaderboard_item_data
            )

            leaderboard.append(leaderboard_item)

        api_providers_leaderboard_retrieve_response_200 = cls(
            days=days,
            leaderboard=leaderboard,
        )

        api_providers_leaderboard_retrieve_response_200.additional_properties = d
        return api_providers_leaderboard_retrieve_response_200

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