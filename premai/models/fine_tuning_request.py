from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.fine_tuning_request_fine_tuning_message import FineTuningRequestFineTuningMessage
from ..models.fine_tuning_request_model import FineTuningRequestModel
from ..models.fine_tuning_request_project import FineTuningRequestProject
from ..models.status_d09_enum import StatusD09Enum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTuningRequest")


class FineTuningRequestDict(TypedDict):
    id: int
    project: "FineTuningRequestProject"
    model: "FineTuningRequestModel"
    dataset: int
    messages: List["FineTuningRequestFineTuningMessage"]
    current_message: "FineTuningRequestFineTuningMessage"
    status: NotRequired[Union[Unset, StatusD09Enum]]
    current_fine_tuning_job: NotRequired[Union[None, Unset, int]]
    pass


@_attrs_define
class FineTuningRequest:
    """
    Attributes:
        id (int):
        project (FineTuningRequestProject):
        model (FineTuningRequestModel):
        dataset (int):
        messages (List['FineTuningRequestFineTuningMessage']):
        current_message (FineTuningRequestFineTuningMessage):
        status (Union[Unset, StatusD09Enum]): * `queued` - Queued
            * `finetuning` - Fine tuning
            * `done` - Done
            * `failed` - Failed
        current_fine_tuning_job (Union[None, Unset, int]):
    """

    id: int
    project: "FineTuningRequestProject"
    model: "FineTuningRequestModel"
    dataset: int
    messages: List["FineTuningRequestFineTuningMessage"]
    current_message: "FineTuningRequestFineTuningMessage"
    status: Union[Unset, StatusD09Enum] = UNSET
    current_fine_tuning_job: Union[None, Unset, int] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        project = self.project.to_dict()

        model = self.model.to_dict()

        dataset = self.dataset

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        current_message = self.current_message.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        current_fine_tuning_job: Union[None, Unset, int]
        if isinstance(self.current_fine_tuning_job, Unset):
            current_fine_tuning_job = UNSET
        else:
            current_fine_tuning_job = self.current_fine_tuning_job

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "project": project,
                "model": model,
                "dataset": dataset,
                "messages": messages,
                "current_message": current_message,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if current_fine_tuning_job is not UNSET:
            field_dict["current_fine_tuning_job"] = current_fine_tuning_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.fine_tuning_request_fine_tuning_message import FineTuningRequestFineTuningMessage
        from ..models.fine_tuning_request_model import FineTuningRequestModel
        from ..models.fine_tuning_request_project import FineTuningRequestProject

        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        project = FineTuningRequestProject.from_dict(d.pop("project"))

        model = FineTuningRequestModel.from_dict(d.pop("model"))

        dataset = d.pop("dataset")

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = FineTuningRequestFineTuningMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        current_message = FineTuningRequestFineTuningMessage.from_dict(d.pop("current_message"))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusD09Enum]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusD09Enum(_status)

        def _parse_current_fine_tuning_job(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        current_fine_tuning_job = _parse_current_fine_tuning_job(d.pop("current_fine_tuning_job", UNSET))

        fine_tuning_request = cls(
            id=id,
            project=project,
            model=model,
            dataset=dataset,
            messages=messages,
            current_message=current_message,
            status=status,
            current_fine_tuning_job=current_fine_tuning_job,
        )

        fine_tuning_request.additional_properties = d
        return fine_tuning_request

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
