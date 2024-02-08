from http import HTTPStatus
from typing import Dict, Optional, Union

import httpx
from typing_extensions import Any

from ... import errors
from ...models.v1_finetuning_retrieve_response_200 import V1FinetuningRetrieveResponse200
from ...models.v1_finetuning_retrieve_response_400 import V1FinetuningRetrieveResponse400
from ...models.v1_finetuning_retrieve_response_401 import V1FinetuningRetrieveResponse401
from ...models.v1_finetuning_retrieve_response_403 import V1FinetuningRetrieveResponse403
from ...models.v1_finetuning_retrieve_response_404_type_0 import V1FinetuningRetrieveResponse404Type0
from ...models.v1_finetuning_retrieve_response_404_type_1 import V1FinetuningRetrieveResponse404Type1
from ...models.v1_finetuning_retrieve_response_409 import V1FinetuningRetrieveResponse409
from ...models.v1_finetuning_retrieve_response_422 import V1FinetuningRetrieveResponse422
from ...models.v1_finetuning_retrieve_response_429 import V1FinetuningRetrieveResponse429
from ...models.v1_finetuning_retrieve_response_500_type_0 import V1FinetuningRetrieveResponse500Type0
from ...models.v1_finetuning_retrieve_response_500_type_1 import V1FinetuningRetrieveResponse500Type1
from ...models.v1_finetuning_retrieve_response_500_type_2 import V1FinetuningRetrieveResponse500Type2
from ...models.v1_finetuning_retrieve_response_500_type_3 import V1FinetuningRetrieveResponse500Type3
from ...models.v1_finetuning_retrieve_response_500_type_4 import V1FinetuningRetrieveResponse500Type4
from ...models.v1_finetuning_retrieve_response_500_type_5 import V1FinetuningRetrieveResponse500Type5

# from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    job_id: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/finetuning/{job_id}",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client, response: httpx.Response
) -> Optional[
    Union[
        Union["V1FinetuningRetrieveResponse404Type0", "V1FinetuningRetrieveResponse404Type1"],
        Union[
            "V1FinetuningRetrieveResponse500Type0",
            "V1FinetuningRetrieveResponse500Type1",
            "V1FinetuningRetrieveResponse500Type2",
            "V1FinetuningRetrieveResponse500Type3",
            "V1FinetuningRetrieveResponse500Type4",
            "V1FinetuningRetrieveResponse500Type5",
        ],
        V1FinetuningRetrieveResponse200,
        V1FinetuningRetrieveResponse400,
        V1FinetuningRetrieveResponse401,
        V1FinetuningRetrieveResponse403,
        V1FinetuningRetrieveResponse409,
        V1FinetuningRetrieveResponse422,
        V1FinetuningRetrieveResponse429,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = V1FinetuningRetrieveResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = V1FinetuningRetrieveResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = V1FinetuningRetrieveResponse401.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = V1FinetuningRetrieveResponse403.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:

        def _parse_response_404(
            data: object,
        ) -> Union["V1FinetuningRetrieveResponse404Type0", "V1FinetuningRetrieveResponse404Type1"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_404_type_0 = V1FinetuningRetrieveResponse404Type0.from_dict(data)

                return response_404_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_404_type_1 = V1FinetuningRetrieveResponse404Type1.from_dict(data)

            return response_404_type_1

        response_404 = _parse_response_404(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = V1FinetuningRetrieveResponse409.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = V1FinetuningRetrieveResponse422.from_dict(response.json())

        return response_422
    if response.status_code == HTTPStatus.TOO_MANY_REQUESTS:
        response_429 = V1FinetuningRetrieveResponse429.from_dict(response.json())

        return response_429
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:

        def _parse_response_500(
            data: object,
        ) -> Union[
            "V1FinetuningRetrieveResponse500Type0",
            "V1FinetuningRetrieveResponse500Type1",
            "V1FinetuningRetrieveResponse500Type2",
            "V1FinetuningRetrieveResponse500Type3",
            "V1FinetuningRetrieveResponse500Type4",
            "V1FinetuningRetrieveResponse500Type5",
        ]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_0 = V1FinetuningRetrieveResponse500Type0.from_dict(data)

                return response_500_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_1 = V1FinetuningRetrieveResponse500Type1.from_dict(data)

                return response_500_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_2 = V1FinetuningRetrieveResponse500Type2.from_dict(data)

                return response_500_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_3 = V1FinetuningRetrieveResponse500Type3.from_dict(data)

                return response_500_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_500_type_4 = V1FinetuningRetrieveResponse500Type4.from_dict(data)

                return response_500_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_500_type_5 = V1FinetuningRetrieveResponse500Type5.from_dict(data)

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
        Union["V1FinetuningRetrieveResponse404Type0", "V1FinetuningRetrieveResponse404Type1"],
        Union[
            "V1FinetuningRetrieveResponse500Type0",
            "V1FinetuningRetrieveResponse500Type1",
            "V1FinetuningRetrieveResponse500Type2",
            "V1FinetuningRetrieveResponse500Type3",
            "V1FinetuningRetrieveResponse500Type4",
            "V1FinetuningRetrieveResponse500Type5",
        ],
        V1FinetuningRetrieveResponse200,
        V1FinetuningRetrieveResponse400,
        V1FinetuningRetrieveResponse401,
        V1FinetuningRetrieveResponse403,
        V1FinetuningRetrieveResponse409,
        V1FinetuningRetrieveResponse422,
        V1FinetuningRetrieveResponse429,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_finetuning_retrieve_wrapper(client):
    def v1_finetuning_retrieve_wrapped(
        job_id: str,
    ) -> Union[
        Union["V1FinetuningRetrieveResponse404Type0", "V1FinetuningRetrieveResponse404Type1"],
        Union[
            "V1FinetuningRetrieveResponse500Type0",
            "V1FinetuningRetrieveResponse500Type1",
            "V1FinetuningRetrieveResponse500Type2",
            "V1FinetuningRetrieveResponse500Type3",
            "V1FinetuningRetrieveResponse500Type4",
            "V1FinetuningRetrieveResponse500Type5",
        ],
        V1FinetuningRetrieveResponse200,
        V1FinetuningRetrieveResponse400,
        V1FinetuningRetrieveResponse401,
        V1FinetuningRetrieveResponse403,
        V1FinetuningRetrieveResponse409,
        V1FinetuningRetrieveResponse422,
        V1FinetuningRetrieveResponse429,
    ]:
        """Retrieve a finetuning job.

        Args:
            job_id (str):
            authorization (str):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[Union['V1FinetuningRetrieveResponse404Type0', 'V1FinetuningRetrieveResponse404Type1'], Union['V1FinetuningRetrieveResponse500Type0', 'V1FinetuningRetrieveResponse500Type1', 'V1FinetuningRetrieveResponse500Type2', 'V1FinetuningRetrieveResponse500Type3', 'V1FinetuningRetrieveResponse500Type4', 'V1FinetuningRetrieveResponse500Type5'], V1FinetuningRetrieveResponse200, V1FinetuningRetrieveResponse400, V1FinetuningRetrieveResponse401, V1FinetuningRetrieveResponse403, V1FinetuningRetrieveResponse409, V1FinetuningRetrieveResponse422, V1FinetuningRetrieveResponse429]]
        """

        kwargs = _get_kwargs(
            job_id=job_id,
        )

        httpx_client = client.get_httpx_client()

        response = httpx_client.request(
            **kwargs,
        )

        return _build_response(client=client, response=response).parsed

    return v1_finetuning_retrieve_wrapped
