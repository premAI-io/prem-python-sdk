from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="LeaderboardItem")


class LeaderboardItemDict(TypedDict):
    provider: str
    provider_slug: str
    provider_name: str
    avg_final_score: float
    avg_tokens_per_second: float
    avg_uptime: float
    avg_uptime_score: int
    avg_tokens_score: int
    pass


@_attrs_define
class LeaderboardItem:
    """
    Attributes:
        provider (str):
        provider_slug (str):
        provider_name (str):
        avg_final_score (float):
        avg_tokens_per_second (float):
        avg_uptime (float):
        avg_uptime_score (int):
        avg_tokens_score (int):
    """

    provider: str
    provider_slug: str
    provider_name: str
    avg_final_score: float
    avg_tokens_per_second: float
    avg_uptime: float
    avg_uptime_score: int
    avg_tokens_score: int

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider = self.provider

        provider_slug = self.provider_slug

        provider_name = self.provider_name

        avg_final_score = self.avg_final_score

        avg_tokens_per_second = self.avg_tokens_per_second

        avg_uptime = self.avg_uptime

        avg_uptime_score = self.avg_uptime_score

        avg_tokens_score = self.avg_tokens_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "provider_slug": provider_slug,
                "provider_name": provider_name,
                "avg_final_score": avg_final_score,
                "avg_tokens_per_second": avg_tokens_per_second,
                "avg_uptime": avg_uptime,
                "avg_uptime_score": avg_uptime_score,
                "avg_tokens_score": avg_tokens_score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider = d.pop("provider")

        provider_slug = d.pop("provider_slug")

        provider_name = d.pop("provider_name")

        avg_final_score = d.pop("avg_final_score")

        avg_tokens_per_second = d.pop("avg_tokens_per_second")

        avg_uptime = d.pop("avg_uptime")

        avg_uptime_score = d.pop("avg_uptime_score")

        avg_tokens_score = d.pop("avg_tokens_score")

        leaderboard_item = cls(
            provider=provider,
            provider_slug=provider_slug,
            provider_name=provider_name,
            avg_final_score=avg_final_score,
            avg_tokens_per_second=avg_tokens_per_second,
            avg_uptime=avg_uptime,
            avg_uptime_score=avg_uptime_score,
            avg_tokens_score=avg_tokens_score,
        )

        leaderboard_item.additional_properties = d
        return leaderboard_item

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
