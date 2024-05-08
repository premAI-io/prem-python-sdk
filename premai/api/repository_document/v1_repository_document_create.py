from http import HTTPStatus
from typing import Dict, Optional

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.document_input import DocumentInput
from ...models.document_output import DocumentOutput

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    repository_id: int,
    **body: Unpack[DocumentInput],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/repository/{repository_id}/document",
    }

    try:
        file_path = body.pop("file")
    except KeyError:
        raise ValueError("file is a required parameter")
    
    _kwargs["files"] = {"file": open(file_path, "rb")}

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client, response: httpx.Response) -> Optional[DocumentOutput]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DocumentOutput.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client, response: httpx.Response) -> Response[DocumentOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_repository_document_create_wrapper(client):
    def v1_repository_document_create_wrapped(
        repository_id: int,
        **body: Unpack[DocumentInput],
    ) -> DocumentOutput:
        """
        Args:
            repository_id (int):
            body (DocumentInput):
            body (DocumentInput):
            body (DocumentInput):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[DocumentOutput]
        """
        kwargs = _get_kwargs(
            repository_id=repository_id,
            **body,
        )
        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_repository_document_create_wrapped
