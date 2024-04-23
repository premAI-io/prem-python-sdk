from http import HTTPStatus
from typing import Dict, List, Optional

import httpx
from typing_extensions import Any

from ... import errors
from ...models.fine_tuned_model_gym_admin import FineTunedModelGymAdmin

# from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    fine_tuning_request_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["fine_tuning_request_id"] = fine_tuning_request_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/gym/admin/finetunedmodels/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[List["FineTunedModelGymAdmin"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = FineTunedModelGymAdmin.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[List["FineTunedModelGymAdmin"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def projects_gym_admin_finetunedmodels_list_wrapper(client):
    def projects_gym_admin_finetunedmodels_list_wrapped(
        fine_tuning_request_id: str,
    ) -> List["FineTunedModelGymAdmin"]:
        """List all finetuned models, filtered by the finetuning_request id

        Args:
            fine_tuning_request_id (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List['FineTunedModelGymAdmin']]
        """

        kwargs = _get_kwargs(
            fine_tuning_request_id=fine_tuning_request_id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return projects_gym_admin_finetunedmodels_list_wrapped
