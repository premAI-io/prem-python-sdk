from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any

from ... import errors
from ...models.api_schema_retrieve_format import ApiSchemaRetrieveFormat
from ...models.api_schema_retrieve_lang import ApiSchemaRetrieveLang
from ...models.api_schema_retrieve_response_200 import ApiSchemaRetrieveResponse200

# from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    format_: Union[Unset, ApiSchemaRetrieveFormat] = UNSET,
    lang: Union[Unset, ApiSchemaRetrieveLang] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_lang: Union[Unset, str] = UNSET
    if not isinstance(lang, Unset):
        json_lang = lang.value

    params["lang"] = json_lang

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/schema/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[ApiSchemaRetrieveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiSchemaRetrieveResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[ApiSchemaRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def api_schema_retrieve_wrapper(client):
    def api_schema_retrieve_wrapped(
        format_: Union[Unset, ApiSchemaRetrieveFormat] = UNSET,
        lang: Union[Unset, ApiSchemaRetrieveLang] = UNSET,
    ) -> ApiSchemaRetrieveResponse200:
        """OpenApi3 schema for this API. Format can be selected via content negotiation.

        - YAML: application/vnd.oai.openapi
        - JSON: application/vnd.oai.openapi+json

        Args:
            format_ (Union[Unset, ApiSchemaRetrieveFormat]):
            lang (Union[Unset, ApiSchemaRetrieveLang]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ApiSchemaRetrieveResponse200]
        """

        kwargs = _get_kwargs(
            format_=format_,
            lang=lang,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return api_schema_retrieve_wrapped
