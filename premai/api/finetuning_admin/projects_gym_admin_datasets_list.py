from http import HTTPStatus
from typing import Dict, List, Optional

import httpx
from typing_extensions import Any

from ... import errors
from ...models.data_set_gym_admin import DataSetGymAdmin

# from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    project_id: str,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["project_id"] = project_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/projects/gym/admin/datasets/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[List["DataSetGymAdmin"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DataSetGymAdmin.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[List["DataSetGymAdmin"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def projects_gym_admin_datasets_list_wrapper(client):
    def projects_gym_admin_datasets_list_wrapped(
        project_id: str,
    ) -> List["DataSetGymAdmin"]:
        """List all finetuned models, filtered by the project id

        Args:
            project_id (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List['DataSetGymAdmin']]
        """

        kwargs = _get_kwargs(
            project_id=project_id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return projects_gym_admin_datasets_list_wrapped
