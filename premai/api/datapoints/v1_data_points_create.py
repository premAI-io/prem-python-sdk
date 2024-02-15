from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.v1_data_points_create_json_body import V1DataPointsCreateJsonBody
from ...models.v1_data_points_create_response_201 import V1DataPointsCreateResponse201

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[V1DataPointsCreateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/data-points/",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[V1DataPointsCreateResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = V1DataPointsCreateResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[V1DataPointsCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_data_points_create_wrapper(client):
    def v1_data_points_create_wrapped(
        **body: Unpack[V1DataPointsCreateJsonBody],
    ) -> V1DataPointsCreateResponse201:
        """
        Args:
            body (V1DataPointsCreateJsonBody):
            body (V1DataPointsCreateDataBody):
            body (V1DataPointsCreateFilesBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[V1DataPointsCreateResponse201]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_data_points_create_wrapped