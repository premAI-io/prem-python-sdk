from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.fine_tuning_job_details_request import FineTuningJobDetailsRequest
from ...models.fine_tuning_job_response import FineTuningJobResponse
from ...models.v1_finetuning_job_details_create_response_404 import V1FinetuningJobDetailsCreateResponse404

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[FineTuningJobDetailsRequest],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/finetuning_job_details",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[Union[FineTuningJobResponse, V1FinetuningJobDetailsCreateResponse404]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FineTuningJobResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[Union[FineTuningJobResponse, V1FinetuningJobDetailsCreateResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_finetuning_job_details_create_wrapper(client):
    def v1_finetuning_job_details_create_wrapped(
        **body: Unpack[FineTuningJobDetailsRequest],
    ) -> Union[FineTuningJobResponse, V1FinetuningJobDetailsCreateResponse404]:
        """Get details for a fine-tuning job

        Args:
            body (FineTuningJobDetailsRequest):
            body (FineTuningJobDetailsRequest):
            body (FineTuningJobDetailsRequest):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[FineTuningJobResponse, V1FinetuningJobDetailsCreateResponse404]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_finetuning_job_details_create_wrapped
