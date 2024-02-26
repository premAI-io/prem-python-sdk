from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..models.embedding import Embedding
from ..models.usage import Usage

T = TypeVar("T", bound="EmbeddingsResponse")


class EmbeddingsResponseDict(TypedDict):
    data: List["Embedding"]
    model: str
    usage: "Usage"
    provider_name: str
    provider_id: str
    pass


@_attrs_define
class EmbeddingsResponse:
    """
    Attributes:
        data (List['Embedding']): The embeddings for the input.
        model (str): The model to generate the embeddings.
        usage (Usage):
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
    """

    data: List["Embedding"]
    model: str
    usage: "Usage"
    provider_name: str
    provider_id: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        model = self.model

        usage = self.usage.to_dict()

        provider_name = self.provider_name

        provider_id = self.provider_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "model": model,
                "usage": usage,
                "provider_name": provider_name,
                "provider_id": provider_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.embedding import Embedding
        from ..models.usage import Usage

        d = src_dict.copy() if src_dict else {}
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = Embedding.from_dict(data_item_data)

            data.append(data_item)

        model = d.pop("model")

        usage = Usage.from_dict(d.pop("usage"))

        provider_name = d.pop("provider_name")

        provider_id = d.pop("provider_id")

        embeddings_response = cls(
            data=data,
            model=model,
            usage=usage,
            provider_name=provider_name,
            provider_id=provider_id,
        )

        embeddings_response.additional_properties = d
        return embeddings_response

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
