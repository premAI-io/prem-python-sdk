from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.feedback_create import FeedbackCreate

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[FeedbackCreate],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/set_trace_feedback",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[FeedbackCreate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FeedbackCreate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[FeedbackCreate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_set_trace_feedback_create_wrapper(client):
    def v1_set_trace_feedback_create_wrapped(
        **body: Unpack[FeedbackCreate],
    ) -> FeedbackCreate:
        """Set trace feedback

        Args:
            body (FeedbackCreate):
            body (FeedbackCreate):
            body (FeedbackCreate):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[FeedbackCreate]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_set_trace_feedback_create_wrapped
