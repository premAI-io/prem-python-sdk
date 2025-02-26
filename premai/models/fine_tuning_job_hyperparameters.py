from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="FineTuningJobHyperparameters")


class FineTuningJobHyperparametersDict(TypedDict):
    batch_size: int
    learning_rate_multiplier: float
    num_epochs: int
    pass


@_attrs_define
class FineTuningJobHyperparameters:
    """
    Attributes:
        batch_size (int): Batch size for fine-tuning
        learning_rate_multiplier (float): Scaling factor for the learning rate. A smaller learning rate may be useful to
            avoid overfitting.
        num_epochs (int): Number of epochs for fine-tuning
    """

    batch_size: int
    learning_rate_multiplier: float
    num_epochs: int

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        batch_size = self.batch_size

        learning_rate_multiplier = self.learning_rate_multiplier

        num_epochs = self.num_epochs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "batch_size": batch_size,
                "learning_rate_multiplier": learning_rate_multiplier,
                "num_epochs": num_epochs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        batch_size = d.pop("batch_size")

        learning_rate_multiplier = d.pop("learning_rate_multiplier")

        num_epochs = d.pop("num_epochs")

        fine_tuning_job_hyperparameters = cls(
            batch_size=batch_size,
            learning_rate_multiplier=learning_rate_multiplier,
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
