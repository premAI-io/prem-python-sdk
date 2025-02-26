from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.fine_tuning_job_create import FineTuningJobCreate
from ...models.fine_tuning_job_create_response import FineTuningJobCreateResponse

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[FineTuningJobCreate],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/create_finetuning_job",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[FineTuningJobCreateResponse]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FineTuningJobCreateResponse.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[FineTuningJobCreateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_create_finetuning_job_create_wrapper(client):
    def v1_create_finetuning_job_create_wrapped(
        **body: Unpack[FineTuningJobCreate],
    ) -> FineTuningJobCreateResponse:
        """Creates a finetuning job for the given project and model.

        Args:
            body (FineTuningJobCreate):
            body (FineTuningJobCreate):
            body (FineTuningJobCreate):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[FineTuningJobCreateResponse]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_create_finetuning_job_create_wrapped
