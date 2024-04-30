from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any

from ... import errors
from ...models.trace_retrieve import TraceRetrieve

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/traces/{id}/",
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[TraceRetrieve]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TraceRetrieve.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[TraceRetrieve]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_traces_retrieve_wrapper(client):
    def v1_traces_retrieve_wrapped(
        id: str,
    ) -> TraceRetrieve:
        """
        Args:
            id (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[TraceRetrieve]
        """

        kwargs = _get_kwargs(
            id=id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_traces_retrieve_wrapped
