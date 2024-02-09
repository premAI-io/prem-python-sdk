from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.api_projects_traces_create_json_body import ApiProjectsTracesCreateJsonBody
from ...models.api_projects_traces_create_response_201 import ApiProjectsTracesCreateResponse201

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[ApiProjectsTracesCreateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/projects/traces/",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[ApiProjectsTracesCreateResponse201]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ApiProjectsTracesCreateResponse201.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[ApiProjectsTracesCreateResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def api_projects_traces_create_wrapper(client):
    def api_projects_traces_create_wrapped(
        **body: Unpack[ApiProjectsTracesCreateJsonBody],
    ) -> ApiProjectsTracesCreateResponse201:
        """
        Args:
            body (ApiProjectsTracesCreateJsonBody):
            body (ApiProjectsTracesCreateDataBody):
            body (ApiProjectsTracesCreateFilesBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[ApiProjectsTracesCreateResponse201]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return api_projects_traces_create_wrapped
