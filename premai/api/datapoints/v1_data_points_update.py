from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.v1_data_points_update_json_body import V1DataPointsUpdateJsonBody
from ...models.v1_data_points_update_response_200 import V1DataPointsUpdateResponse200

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: int,
    **body: Unpack[V1DataPointsUpdateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/v1/data-points/{id}/",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[V1DataPointsUpdateResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = V1DataPointsUpdateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[V1DataPointsUpdateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_data_points_update_wrapper(client):
    def v1_data_points_update_wrapped(
        id: int,
        **body: Unpack[V1DataPointsUpdateJsonBody],
    ) -> V1DataPointsUpdateResponse200:
        """
        Args:
            id (int):
            body (V1DataPointsUpdateJsonBody):
            body (V1DataPointsUpdateDataBody):
            body (V1DataPointsUpdateFilesBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[V1DataPointsUpdateResponse200]
        """

        kwargs = _get_kwargs(
            id=id,
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_data_points_update_wrapped
