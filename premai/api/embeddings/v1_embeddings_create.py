from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any, Unpack

from ... import errors
from ...models.v1_embeddings_create_json_body import V1EmbeddingsCreateJsonBody
from ...models.v1_embeddings_create_response_200 import V1EmbeddingsCreateResponse200
from ...models.v1_embeddings_create_response_400 import V1EmbeddingsCreateResponse400
from ...models.v1_embeddings_create_response_401 import V1EmbeddingsCreateResponse401
from ...models.v1_embeddings_create_response_403 import V1EmbeddingsCreateResponse403
from ...models.v1_embeddings_create_response_404_type_0 import V1EmbeddingsCreateResponse404Type0
from ...models.v1_embeddings_create_response_404_type_1 import V1EmbeddingsCreateResponse404Type1
from ...models.v1_embeddings_create_response_409 import V1EmbeddingsCreateResponse409
from ...models.v1_embeddings_create_response_422 import V1EmbeddingsCreateResponse422
from ...models.v1_embeddings_create_response_429 import V1EmbeddingsCreateResponse429
from ...models.v1_embeddings_create_response_500_type_0 import V1EmbeddingsCreateResponse500Type0
from ...models.v1_embeddings_create_response_500_type_1 import V1EmbeddingsCreateResponse500Type1
from ...models.v1_embeddings_create_response_500_type_2 import V1EmbeddingsCreateResponse500Type2
from ...models.v1_embeddings_create_response_500_type_3 import V1EmbeddingsCreateResponse500Type3
from ...models.v1_embeddings_create_response_500_type_4 import V1EmbeddingsCreateResponse500Type4
from ...models.v1_embeddings_create_response_500_type_5 import V1EmbeddingsCreateResponse500Type5

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    **body: Unpack[V1EmbeddingsCreateJsonBody],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/embeddings",
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
        Union["V1EmbeddingsCreateResponse404Type0", "V1EmbeddingsCreateResponse404Type1"],
        Union[
            "V1EmbeddingsCreateResponse500Type0",
            "V1EmbeddingsCreateResponse500Type1",
            "V1EmbeddingsCreateResponse500Type2",
            "V1EmbeddingsCreateResponse500Type3",
            "V1EmbeddingsCreateResponse500Type4",
            "V1EmbeddingsCreateResponse500Type5",
        ],
        V1EmbeddingsCreateResponse200,
        V1EmbeddingsCreateResponse400,
        V1EmbeddingsCreateResponse401,
        V1EmbeddingsCreateResponse403,
        V1EmbeddingsCreateResponse409,
        V1EmbeddingsCreateResponse422,
        V1EmbeddingsCreateResponse429,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = V1EmbeddingsCreateResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = V1EmbeddingsCreateResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = V1EmbeddingsCreateResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = V1EmbeddingsCreateResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:

        def _parse_response_404(
            data: object,
        ) -> Union["V1EmbeddingsCreateResponse404Type0", "V1EmbeddingsCreateResponse404Type1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = V1EmbeddingsCreateResponse404Type0.from_dict(data)

                return response_404_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = V1EmbeddingsCreateResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = V1EmbeddingsCreateResponse409.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = V1EmbeddingsCreateResponse422.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = V1EmbeddingsCreateResponse429.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:

        def _parse_response_500(
            data: object,
        ) -> Union[
            "V1EmbeddingsCreateResponse500Type0",
            "V1EmbeddingsCreateResponse500Type1",
            "V1EmbeddingsCreateResponse500Type2",
            "V1EmbeddingsCreateResponse500Type3",
            "V1EmbeddingsCreateResponse500Type4",
            "V1EmbeddingsCreateResponse500Type5",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_0 = V1EmbeddingsCreateResponse500Type0.from_dict(data)

                return response_500_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_1 = V1EmbeddingsCreateResponse500Type1.from_dict(data)

                return response_500_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_2 = V1EmbeddingsCreateResponse500Type2.from_dict(data)

                return response_500_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_3 = V1EmbeddingsCreateResponse500Type3.from_dict(data)

                return response_500_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_4 = V1EmbeddingsCreateResponse500Type4.from_dict(data)

                return response_500_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_500_type_5 = V1EmbeddingsCreateResponse500Type5.from_dict(data)

            return response_500_type_5

        response_500 = _parse_response_500(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[
    Union[
        Union["V1EmbeddingsCreateResponse404Type0", "V1EmbeddingsCreateResponse404Type1"],
        Union[
            "V1EmbeddingsCreateResponse500Type0",
            "V1EmbeddingsCreateResponse500Type1",
            "V1EmbeddingsCreateResponse500Type2",
            "V1EmbeddingsCreateResponse500Type3",
            "V1EmbeddingsCreateResponse500Type4",
            "V1EmbeddingsCreateResponse500Type5",
        ],
        V1EmbeddingsCreateResponse200,
        V1EmbeddingsCreateResponse400,
        V1EmbeddingsCreateResponse401,
        V1EmbeddingsCreateResponse403,
        V1EmbeddingsCreateResponse409,
        V1EmbeddingsCreateResponse422,
        V1EmbeddingsCreateResponse429,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_embeddings_create_wrapper(client):
    def v1_embeddings_create_wrapped(
        **body: Unpack[V1EmbeddingsCreateJsonBody],
    ) -> Union[
        Union["V1EmbeddingsCreateResponse404Type0", "V1EmbeddingsCreateResponse404Type1"],
        Union[
            "V1EmbeddingsCreateResponse500Type0",
            "V1EmbeddingsCreateResponse500Type1",
            "V1EmbeddingsCreateResponse500Type2",
            "V1EmbeddingsCreateResponse500Type3",
            "V1EmbeddingsCreateResponse500Type4",
            "V1EmbeddingsCreateResponse500Type5",
        ],
        V1EmbeddingsCreateResponse200,
        V1EmbeddingsCreateResponse400,
        V1EmbeddingsCreateResponse401,
        V1EmbeddingsCreateResponse403,
        V1EmbeddingsCreateResponse409,
        V1EmbeddingsCreateResponse422,
        V1EmbeddingsCreateResponse429,
    ]:
        """Creates embeddings for the given input.

        Args:
            authorization (str):
            body (V1EmbeddingsCreateJsonBody):
            body (V1EmbeddingsCreateDataBody):
            body (V1EmbeddingsCreateFilesBody):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Union['V1EmbeddingsCreateResponse404Type0', 'V1EmbeddingsCreateResponse404Type1'], Union['V1EmbeddingsCreateResponse500Type0', 'V1EmbeddingsCreateResponse500Type1', 'V1EmbeddingsCreateResponse500Type2', 'V1EmbeddingsCreateResponse500Type3', 'V1EmbeddingsCreateResponse500Type4', 'V1EmbeddingsCreateResponse500Type5'], V1EmbeddingsCreateResponse200, V1EmbeddingsCreateResponse400, V1EmbeddingsCreateResponse401, V1EmbeddingsCreateResponse403, V1EmbeddingsCreateResponse409, V1EmbeddingsCreateResponse422, V1EmbeddingsCreateResponse429]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_embeddings_create_wrapped