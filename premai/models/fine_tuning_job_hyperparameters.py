from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningJobHyperparameters")


class FineTuningJobHyperparametersDict(TypedDict):
    num_epochs: Union[Unset, int] = 3
    pass


@_attrs_define
class FineTuningJobHyperparameters:
    """
    Attributes:
        num_epochs (Union[Unset, int]): Number of epochs for fine-tuning Default: 3.
    """

    num_epochs: Union[Unset, int] = 3

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_epochs = self.num_epochs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_epochs is not UNSET:
            field_dict["num_epochs"] = num_epochs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        num_epochs = d.pop("num_epochs", UNSET)

        fine_tuning_job_hyperparameters = cls(
            num_epochs=num_epochs,
        )

        fine_tuning_job_hyperparameters.additional_properties = d
        return fine_tuning_job_hyperparameters

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
