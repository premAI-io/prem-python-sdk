from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any

from ... import errors
from ...models.api_response_validation_error import APIResponseValidationError
from ...models.authentication_error import AuthenticationError
from ...models.catch_all_error import CatchAllError
from ...models.conflict_error import ConflictError
from ...models.model_not_found_error import ModelNotFoundError
from ...models.permission_denied_error import PermissionDeniedError
from ...models.provider_api_connection_error import ProviderAPIConnectionError
from ...models.provider_api_status_error import ProviderAPIStatusError
from ...models.provider_api_timeout_error import ProviderAPITimeoutError
from ...models.provider_internal_server_error import ProviderInternalServerError
from ...models.provider_not_found_error import ProviderNotFoundError
from ...models.rate_limit_error import RateLimitError
from ...models.retrieve_fine_tuning_response import RetrieveFineTuningResponse
from ...models.unprocessable_entity_error import UnprocessableEntityError
from ...models.validation_error import ValidationError

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/finetuning/{job_id}",
    }

    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[
    Union[
        AuthenticationError,
        ConflictError,
        PermissionDeniedError,
        RateLimitError,
        RetrieveFineTuningResponse,
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
        response_200 = RetrieveFineTuningResponse.from_dict(response.json())

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
        PermissionDeniedError,
        RateLimitError,
        RetrieveFineTuningResponse,
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


def v1_finetuning_retrieve_wrapper(client):
    def v1_finetuning_retrieve_wrapped(
        job_id: str,
    ) -> Union[
        AuthenticationError,
        ConflictError,
        PermissionDeniedError,
        RateLimitError,
        RetrieveFineTuningResponse,
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
        """Retrieve a finetuning job.

        Args:
            job_id (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[AuthenticationError, ConflictError, PermissionDeniedError, RateLimitError, RetrieveFineTuningResponse, Union['APIResponseValidationError', 'CatchAllError', 'ProviderAPIConnectionError', 'ProviderAPIStatusError', 'ProviderAPITimeoutError', 'ProviderInternalServerError'], Union['ModelNotFoundError', 'ProviderNotFoundError'], UnprocessableEntityError, ValidationError]]
        """

        kwargs = _get_kwargs(
            job_id=job_id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_finetuning_retrieve_wrapped
