from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.v1_finetuning_create_json_body import V1FinetuningCreateJsonBody
from ...models.v1_finetuning_create_response_200 import V1FinetuningCreateResponse200
from ...models.v1_finetuning_create_response_400 import V1FinetuningCreateResponse400
from ...models.v1_finetuning_create_response_401 import V1FinetuningCreateResponse401
from ...models.v1_finetuning_create_response_403 import V1FinetuningCreateResponse403
from ...models.v1_finetuning_create_response_404_type_0 import V1FinetuningCreateResponse404Type0
from ...models.v1_finetuning_create_response_404_type_1 import V1FinetuningCreateResponse404Type1
from ...models.v1_finetuning_create_response_409 import V1FinetuningCreateResponse409
from ...models.v1_finetuning_create_response_422 import V1FinetuningCreateResponse422
from ...models.v1_finetuning_create_response_429 import V1FinetuningCreateResponse429
from ...models.v1_finetuning_create_response_500_type_0 import V1FinetuningCreateResponse500Type0
from ...models.v1_finetuning_create_response_500_type_1 import V1FinetuningCreateResponse500Type1
from ...models.v1_finetuning_create_response_500_type_2 import V1FinetuningCreateResponse500Type2
from ...models.v1_finetuning_create_response_500_type_3 import V1FinetuningCreateResponse500Type3
from ...models.v1_finetuning_create_response_500_type_4 import V1FinetuningCreateResponse500Type4
from ...models.v1_finetuning_create_response_500_type_5 import V1FinetuningCreateResponse500Type5

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[V1FinetuningCreateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/finetuning",
    }

    _json_body = body

    _kwargs["json"] = _json_body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[
    Union[
        Union["V1FinetuningCreateResponse404Type0", "V1FinetuningCreateResponse404Type1"],
        Union[
            "V1FinetuningCreateResponse500Type0",
            "V1FinetuningCreateResponse500Type1",
            "V1FinetuningCreateResponse500Type2",
            "V1FinetuningCreateResponse500Type3",
            "V1FinetuningCreateResponse500Type4",
            "V1FinetuningCreateResponse500Type5",
        ],
        V1FinetuningCreateResponse200,
        V1FinetuningCreateResponse400,
        V1FinetuningCreateResponse401,
        V1FinetuningCreateResponse403,
        V1FinetuningCreateResponse409,
        V1FinetuningCreateResponse422,
        V1FinetuningCreateResponse429,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = V1FinetuningCreateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[
    Union[
        Union["V1FinetuningCreateResponse404Type0", "V1FinetuningCreateResponse404Type1"],
        Union[
            "V1FinetuningCreateResponse500Type0",
            "V1FinetuningCreateResponse500Type1",
            "V1FinetuningCreateResponse500Type2",
            "V1FinetuningCreateResponse500Type3",
            "V1FinetuningCreateResponse500Type4",
            "V1FinetuningCreateResponse500Type5",
        ],
        V1FinetuningCreateResponse200,
        V1FinetuningCreateResponse400,
        V1FinetuningCreateResponse401,
        V1FinetuningCreateResponse403,
        V1FinetuningCreateResponse409,
        V1FinetuningCreateResponse422,
        V1FinetuningCreateResponse429,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_finetuning_create_wrapper(client):
    def v1_finetuning_create_wrapped(
        **body: Unpack[V1FinetuningCreateJsonBody],
    ) -> Union[
        Union["V1FinetuningCreateResponse404Type0", "V1FinetuningCreateResponse404Type1"],
        Union[
            "V1FinetuningCreateResponse500Type0",
            "V1FinetuningCreateResponse500Type1",
            "V1FinetuningCreateResponse500Type2",
            "V1FinetuningCreateResponse500Type3",
            "V1FinetuningCreateResponse500Type4",
            "V1FinetuningCreateResponse500Type5",
        ],
        V1FinetuningCreateResponse200,
        V1FinetuningCreateResponse400,
        V1FinetuningCreateResponse401,
        V1FinetuningCreateResponse403,
        V1FinetuningCreateResponse409,
        V1FinetuningCreateResponse422,
        V1FinetuningCreateResponse429,
    ]:
        """Creates a finetuning job.

        Args:
            authorization (str):
            body (V1FinetuningCreateJsonBody):
            body (V1FinetuningCreateDataBody):
            body (V1FinetuningCreateFilesBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Union['V1FinetuningCreateResponse404Type0', 'V1FinetuningCreateResponse404Type1'], Union['V1FinetuningCreateResponse500Type0', 'V1FinetuningCreateResponse500Type1', 'V1FinetuningCreateResponse500Type2', 'V1FinetuningCreateResponse500Type3', 'V1FinetuningCreateResponse500Type4', 'V1FinetuningCreateResponse500Type5'], V1FinetuningCreateResponse200, V1FinetuningCreateResponse400, V1FinetuningCreateResponse401, V1FinetuningCreateResponse403, V1FinetuningCreateResponse409, V1FinetuningCreateResponse422, V1FinetuningCreateResponse429]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_finetuning_create_wrapped
