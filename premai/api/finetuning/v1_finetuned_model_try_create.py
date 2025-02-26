from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.fine_tuned_model_try_request import FineTunedModelTryRequest
from ...models.fine_tuned_model_try_response import FineTunedModelTryResponse
from ...models.v1_finetuned_model_try_create_response_404 import V1FinetunedModelTryCreateResponse404

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[FineTunedModelTryRequest],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/finetuned_model_try",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[Union[FineTunedModelTryResponse, V1FinetunedModelTryCreateResponse404]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FineTunedModelTryResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[Union[FineTunedModelTryResponse, V1FinetunedModelTryCreateResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_finetuned_model_try_create_wrapper(client):
    def v1_finetuned_model_try_create_wrapped(
        **body: Unpack[FineTunedModelTryRequest],
    ) -> Union[FineTunedModelTryResponse, V1FinetunedModelTryCreateResponse404]:
        """Try out a finetuned model by creating a new playground

        Args:
            body (FineTunedModelTryRequest):
            body (FineTunedModelTryRequest):
            body (FineTunedModelTryRequest):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[FineTunedModelTryResponse, V1FinetunedModelTryCreateResponse404]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_finetuned_model_try_create_wrapped
