from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.v1_finetuning_create_data_body_training_data_item import V1FinetuningCreateDataBodyTrainingDataItem
from ..models.v1_finetuning_create_data_body_validaton_data_item import V1FinetuningCreateDataBodyValidatonDataItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1FinetuningCreateDataBody")


class V1FinetuningCreateDataBodyDict(TypedDict):
    project_id: int
    training_data: List["V1FinetuningCreateDataBodyTrainingDataItem"]
    model: NotRequired[Union[Unset, str]]
    validaton_data: NotRequired[Union[Unset, List["V1FinetuningCreateDataBodyValidatonDataItem"]]]
    num_epochs: Union[Unset, int] = 1
    pass


@_attrs_define
class V1FinetuningCreateDataBody:
    """
    Attributes:
        project_id (int): The ID of the project to use.
        training_data (List['V1FinetuningCreateDataBodyTrainingDataItem']): The training file.
        model (Union[Unset, str]): ID of the model to use. See the model endpoint compatibility table for details.
        validaton_data (Union[Unset, List['V1FinetuningCreateDataBodyValidatonDataItem']]): The training file.
        num_epochs (Union[Unset, int]): The number of epochs to train for. Default: 1.
    """

    project_id: int
    training_data: List["V1FinetuningCreateDataBodyTrainingDataItem"]
    model: Union[Unset, str] = UNSET
    validaton_data: Union[Unset, List["V1FinetuningCreateDataBodyValidatonDataItem"]] = UNSET
    num_epochs: Union[Unset, int] = 1

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id

        training_data = []
        for training_data_item_data in self.training_data:
            training_data_item = training_data_item_data.to_dict()
            training_data.append(training_data_item)

        model = self.model

        validaton_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.validaton_data, Unset):
            validaton_data = []
            for validaton_data_item_data in self.validaton_data:
                validaton_data_item = validaton_data_item_data.to_dict()
                validaton_data.append(validaton_data_item)

        num_epochs = self.num_epochs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "training_data": training_data,
            }
        )
        if model is not UNSET:
            field_dict["model"] = model
        if validaton_data is not UNSET:
            field_dict["validaton_data"] = validaton_data
        if num_epochs is not UNSET:
            field_dict["num_epochs"] = num_epochs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v1_finetuning_create_data_body_training_data_item import (
            V1FinetuningCreateDataBodyTrainingDataItem,
        )
        from ..models.v1_finetuning_create_data_body_validaton_data_item import (
            V1FinetuningCreateDataBodyValidatonDataItem,
        )

        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        training_data = []
        _training_data = d.pop("training_data")
        for training_data_item_data in _training_data:
            training_data_item = V1FinetuningCreateDataBodyTrainingDataItem.from_dict(training_data_item_data)

            training_data.append(training_data_item)

        model = d.pop("model", UNSET)

        validaton_data = []
        _validaton_data = d.pop("validaton_data", UNSET)
        for validaton_data_item_data in _validaton_data or []:
            validaton_data_item = V1FinetuningCreateDataBodyValidatonDataItem.from_dict(validaton_data_item_data)

            validaton_data.append(validaton_data_item)

        num_epochs = d.pop("num_epochs", UNSET)

        v1_finetuning_create_data_body = cls(
            project_id=project_id,
            training_data=training_data,
            model=model,
            validaton_data=validaton_data,
            num_epochs=num_epochs,
        )

        v1_finetuning_create_data_body.additional_properties = d
        return v1_finetuning_create_data_body

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
