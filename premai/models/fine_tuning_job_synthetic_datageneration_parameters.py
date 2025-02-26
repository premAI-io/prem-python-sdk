from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="FineTuningJobSyntheticDatagenerationParameters")


class FineTuningJobSyntheticDatagenerationParametersDict(TypedDict):
    run_synthetic_datageneration: bool
    min_num_datapoints_for_ft: int
    temperature: float
    positive_instructions: str
    negative_instructions: str
    pass


@_attrs_define
class FineTuningJobSyntheticDatagenerationParameters:
    """
    Attributes:
        run_synthetic_datageneration (bool): Whether to run synthetic datageneration
        min_num_datapoints_for_ft (int): Minimum number of datapoints required for fine-tuning
        temperature (float): Temperature for synthetic datageneration
        positive_instructions (str): Positive instructions for synthetic datageneration, what the datapoints should be
            about
        negative_instructions (str): Negative instructions for synthetic datageneration, what the datapoints should not
            be about
    """

    run_synthetic_datageneration: bool
    min_num_datapoints_for_ft: int
    temperature: float
    positive_instructions: str
    negative_instructions: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_synthetic_datageneration = self.run_synthetic_datageneration

        min_num_datapoints_for_ft = self.min_num_datapoints_for_ft

        temperature = self.temperature

        positive_instructions = self.positive_instructions

        negative_instructions = self.negative_instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "run_synthetic_datageneration": run_synthetic_datageneration,
                "min_num_datapoints_for_ft": min_num_datapoints_for_ft,
                "temperature": temperature,
                "positive_instructions": positive_instructions,
                "negative_instructions": negative_instructions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        run_synthetic_datageneration = d.pop("run_synthetic_datageneration")

        min_num_datapoints_for_ft = d.pop("min_num_datapoints_for_ft")

        temperature = d.pop("temperature")

        positive_instructions = d.pop("positive_instructions")

        negative_instructions = d.pop("negative_instructions")

        fine_tuning_job_synthetic_datageneration_parameters = cls(
            run_synthetic_datageneration=run_synthetic_datageneration,
            min_num_datapoints_for_ft=min_num_datapoints_for_ft,
            temperature=temperature,
            positive_instructions=positive_instructions,
            negative_instructions=negative_instructions,
        )

        fine_tuning_job_synthetic_datageneration_parameters.additional_properties = d
        return fine_tuning_job_synthetic_datageneration_parameters

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
