from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.v1_embeddings_create_data_body_encoding_format import V1EmbeddingsCreateDataBodyEncodingFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V1EmbeddingsCreateDataBody")


class V1EmbeddingsCreateDataBodyDict(TypedDict):
    project_id: int
    model: str
    input_: List[Union[List[List[int]], List[int], List[str], str]]
    encoding_format: NotRequired[Union[Unset, V1EmbeddingsCreateDataBodyEncodingFormat]]
    pass


@_attrs_define
class V1EmbeddingsCreateDataBody:
    """
    Attributes:
        project_id (int): The ID of the project to use.
        model (str): The model to generate the embeddings.
        input_ (List[Union[List[List[int]], List[int], List[str], str]]): Embedding Input
        encoding_format (Union[Unset, V1EmbeddingsCreateDataBodyEncodingFormat]):
    """

    project_id: int
    model: str
    input_: List[Union[List[List[int]], List[int], List[str], str]]
    encoding_format: Union[Unset, "V1EmbeddingsCreateDataBodyEncodingFormat"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        project_id = self.project_id

        model = self.model

        input_ = []
        for input_item_data in self.input_:
            input_item: Union[List[List[int]], List[int], List[str], str]
            if isinstance(input_item_data, list):
                input_item = input_item_data

            elif isinstance(input_item_data, list):
                input_item = input_item_data

            elif isinstance(input_item_data, list):
                input_item = []
                for input_item_type_3_item_data in input_item_data:
                    input_item_type_3_item = input_item_type_3_item_data

                    input_item.append(input_item_type_3_item)

            else:
                input_item = input_item_data
            input_.append(input_item)

        encoding_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.encoding_format, Unset):
            encoding_format = self.encoding_format.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "project_id": project_id,
                "model": model,
                "input": input_,
            }
        )
        if encoding_format is not UNSET:
            field_dict["encoding_format"] = encoding_format

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.v1_embeddings_create_data_body_encoding_format import V1EmbeddingsCreateDataBodyEncodingFormat

        d = src_dict.copy() if src_dict else {}
        project_id = d.pop("project_id")

        model = d.pop("model")

        input_ = []
        _input_ = d.pop("input")
        for input_item_data in _input_:

            def _parse_input_item(data: object) -> Union[List[List[int]], List[int], List[str], str]:
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    input_item_type_1 = cast(List[str], data)

                    return input_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    input_item_type_2 = cast(List[int], data)

                    return input_item_type_2
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, list):
                        raise TypeError()
                    input_item_type_3 = []
                    _input_item_type_3 = data
                    for input_item_type_3_item_data in _input_item_type_3:
                        input_item_type_3_item = cast(List[int], input_item_type_3_item_data)

                        input_item_type_3.append(input_item_type_3_item)

                    return input_item_type_3
                except:  # noqa: E722
                    pass
                return cast(Union[List[List[int]], List[int], List[str], str], data)

            input_item = _parse_input_item(input_item_data)

            input_.append(input_item)

        _encoding_format = d.pop("encoding_format", UNSET)
        encoding_format: Union[Unset, V1EmbeddingsCreateDataBodyEncodingFormat]
        if isinstance(_encoding_format, Unset):
            encoding_format = UNSET
        else:
            encoding_format = V1EmbeddingsCreateDataBodyEncodingFormat.from_dict(_encoding_format)

        v1_embeddings_create_data_body = cls(
            project_id=project_id,
            model=model,
            input_=input_,
            encoding_format=encoding_format,
        )

        v1_embeddings_create_data_body.additional_properties = d
        return v1_embeddings_create_data_body

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
