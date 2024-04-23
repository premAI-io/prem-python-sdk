from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.fine_tuning_job_create_gym_admin import FineTuningJobCreateGymAdmin
from ...models.fine_tuning_job_output_gym_admin import FineTuningJobOutputGymAdmin

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[FineTuningJobCreateGymAdmin],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/projects/gym/admin/finetuningjobs/",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[FineTuningJobOutputGymAdmin]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = FineTuningJobOutputGymAdmin.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[FineTuningJobOutputGymAdmin]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def projects_gym_admin_finetuningjobs_create_wrapper(client):
    def projects_gym_admin_finetuningjobs_create_wrapped(
        **body: Unpack[FineTuningJobCreateGymAdmin],
    ) -> FineTuningJobOutputGymAdmin:
        """Create a new finetuning job given the finetuning_request id,tranining_dataset id (optional, default
        is the finetuning_request dataset), eventually the validation_dataset id and hyperparameters:
        num_epochs

        Args:
            body (FineTuningJobCreateGymAdmin):
            body (FineTuningJobCreateGymAdmin):
            body (FineTuningJobCreateGymAdmin):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[FineTuningJobOutputGymAdmin]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return projects_gym_admin_finetuningjobs_create_wrapped
