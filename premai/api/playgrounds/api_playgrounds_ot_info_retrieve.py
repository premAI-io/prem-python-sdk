from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any

from ... import errors

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    sharable_playground_uuid: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/playgrounds/ot-info/{sharable_playground_uuid}",
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def api_playgrounds_ot_info_retrieve_wrapper(client):
    def api_playgrounds_ot_info_retrieve_wrapped(
        sharable_playground_uuid: str,
    ) -> Any:
        """
        Args:
            sharable_playground_uuid (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Any]
        """

        kwargs = _get_kwargs(
            sharable_playground_uuid=sharable_playground_uuid,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return api_playgrounds_ot_info_retrieve_wrapped
