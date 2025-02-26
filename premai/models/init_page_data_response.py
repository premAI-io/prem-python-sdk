from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.fine_tuning_job_response import FineTuningJobResponse

T = TypeVar("T", bound="InitPageDataResponse")


class InitPageDataResponseDict(TypedDict):
    ft_jobs: List["FineTuningJobResponse"]
    pass


@_attrs_define
class InitPageDataResponse:
    """
    Attributes:
        ft_jobs (List['FineTuningJobResponse']):
    """

    ft_jobs: List["FineTuningJobResponse"]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ft_jobs = []
        for ft_jobs_item_data in self.ft_jobs:
            ft_jobs_item = ft_jobs_item_data.to_dict()
            ft_jobs.append(ft_jobs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ftJobs": ft_jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fine_tuning_job_response import FineTuningJobResponse

        d = src_dict.copy() if src_dict else {}
        ft_jobs = []
        _ft_jobs = d.pop("ftJobs")
        for ft_jobs_item_data in _ft_jobs:
            ft_jobs_item = FineTuningJobResponse.from_dict(ft_jobs_item_data)

            ft_jobs.append(ft_jobs_item)

        init_page_data_response = cls(
            ft_jobs=ft_jobs,
        )

        init_page_data_response.additional_properties = d
        return init_page_data_response

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
