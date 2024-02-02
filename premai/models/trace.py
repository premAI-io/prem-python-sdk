import datetime
from typing import Dict, List, Type, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse
from typing_extensions import Any, NotRequired, TypedDict, TypeVar

from ..models.trace_raw_request_type_0 import TraceRawRequestType0
from ..models.trace_raw_response_type_0 import TraceRawResponseType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="Trace")


class TraceDict(TypedDict):
    id: str
    model_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    start_time: datetime.datetime
    end_time: datetime.datetime
    input_prompt_tokens_number: int
    output_text_tokens_number: int
    is_deleted: NotRequired[Union[Unset, bool]]
    input_prompt: NotRequired[Union[Unset, str]]
    input_file_prompt: NotRequired[Union[None, Unset, str]]
    endpoint_type: NotRequired[Union[None, Unset, str]]
    privacy_score: NotRequired[Union[None, Unset, str]]
    output_text: NotRequired[Union[Unset, str]]
    http_status_code: NotRequired[Union[None, Unset, int]]
    raw_request: NotRequired[Union["TraceRawRequestType0", None, Unset]]
    raw_response: NotRequired[Union["TraceRawResponseType0", None, Unset]]
    tag: NotRequired[Union[None, Unset, str]]
    error: NotRequired[Union[None, Unset, str]]
    text_to_text_model_parameters: NotRequired[Union[None, Unset, int]]
    api_key: NotRequired[Union[None, Unset, int]]
    pass


@_attrs_define
class Trace:
    """
    Attributes:
        id (str):
        model_name (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        start_time (datetime.datetime):
        end_time (datetime.datetime):
        input_prompt_tokens_number (int):
        output_text_tokens_number (int):
        is_deleted (Union[Unset, bool]):
        input_prompt (Union[Unset, str]):
        input_file_prompt (Union[None, Unset, str]):
        endpoint_type (Union[None, Unset, str]):
        privacy_score (Union[None, Unset, str]):
        output_text (Union[Unset, str]):
        http_status_code (Union[None, Unset, int]):
        raw_request (Union['TraceRawRequestType0', None, Unset]):
        raw_response (Union['TraceRawResponseType0', None, Unset]):
        tag (Union[None, Unset, str]):
        error (Union[None, Unset, str]):
        text_to_text_model_parameters (Union[None, Unset, int]):
        api_key (Union[None, Unset, int]):
    """

    id: str
    model_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    start_time: datetime.datetime
    end_time: datetime.datetime
    input_prompt_tokens_number: int
    output_text_tokens_number: int
    is_deleted: Union[Unset, bool] = UNSET
    input_prompt: Union[Unset, str] = UNSET
    input_file_prompt: Union[None, Unset, str] = UNSET
    endpoint_type: Union[None, Unset, str] = UNSET
    privacy_score: Union[None, Unset, str] = UNSET
    output_text: Union[Unset, str] = UNSET
    http_status_code: Union[None, Unset, int] = UNSET
    raw_request: Union["TraceRawRequestType0", None, Unset] = UNSET
    raw_response: Union["TraceRawResponseType0", None, Unset] = UNSET
    tag: Union[None, Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
    text_to_text_model_parameters: Union[None, Unset, int] = UNSET
    api_key: Union[None, Unset, int] = UNSET

    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.trace_raw_request_type_0 import TraceRawRequestType0
        from ..models.trace_raw_response_type_0 import TraceRawResponseType0

        id = self.id

        model_name = self.model_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        start_time = self.start_time.isoformat()

        end_time = self.end_time.isoformat()

        input_prompt_tokens_number = self.input_prompt_tokens_number

        output_text_tokens_number = self.output_text_tokens_number

        is_deleted = self.is_deleted

        input_prompt = self.input_prompt

        input_file_prompt: Union[None, Unset, str]
        if isinstance(self.input_file_prompt, Unset):
            input_file_prompt = UNSET
        else:
            input_file_prompt = self.input_file_prompt

        endpoint_type: Union[None, Unset, str]
        if isinstance(self.endpoint_type, Unset):
            endpoint_type = UNSET
        else:
            endpoint_type = self.endpoint_type

        privacy_score: Union[None, Unset, str]
        if isinstance(self.privacy_score, Unset):
            privacy_score = UNSET
        else:
            privacy_score = self.privacy_score

        output_text = self.output_text

        http_status_code: Union[None, Unset, int]
        if isinstance(self.http_status_code, Unset):
            http_status_code = UNSET
        else:
            http_status_code = self.http_status_code

        raw_request: Union[Dict[str, Any], None, Unset]
        if isinstance(self.raw_request, Unset):
            raw_request = UNSET
        elif isinstance(self.raw_request, TraceRawRequestType0):
            raw_request = self.raw_request.to_dict()
        else:
            raw_request = self.raw_request

        raw_response: Union[Dict[str, Any], None, Unset]
        if isinstance(self.raw_response, Unset):
            raw_response = UNSET
        elif isinstance(self.raw_response, TraceRawResponseType0):
            raw_response = self.raw_response.to_dict()
        else:
            raw_response = self.raw_response

        tag: Union[None, Unset, str]
        if isinstance(self.tag, Unset):
            tag = UNSET
        else:
            tag = self.tag

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        text_to_text_model_parameters: Union[None, Unset, int]
        if isinstance(self.text_to_text_model_parameters, Unset):
            text_to_text_model_parameters = UNSET
        else:
            text_to_text_model_parameters = self.text_to_text_model_parameters

        api_key: Union[None, Unset, int]
        if isinstance(self.api_key, Unset):
            api_key = UNSET
        else:
            api_key = self.api_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "model_name": model_name,
                "created_at": created_at,
                "updated_at": updated_at,
                "start_time": start_time,
                "end_time": end_time,
                "input_prompt_tokens_number": input_prompt_tokens_number,
                "output_text_tokens_number": output_text_tokens_number,
            }
        )
        if is_deleted is not UNSET:
            field_dict["is_deleted"] = is_deleted
        if input_prompt is not UNSET:
            field_dict["input_prompt"] = input_prompt
        if input_file_prompt is not UNSET:
            field_dict["input_file_prompt"] = input_file_prompt
        if endpoint_type is not UNSET:
            field_dict["endpoint_type"] = endpoint_type
        if privacy_score is not UNSET:
            field_dict["privacy_score"] = privacy_score
        if output_text is not UNSET:
            field_dict["output_text"] = output_text
        if http_status_code is not UNSET:
            field_dict["http_status_code"] = http_status_code
        if raw_request is not UNSET:
            field_dict["raw_request"] = raw_request
        if raw_response is not UNSET:
            field_dict["raw_response"] = raw_response
        if tag is not UNSET:
            field_dict["tag"] = tag
        if error is not UNSET:
            field_dict["error"] = error
        if text_to_text_model_parameters is not UNSET:
            field_dict["text_to_text_model_parameters"] = text_to_text_model_parameters
        if api_key is not UNSET:
            field_dict["api_key"] = api_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trace_raw_request_type_0 import TraceRawRequestType0
        from ..models.trace_raw_response_type_0 import TraceRawResponseType0

        d = src_dict.copy()
        id = d.pop("id")

        model_name = d.pop("model_name")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        start_time = isoparse(d.pop("start_time"))

        end_time = isoparse(d.pop("end_time"))

        input_prompt_tokens_number = d.pop("input_prompt_tokens_number")

        output_text_tokens_number = d.pop("output_text_tokens_number")

        is_deleted = d.pop("is_deleted", UNSET)

        input_prompt = d.pop("input_prompt", UNSET)

        def _parse_input_file_prompt(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        input_file_prompt = _parse_input_file_prompt(d.pop("input_file_prompt", UNSET))

        def _parse_endpoint_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        endpoint_type = _parse_endpoint_type(d.pop("endpoint_type", UNSET))

        def _parse_privacy_score(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        privacy_score = _parse_privacy_score(d.pop("privacy_score", UNSET))

        output_text = d.pop("output_text", UNSET)

        def _parse_http_status_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        http_status_code = _parse_http_status_code(d.pop("http_status_code", UNSET))

        def _parse_raw_request(data: object) -> Union["TraceRawRequestType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_request_type_0 = TraceRawRequestType0.from_dict(data)

                return raw_request_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TraceRawRequestType0", None, Unset], data)

        raw_request = _parse_raw_request(d.pop("raw_request", UNSET))

        def _parse_raw_response(data: object) -> Union["TraceRawResponseType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_response_type_0 = TraceRawResponseType0.from_dict(data)

                return raw_response_type_0
            except:  # noqa: E722
                pass
            return cast(Union["TraceRawResponseType0", None, Unset], data)

        raw_response = _parse_raw_response(d.pop("raw_response", UNSET))

        def _parse_tag(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag = _parse_tag(d.pop("tag", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_text_to_text_model_parameters(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        text_to_text_model_parameters = _parse_text_to_text_model_parameters(
            d.pop("text_to_text_model_parameters", UNSET)
        )

        def _parse_api_key(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        api_key = _parse_api_key(d.pop("api_key", UNSET))

        trace = cls(
            id=id,
            model_name=model_name,
            created_at=created_at,
            updated_at=updated_at,
            start_time=start_time,
            end_time=end_time,
            input_prompt_tokens_number=input_prompt_tokens_number,
            output_text_tokens_number=output_text_tokens_number,
            is_deleted=is_deleted,
            input_prompt=input_prompt,
            input_file_prompt=input_file_prompt,
            endpoint_type=endpoint_type,
            privacy_score=privacy_score,
            output_text=output_text,
            http_status_code=http_status_code,
            raw_request=raw_request,
            raw_response=raw_response,
            tag=tag,
            error=error,
            text_to_text_model_parameters=text_to_text_model_parameters,
            api_key=api_key,
        )

        trace.additional_properties = d
        return trace

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
