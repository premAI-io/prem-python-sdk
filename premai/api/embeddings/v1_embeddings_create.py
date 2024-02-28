from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.api_response_validation_error import APIResponseValidationError
from ...models.authentication_error import AuthenticationError
from ...models.catch_all_error import CatchAllError
from ...models.conflict_error import ConflictError
from ...models.embeddings_input import EmbeddingsInput
from ...models.embeddings_response import EmbeddingsResponse
from ...models.model_not_found_error import ModelNotFoundError
from ...models.permission_denied_error import PermissionDeniedError
from ...models.provider_api_connection_error import ProviderAPIConnectionError
from ...models.provider_api_status_error import ProviderAPIStatusError
from ...models.provider_api_timeout_error import ProviderAPITimeoutError
from ...models.provider_internal_server_error import ProviderInternalServerError
from ...models.provider_not_found_error import ProviderNotFoundError
from ...models.rate_limit_error import RateLimitError
from ...models.unprocessable_entity_error import UnprocessableEntityError
from ...models.validation_error import ValidationError

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[EmbeddingsInput],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/embeddings",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[
    Union[
        AuthenticationError,
        ConflictError,
        EmbeddingsResponse,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EmbeddingsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[
    Union[
        AuthenticationError,
        ConflictError,
        EmbeddingsResponse,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_embeddings_create_wrapper(client):
    def v1_embeddings_create_wrapped(
        **body: Unpack[EmbeddingsInput],
    ) -> Union[
        AuthenticationError,
        ConflictError,
        EmbeddingsResponse,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]:
        """Creates embeddings for the given input.

        Args:
            body (EmbeddingsInput):
            body (EmbeddingsInput):
            body (EmbeddingsInput):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[AuthenticationError, ConflictError, EmbeddingsResponse, PermissionDeniedError, RateLimitError, Union['APIResponseValidationError', 'CatchAllError', 'ProviderAPIConnectionError', 'ProviderAPIStatusError', 'ProviderAPITimeoutError', 'ProviderInternalServerError'], Union['ModelNotFoundError', 'ProviderNotFoundError'], UnprocessableEntityError, ValidationError]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_embeddings_create_wrapped
