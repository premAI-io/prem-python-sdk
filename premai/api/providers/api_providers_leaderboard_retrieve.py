from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any

from ... import errors
from ...models.api_providers_leaderboard_retrieve_response_200 import ApiProvidersLeaderboardRetrieveResponse200

# from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    days: Union[Unset, int] = 30,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/providers/leaderboard",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[ApiProvidersLeaderboardRetrieveResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiProvidersLeaderboardRetrieveResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[ApiProvidersLeaderboardRetrieveResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def api_providers_leaderboard_retrieve_wrapper(client):
    def api_providers_leaderboard_retrieve_wrapped(
        days: Union[Unset, int] = 30,
    ) -> ApiProvidersLeaderboardRetrieveResponse200:
        """
        Args:
            days (Union[Unset, int]):  Default: 30.

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ApiProvidersLeaderboardRetrieveResponse200]
        """

        kwargs = _get_kwargs(
            days=days,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return api_providers_leaderboard_retrieve_wrapped