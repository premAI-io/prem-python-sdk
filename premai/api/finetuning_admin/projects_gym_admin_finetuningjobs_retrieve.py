from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any

from ... import errors
from ...models.fine_tuning_job_output_gym_admin import FineTuningJobOutputGymAdmin

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/projects/gym/admin/finetuningjobs/{id}/",
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[FineTuningJobOutputGymAdmin]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FineTuningJobOutputGymAdmin.from_dict(response.json())

        return response_200
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


def projects_gym_admin_finetuningjobs_retrieve_wrapper(client):
    def projects_gym_admin_finetuningjobs_retrieve_wrapped(
        id: int,
    ) -> FineTuningJobOutputGymAdmin:
        """Manage finetuning_jobs

        Args:
            id (int):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[FineTuningJobOutputGymAdmin]
        """

        kwargs = _get_kwargs(
            id=id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return projects_gym_admin_finetuningjobs_retrieve_wrapped
