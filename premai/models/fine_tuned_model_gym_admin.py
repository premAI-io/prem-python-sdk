from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.blank_enum import BlankEnum
from ..models.model_provider_enum import ModelProviderEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="FineTunedModelGymAdmin")


class FineTunedModelGymAdminDict(TypedDict):
    id: int
    slug: str
    alias: NotRequired[Union[None, Unset, str]]
    model_provider: NotRequired[Union[BlankEnum, ModelProviderEnum, None, Unset]]
    pass


@_attrs_define
class FineTunedModelGymAdmin:
    """
    Attributes:
        id (int):
        slug (str):
        alias (Union[None, Unset, str]):
        model_provider (Union[BlankEnum, ModelProviderEnum, None, Unset]):
    """

    id: int
    slug: str
    alias: Union[None, Unset, str] = UNSET
    model_provider: Union[BlankEnum, ModelProviderEnum, None, Unset] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        slug = self.slug

        alias: Union[None, Unset, str]
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        model_provider: Union[None, Unset, str]
        if isinstance(self.model_provider, Unset):
            model_provider = UNSET
        elif isinstance(self.model_provider, ModelProviderEnum):
            model_provider = self.model_provider.value
        elif isinstance(self.model_provider, BlankEnum):
            model_provider = self.model_provider.value
        else:
            model_provider = self.model_provider

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if model_provider is not UNSET:
            field_dict["model_provider"] = model_provider

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy() if src_dict else {}
        id = d.pop("id")

        slug = d.pop("slug")

        def _parse_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alias = _parse_alias(d.pop("alias", UNSET))

        def _parse_model_provider(data: object) -> Union[BlankEnum, ModelProviderEnum, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_provider_type_0 = ModelProviderEnum(data)

                return model_provider_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_provider_type_1 = BlankEnum(data)

                return model_provider_type_1
            except:  # noqa: E722
                pass
            return cast(Union[BlankEnum, ModelProviderEnum, None, Unset], data)

        model_provider = _parse_model_provider(d.pop("model_provider", UNSET))

        fine_tuned_model_gym_admin = cls(
            id=id,
            slug=slug,
            alias=alias,
            model_provider=model_provider,
        )

        fine_tuned_model_gym_admin.additional_properties = d
        return fine_tuned_model_gym_admin

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
