from http import HTTPStatus
from typing import Dict, Optional, Union, TypeVar, List, Type
from attrs import define as _attrs_define
from attrs import field as _attrs_field

import httpx
import json
from typing_extensions import Any, Unpack

from ... import errors
from ...models.api_response_validation_error import APIResponseValidationError
from ...models.authentication_error import AuthenticationError
from ...models.catch_all_error import CatchAllError
from ...models.chat_completion_input import ChatCompletionInput
from ...models.chat_completion_response import ChatCompletionResponse
from ...models.document_chunks import DocumentChunks
from ...models.conflict_error import ConflictError
from ...models.model_not_found_error import ModelNotFoundError
from ...models.permission_denied_error import PermissionDeniedError
from ...models.provider_api_connection_error import ProviderAPIConnectionError
from ...models.provider_api_status_error import ProviderAPIStatusError
from ...models.provider_api_timeout_error import ProviderAPITimeoutError
from ...models.provider_internal_server_error import ProviderInternalServerError
from ...models.provider_not_found_error import ProviderNotFoundError
from ...models.rate_limit_error import RateLimitError
from ...models.unprocessable_entity_error import UnprocessableEntityError
from ...models.validation_error import ValidationError
from ...models.usage import Usage
from ...models.response_choice import ResponseChoice
from ...types import Response, UNSET, Unset


# from ...client import AuthenticatedClient, Client
from ...types import Response
T = TypeVar("T", bound="ResponseChoice")

def _get_kwargs(
    **body: Unpack[ChatCompletionInput],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/chat/completions",
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
        AuthenticationError,
        ChatCompletionResponse,
        ConflictError,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ChatCompletionResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client, response: httpx.Response
) -> Response[
    Union[
        AuthenticationError,
        ChatCompletionResponse,
        ConflictError,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def v1_chat_completions_create_wrapper(client):
    def v1_chat_completions_create_wrapped(
        **body: Unpack[ChatCompletionInput],
    ) -> Union[
        AuthenticationError,
        ChatCompletionResponse,
        ConflictError,
        PermissionDeniedError,
        RateLimitError,
        Union[
            "APIResponseValidationError",
            "CatchAllError",
            "ProviderAPIConnectionError",
            "ProviderAPIStatusError",
            "ProviderAPITimeoutError",
            "ProviderInternalServerError",
        ],
        Union["ModelNotFoundError", "ProviderNotFoundError"],
        UnprocessableEntityError,
        ValidationError,
    ]:
        """Creates a model response for the given chat conversation.

        Args:
            authorization (str):
            body (ChatCompletionInput):
            body (ChatCompletionInput):
            body (ChatCompletionInput):

        Raises:
            errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
            httpx.TimeoutException: If the request takes longer than Client.timeout.

        Returns:
            Response[Union[AuthenticationError, ChatCompletionResponse, ConflictError, PermissionDeniedError, RateLimitError, Union['APIResponseValidationError', 'CatchAllError', 'ProviderAPIConnectionError', 'ProviderAPIStatusError', 'ProviderAPITimeoutError', 'ProviderInternalServerError'], Union['ModelNotFoundError', 'ProviderNotFoundError'], UnprocessableEntityError, ValidationError]]
        """

        kwargs = _get_kwargs(
            **body,
        )

        httpx_client = client.get_httpx_client()
        if ('stream' in body) and (body['stream']):
            stream = httpx_client.stream(**kwargs)
            return ChatCompletionResponseStreamContainer(stream)
        else:
            response = httpx_client.request(
                **kwargs,
            )
            return _build_response(client=client, response=response).parsed
    return v1_chat_completions_create_wrapped


END_STREAM = 'done'
import re
class ChatCompletionResponseStreamContainer:
    _pattern = '(?<={key}: )(.*)'
    trace_id: str = None
    document_chunks: DocumentChunks = None

    def __init__(self, stream: httpx.Response):  
        self._stream = stream

    def _parse_data(self, text: str):
        try:
            match = re.search(self._pattern.format(key='data'), text)
            if match:
                data = json.loads(match.group(1))
                parsed_data: ChatCompletionResponseStream = ChatCompletionResponseStream.from_dict(data)
                return parsed_data
            else:   return None
        except Exception as e:
            return None

    def _parse_event(self, text: str):
        match = re.search(self._pattern.format(key='event'), text)
        if match: return match.group(1)
        else:   return None

    def _parse_trace_id(self, text: str):
        match = re.search(self._pattern.format(key='trace_id'), text)
        if match: return match.group(1)
        else:   return None

    def _parse_document_chunks(self, text: str):
        match = re.search(self._pattern.format(key='document_chunks'), text)
        if match:
            data = json.loads(match.group(1))
            parsed_data: DocumentChunks = [DocumentChunks.from_dict(parsed_chunk) for parsed_chunk in data]
            return parsed_data
        else:   return None
    

    def __iter__(self):
        def generator():
            with self._stream as stream:
                for texts in stream.iter_text():
                    
                    for text in texts.split('\n'):
                        trace_id = self._parse_trace_id(text)
                        self.trace_id = self.trace_id or trace_id
                        
                        self.document_chunks = self.document_chunks or self._parse_document_chunks(text)

                        data = self._parse_data(text)

                        if data:
                            yield data  
        return generator()
    

@_attrs_define
class ChatCompletionResponseStream:
    """
    Attributes:
        id (str): A unique identifier for the chat completion. Each chunk has the same ID.
        choices (List['ChatCompletionResponseChoicesItem']): A list of chat completion choices. Can be more
            than one if n is greater than 1.
        created (int): The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same
            timestamp.
        model (str): The model to generate the completion.
        provider_name (str): The name of the provider that generated the completion.
        provider_id (str): The ID of the provider that generated the completion.
        usage (Union[Unset, ChatCompletionResponseUsage]): The usage statistics for the completion.
    """
    id: str
    choices: List["ResponseChoiceStream"]
    created: int
    model: str
    usage: Union[Unset, "Usage"] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        created = self.created

        model = self.model

        usage: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "choices": choices,
                "created": created,
                "model": model,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:

        d = src_dict.copy()
        id = d.pop("id")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = ResponseChoiceStream.from_dict(choices_item_data)

            choices.append(choices_item)

        created = d.pop("created")
        model = d.pop("model")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, Usage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = Usage.from_dict(_usage)

        v1_chat_completions_create_response_200 = cls(
            id=id,
            choices=choices,
            created=created,
            model=model,
            usage=usage,
        )

        v1_chat_completions_create_response_200.additional_properties = d
        return v1_chat_completions_create_response_200

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@_attrs_define
class ResponseChoiceStream:
    """
    Attributes:
        message (str): The generated message in the chat completion choice.
        finish_reason (str): The reason the chat completion finished, e.g., 'stop' or 'length'.
    """

    delta: str
    finish_reason: str

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delta = self.delta

        finish_reason = self.finish_reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delta": delta,
                "finish_reason": finish_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delta = d.pop("delta")

        finish_reason = d.pop("finish_reason")

        v1_chat_completions_create_response_200_choices_item = cls(
            delta=delta,
            finish_reason=finish_reason,
        )

        v1_chat_completions_create_response_200_choices_item.additional_properties = d
        return v1_chat_completions_create_response_200_choices_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties