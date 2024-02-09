from typing import Dict, List, Type, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

T = TypeVar("T", bound="EmbeddingsResponseDataItem")


class EmbeddingsResponseDataItemDict(TypedDict):
    index: int
    embedding: List[float]
    pass


@_attrs_define
class EmbeddingsResponseDataItem:
    """
    Attributes:
        index (int): The index of the token in the input.
        embedding (List[float]): The embedding for the input.
    """

    index: int
    embedding: List[float]

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        index = self.index

        embedding = self.embedding

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "embedding": embedding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        index = d.pop("index")

        embedding = cast(List[float], d.pop("embedding"))

        embeddings_response_data_item = cls(
            index=index,
            embedding=embedding,
        )

        embeddings_response_data_item.additional_properties = d
        return embeddings_response_data_item

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
