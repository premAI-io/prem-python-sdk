from typing import Dict, List, Type, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.v1_embeddings_create_response_200_data_item import V1EmbeddingsCreateResponse200DataItem
from ..models.v1_embeddings_create_response_200_usage import V1EmbeddingsCreateResponse200Usage
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1EmbeddingsCreateResponse200")


class V1EmbeddingsCreateResponse200Dict(TypedDict):
    data: List["V1EmbeddingsCreateResponse200DataItem"]
    model: str
    provider_name: str
    provider_id: str
    usage: NotRequired[Union[Unset, V1EmbeddingsCreateResponse200Usage]]
    pass


@_attrs_define
class V1EmbeddingsCreateResponse200:
    """
    Attributes:
        data (List['V1EmbeddingsCreateResponse200DataItem']): The embeddings for the input.
        model (str): The model to generate the embeddings.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        usage (Union[Unset, V1EmbeddingsCreateResponse200Usage]): The usage statistics for the completion.
    """

    data: List["V1EmbeddingsCreateResponse200DataItem"]
    model: str
    provider_name: str
    provider_id: str
    usage: Union[Unset, "V1EmbeddingsCreateResponse200Usage"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        model = self.model

        provider_name = self.provider_name

        provider_id = self.provider_id

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "model": model,
                "provider_name": provider_name,
                "provider_id": provider_id,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v1_embeddings_create_response_200_data_item import V1EmbeddingsCreateResponse200DataItem
        from ..models.v1_embeddings_create_response_200_usage import V1EmbeddingsCreateResponse200Usage

        d = src_dict.copy() if src_dict else {}
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = V1EmbeddingsCreateResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        model = d.pop("model")

        provider_name = d.pop("provider_name")

        provider_id = d.pop("provider_id")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, V1EmbeddingsCreateResponse200Usage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = V1EmbeddingsCreateResponse200Usage.from_dict(_usage)

        v1_embeddings_create_response_200 = cls(
            data=data,
            model=model,
            provider_name=provider_name,
            provider_id=provider_id,
            usage=usage,
        )

        v1_embeddings_create_response_200.additional_properties = d
        return v1_embeddings_create_response_200

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
