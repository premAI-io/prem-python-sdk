from http import HTTPStatus
from typing import Dict, List, Optional, Union

import httpx
from typing_extensions import Any

from ... import errors
from ...models.trace_list import TraceList
from ...models.v1_traces_list_admin_filter import V1TracesListAdminFilter
from ...models.v1_traces_list_date_filter import V1TracesListDateFilter

# from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: int,
    admin_filter: Union[Unset, V1TracesListAdminFilter] = UNSET,
    date_filter: Union[Unset, V1TracesListDateFilter] = UNSET,
    from_date: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    sort: Union[Unset, str] = UNSET,
    to_date: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_admin_filter: Union[Unset, str] = UNSET
    if not isinstance(admin_filter, Unset):
        json_admin_filter = admin_filter.value

    params["admin_filter"] = json_admin_filter

    json_date_filter: Union[Unset, str] = UNSET
    if not isinstance(date_filter, Unset):
        json_date_filter = date_filter.value

    params["date_filter"] = json_date_filter

    params["from_date"] = from_date

    params["project_id"] = project_id

    params["search"] = search

    params["sort"] = sort

    params["to_date"] = to_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/traces/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[List["TraceList"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TraceList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[List["TraceList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_traces_list_wrapper(client):
    def v1_traces_list_wrapped(
        project_id: int,
        admin_filter: Union[Unset, V1TracesListAdminFilter] = UNSET,
        date_filter: Union[Unset, V1TracesListDateFilter] = UNSET,
        from_date: Union[Unset, str] = UNSET,
        search: Union[Unset, str] = UNSET,
        sort: Union[Unset, str] = UNSET,
        to_date: Union[Unset, str] = UNSET,
    ) -> List["TraceList"]:
        """
        Args:
            admin_filter (Union[Unset, V1TracesListAdminFilter]):
            date_filter (Union[Unset, V1TracesListDateFilter]):
            from_date (Union[Unset, str]):
            project_id (int):
            search (Union[Unset, str]):
            sort (Union[Unset, str]):
            to_date (Union[Unset, str]):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[List['TraceList']]
        """

        kwargs = _get_kwargs(
            admin_filter=admin_filter,
            date_filter=date_filter,
            from_date=from_date,
            project_id=project_id,
            search=search,
            sort=sort,
            to_date=to_date,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_traces_list_wrapped
