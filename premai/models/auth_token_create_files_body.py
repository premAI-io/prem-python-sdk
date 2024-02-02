from typing import Dict, List, Type

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Any, TypedDict, TypeVar

from ..types import Unset

T = TypeVar("T", bound="AuthTokenCreateFilesBody")


class AuthTokenCreateFilesBodyDict(TypedDict):
    username: str
    password: str
    token: str
    pass


@_attrs_define
class AuthTokenCreateFilesBody:
    """
    Attributes:
        username (str):
        password (str):
        token (str):
    """

    username: str
    password: str
    token: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username

        password = self.password

        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
                "token": token,
            }
        )

        return field_dict

    def to_multipart(self) -> Dict[str, Any]:
        username = (
            self.username if isinstance(self.username, Unset) else (None, str(self.username).encode(), "text/plain")
        )

        password = (
            self.password if isinstance(self.password, Unset) else (None, str(self.password).encode(), "text/plain")
        )

        token = self.token if isinstance(self.token, Unset) else (None, str(self.token).encode(), "text/plain")

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {key: (None, str(value).encode(), "text/plain") for key, value in self.additional_properties.items()}
        )
        field_dict.update(
            {
                "username": username,
                "password": password,
                "token": token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        token = d.pop("token")

        auth_token_create_files_body = cls(
            username=username,
            password=password,
            token=token,
        )

        auth_token_create_files_body.additional_properties = d
        return auth_token_create_files_body

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
