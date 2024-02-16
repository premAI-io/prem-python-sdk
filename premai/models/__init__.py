""" Contains all the data models used in inputs/outputs """

from .api_response_validation_error import APIResponseValidationError
from .api_response_validation_error_code import APIResponseValidationErrorCode
from .api_response_validation_error_code_enum import APIResponseValidationErrorCodeEnum
from .authentication_error import AuthenticationError
from .authentication_error_code import AuthenticationErrorCode
from .authentication_error_code_enum import AuthenticationErrorCodeEnum
from .catch_all_error import CatchAllError
from .catch_all_error_code import CatchAllErrorCode
from .catch_all_error_code_enum import CatchAllErrorCodeEnum
from .chat_completion_input import ChatCompletionInput
from .chat_completion_input_logit_bias_type_0 import ChatCompletionInputLogitBiasType0
from .chat_completion_input_messages_item import ChatCompletionInputMessagesItem
from .chat_completion_input_messages_item_role import ChatCompletionInputMessagesItemRole
from .chat_completion_input_response_format_type_0 import ChatCompletionInputResponseFormatType0
from .chat_completion_input_tools_item import ChatCompletionInputToolsItem
from .chat_completion_response import ChatCompletionResponse
from .chat_completion_response_choices_item import ChatCompletionResponseChoicesItem
from .chat_completion_response_usage import ChatCompletionResponseUsage
from .conflict_error import ConflictError
from .conflict_error_code import ConflictErrorCode
from .conflict_error_code_enum import ConflictErrorCodeEnum
from .data_point import DataPoint
from .embedding import Embedding
from .embeddings_input import EmbeddingsInput
from .embeddings_input_encoding_format import EmbeddingsInputEncodingFormat
from .embeddings_response import EmbeddingsResponse
from .embeddings_response_data_item import EmbeddingsResponseDataItem
from .embeddings_response_usage import EmbeddingsResponseUsage
from .encoding_format_enum import EncodingFormatEnum
from .fine_tuning_input import FineTuningInput
from .fine_tuning_input_training_data_item import FineTuningInputTrainingDataItem
from .fine_tuning_input_validaton_data_item import FineTuningInputValidatonDataItem
from .fine_tuning_response import FineTuningResponse
from .fine_tuning_sample import FineTuningSample
from .input_data_point import InputDataPoint
from .internal_server_error_type_0 import InternalServerErrorType0
from .internal_server_error_type_0_code import InternalServerErrorType0Code
from .internal_server_error_type_1 import InternalServerErrorType1
from .internal_server_error_type_1_code import InternalServerErrorType1Code
from .internal_server_error_type_2 import InternalServerErrorType2
from .internal_server_error_type_2_code import InternalServerErrorType2Code
from .internal_server_error_type_3 import InternalServerErrorType3
from .internal_server_error_type_3_code import InternalServerErrorType3Code
from .internal_server_error_type_4 import InternalServerErrorType4
from .internal_server_error_type_4_code import InternalServerErrorType4Code
from .internal_server_error_type_5 import InternalServerErrorType5
from .internal_server_error_type_5_code import InternalServerErrorType5Code
from .message import Message
from .message_role import MessageRole
from .model_not_found_error import ModelNotFoundError
from .model_not_found_error_code import ModelNotFoundErrorCode
from .model_not_found_error_code_enum import ModelNotFoundErrorCodeEnum
from .not_found_error_type_0 import NotFoundErrorType0
from .not_found_error_type_0_code import NotFoundErrorType0Code
from .not_found_error_type_1 import NotFoundErrorType1
from .not_found_error_type_1_code import NotFoundErrorType1Code
from .patched_data_point import PatchedDataPoint
from .permission_denied_error import PermissionDeniedError
from .permission_denied_error_code import PermissionDeniedErrorCode
from .permission_denied_error_code_enum import PermissionDeniedErrorCodeEnum
from .provider_api_connection_error import ProviderAPIConnectionError
from .provider_api_connection_error_code import ProviderAPIConnectionErrorCode
from .provider_api_connection_error_code_enum import ProviderAPIConnectionErrorCodeEnum
from .provider_api_status_error import ProviderAPIStatusError
from .provider_api_status_error_code import ProviderAPIStatusErrorCode
from .provider_api_status_error_code_enum import ProviderAPIStatusErrorCodeEnum
from .provider_api_timeout_error import ProviderAPITimeoutError
from .provider_api_timeout_error_code import ProviderAPITimeoutErrorCode
from .provider_api_timeout_error_code_enum import ProviderAPITimeoutErrorCodeEnum
from .provider_internal_server_error import ProviderInternalServerError
from .provider_internal_server_error_code import ProviderInternalServerErrorCode
from .provider_internal_server_error_code_enum import ProviderInternalServerErrorCodeEnum
from .provider_not_found_error import ProviderNotFoundError
from .provider_not_found_error_code import ProviderNotFoundErrorCode
from .provider_not_found_error_code_enum import ProviderNotFoundErrorCodeEnum
from .rate_limit_error import RateLimitError
from .rate_limit_error_code import RateLimitErrorCode
from .rate_limit_error_code_enum import RateLimitErrorCodeEnum
from .response_choice import ResponseChoice
from .retrieve_fine_tuning_response import RetrieveFineTuningResponse
from .role_enum import RoleEnum
from .unprocessable_entity_error import UnprocessableEntityError
from .unprocessable_entity_error_code import UnprocessableEntityErrorCode
from .unprocessable_entity_error_code_enum import UnprocessableEntityErrorCodeEnum
from .usage import Usage
from .v1_chat_completions_create_data_body import V1ChatCompletionsCreateDataBody, V1ChatCompletionsCreateDataBodyDict
from .v1_chat_completions_create_data_body_logit_bias_type_0 import V1ChatCompletionsCreateDataBodyLogitBiasType0
from .v1_chat_completions_create_data_body_messages_item import V1ChatCompletionsCreateDataBodyMessagesItem
from .v1_chat_completions_create_data_body_messages_item_role import V1ChatCompletionsCreateDataBodyMessagesItemRole
from .v1_chat_completions_create_data_body_response_format_type_0 import (
    V1ChatCompletionsCreateDataBodyResponseFormatType0,
)
from .v1_chat_completions_create_data_body_tools_item import V1ChatCompletionsCreateDataBodyToolsItem
from .v1_chat_completions_create_files_body import (
    V1ChatCompletionsCreateFilesBody,
    V1ChatCompletionsCreateFilesBodyDict,
)
from .v1_chat_completions_create_files_body_logit_bias_type_0 import V1ChatCompletionsCreateFilesBodyLogitBiasType0
from .v1_chat_completions_create_files_body_messages_item import V1ChatCompletionsCreateFilesBodyMessagesItem
from .v1_chat_completions_create_files_body_messages_item_role import V1ChatCompletionsCreateFilesBodyMessagesItemRole
from .v1_chat_completions_create_files_body_response_format_type_0 import (
    V1ChatCompletionsCreateFilesBodyResponseFormatType0,
)
from .v1_chat_completions_create_files_body_tools_item import V1ChatCompletionsCreateFilesBodyToolsItem
from .v1_chat_completions_create_json_body import V1ChatCompletionsCreateJsonBody, V1ChatCompletionsCreateJsonBodyDict
from .v1_chat_completions_create_json_body_logit_bias_type_0 import V1ChatCompletionsCreateJsonBodyLogitBiasType0
from .v1_chat_completions_create_json_body_messages_item import V1ChatCompletionsCreateJsonBodyMessagesItem
from .v1_chat_completions_create_json_body_messages_item_role import V1ChatCompletionsCreateJsonBodyMessagesItemRole
from .v1_chat_completions_create_json_body_response_format_type_0 import (
    V1ChatCompletionsCreateJsonBodyResponseFormatType0,
)
from .v1_chat_completions_create_json_body_tools_item import V1ChatCompletionsCreateJsonBodyToolsItem
from .v1_chat_completions_create_response_200 import V1ChatCompletionsCreateResponse200
from .v1_chat_completions_create_response_200_choices_item import V1ChatCompletionsCreateResponse200ChoicesItem
from .v1_chat_completions_create_response_200_usage import V1ChatCompletionsCreateResponse200Usage
from .v1_chat_completions_create_response_400 import V1ChatCompletionsCreateResponse400
from .v1_chat_completions_create_response_400_code import V1ChatCompletionsCreateResponse400Code
from .v1_chat_completions_create_response_400_details import V1ChatCompletionsCreateResponse400Details
from .v1_chat_completions_create_response_400_details_additional_property import (
    V1ChatCompletionsCreateResponse400DetailsAdditionalProperty,
)
from .v1_chat_completions_create_response_400_details_additional_property_error_messages_item import (
    V1ChatCompletionsCreateResponse400DetailsAdditionalPropertyErrorMessagesItem,
)
from .v1_chat_completions_create_response_401 import V1ChatCompletionsCreateResponse401
from .v1_chat_completions_create_response_401_code import V1ChatCompletionsCreateResponse401Code
from .v1_chat_completions_create_response_403 import V1ChatCompletionsCreateResponse403
from .v1_chat_completions_create_response_403_code import V1ChatCompletionsCreateResponse403Code
from .v1_chat_completions_create_response_404_type_0 import V1ChatCompletionsCreateResponse404Type0
from .v1_chat_completions_create_response_404_type_0_code import V1ChatCompletionsCreateResponse404Type0Code
from .v1_chat_completions_create_response_404_type_1 import V1ChatCompletionsCreateResponse404Type1
from .v1_chat_completions_create_response_404_type_1_code import V1ChatCompletionsCreateResponse404Type1Code
from .v1_chat_completions_create_response_409 import V1ChatCompletionsCreateResponse409
from .v1_chat_completions_create_response_409_code import V1ChatCompletionsCreateResponse409Code
from .v1_chat_completions_create_response_422 import V1ChatCompletionsCreateResponse422
from .v1_chat_completions_create_response_422_code import V1ChatCompletionsCreateResponse422Code
from .v1_chat_completions_create_response_429 import V1ChatCompletionsCreateResponse429
from .v1_chat_completions_create_response_429_code import V1ChatCompletionsCreateResponse429Code
from .v1_chat_completions_create_response_500_type_0 import V1ChatCompletionsCreateResponse500Type0
from .v1_chat_completions_create_response_500_type_0_code import V1ChatCompletionsCreateResponse500Type0Code
from .v1_chat_completions_create_response_500_type_1 import V1ChatCompletionsCreateResponse500Type1
from .v1_chat_completions_create_response_500_type_1_code import V1ChatCompletionsCreateResponse500Type1Code
from .v1_chat_completions_create_response_500_type_2 import V1ChatCompletionsCreateResponse500Type2
from .v1_chat_completions_create_response_500_type_2_code import V1ChatCompletionsCreateResponse500Type2Code
from .v1_chat_completions_create_response_500_type_3 import V1ChatCompletionsCreateResponse500Type3
from .v1_chat_completions_create_response_500_type_3_code import V1ChatCompletionsCreateResponse500Type3Code
from .v1_chat_completions_create_response_500_type_4 import V1ChatCompletionsCreateResponse500Type4
from .v1_chat_completions_create_response_500_type_4_code import V1ChatCompletionsCreateResponse500Type4Code
from .v1_chat_completions_create_response_500_type_5 import V1ChatCompletionsCreateResponse500Type5
from .v1_chat_completions_create_response_500_type_5_code import V1ChatCompletionsCreateResponse500Type5Code
from .v1_data_points_create_data_body import V1DataPointsCreateDataBody, V1DataPointsCreateDataBodyDict
from .v1_data_points_create_files_body import V1DataPointsCreateFilesBody, V1DataPointsCreateFilesBodyDict
from .v1_data_points_create_json_body import V1DataPointsCreateJsonBody, V1DataPointsCreateJsonBodyDict
from .v1_data_points_create_response_201 import V1DataPointsCreateResponse201
from .v1_data_points_list_response_200_item import V1DataPointsListResponse200Item
from .v1_data_points_partial_update_data_body import (
    V1DataPointsPartialUpdateDataBody,
    V1DataPointsPartialUpdateDataBodyDict,
)
from .v1_data_points_partial_update_files_body import (
    V1DataPointsPartialUpdateFilesBody,
    V1DataPointsPartialUpdateFilesBodyDict,
)
from .v1_data_points_partial_update_json_body import (
    V1DataPointsPartialUpdateJsonBody,
    V1DataPointsPartialUpdateJsonBodyDict,
)
from .v1_data_points_partial_update_response_200 import V1DataPointsPartialUpdateResponse200
from .v1_data_points_retrieve_response_200 import V1DataPointsRetrieveResponse200
from .v1_data_points_update_data_body import V1DataPointsUpdateDataBody, V1DataPointsUpdateDataBodyDict
from .v1_data_points_update_files_body import V1DataPointsUpdateFilesBody, V1DataPointsUpdateFilesBodyDict
from .v1_data_points_update_json_body import V1DataPointsUpdateJsonBody, V1DataPointsUpdateJsonBodyDict
from .v1_data_points_update_response_200 import V1DataPointsUpdateResponse200
from .v1_embeddings_create_data_body import V1EmbeddingsCreateDataBody, V1EmbeddingsCreateDataBodyDict
from .v1_embeddings_create_data_body_encoding_format import V1EmbeddingsCreateDataBodyEncodingFormat
from .v1_embeddings_create_files_body import V1EmbeddingsCreateFilesBody, V1EmbeddingsCreateFilesBodyDict
from .v1_embeddings_create_files_body_encoding_format import V1EmbeddingsCreateFilesBodyEncodingFormat
from .v1_embeddings_create_json_body import V1EmbeddingsCreateJsonBody, V1EmbeddingsCreateJsonBodyDict
from .v1_embeddings_create_json_body_encoding_format import V1EmbeddingsCreateJsonBodyEncodingFormat
from .v1_embeddings_create_response_200 import V1EmbeddingsCreateResponse200
from .v1_embeddings_create_response_200_data_item import V1EmbeddingsCreateResponse200DataItem
from .v1_embeddings_create_response_200_usage import V1EmbeddingsCreateResponse200Usage
from .v1_embeddings_create_response_400 import V1EmbeddingsCreateResponse400
from .v1_embeddings_create_response_400_code import V1EmbeddingsCreateResponse400Code
from .v1_embeddings_create_response_400_details import V1EmbeddingsCreateResponse400Details
from .v1_embeddings_create_response_400_details_additional_property import (
    V1EmbeddingsCreateResponse400DetailsAdditionalProperty,
)
from .v1_embeddings_create_response_400_details_additional_property_error_messages_item import (
    V1EmbeddingsCreateResponse400DetailsAdditionalPropertyErrorMessagesItem,
)
from .v1_embeddings_create_response_401 import V1EmbeddingsCreateResponse401
from .v1_embeddings_create_response_401_code import V1EmbeddingsCreateResponse401Code
from .v1_embeddings_create_response_403 import V1EmbeddingsCreateResponse403
from .v1_embeddings_create_response_403_code import V1EmbeddingsCreateResponse403Code
from .v1_embeddings_create_response_404_type_0 import V1EmbeddingsCreateResponse404Type0
from .v1_embeddings_create_response_404_type_0_code import V1EmbeddingsCreateResponse404Type0Code
from .v1_embeddings_create_response_404_type_1 import V1EmbeddingsCreateResponse404Type1
from .v1_embeddings_create_response_404_type_1_code import V1EmbeddingsCreateResponse404Type1Code
from .v1_embeddings_create_response_409 import V1EmbeddingsCreateResponse409
from .v1_embeddings_create_response_409_code import V1EmbeddingsCreateResponse409Code
from .v1_embeddings_create_response_422 import V1EmbeddingsCreateResponse422
from .v1_embeddings_create_response_422_code import V1EmbeddingsCreateResponse422Code
from .v1_embeddings_create_response_429 import V1EmbeddingsCreateResponse429
from .v1_embeddings_create_response_429_code import V1EmbeddingsCreateResponse429Code
from .v1_embeddings_create_response_500_type_0 import V1EmbeddingsCreateResponse500Type0
from .v1_embeddings_create_response_500_type_0_code import V1EmbeddingsCreateResponse500Type0Code
from .v1_embeddings_create_response_500_type_1 import V1EmbeddingsCreateResponse500Type1
from .v1_embeddings_create_response_500_type_1_code import V1EmbeddingsCreateResponse500Type1Code
from .v1_embeddings_create_response_500_type_2 import V1EmbeddingsCreateResponse500Type2
from .v1_embeddings_create_response_500_type_2_code import V1EmbeddingsCreateResponse500Type2Code
from .v1_embeddings_create_response_500_type_3 import V1EmbeddingsCreateResponse500Type3
from .v1_embeddings_create_response_500_type_3_code import V1EmbeddingsCreateResponse500Type3Code
from .v1_embeddings_create_response_500_type_4 import V1EmbeddingsCreateResponse500Type4
from .v1_embeddings_create_response_500_type_4_code import V1EmbeddingsCreateResponse500Type4Code
from .v1_embeddings_create_response_500_type_5 import V1EmbeddingsCreateResponse500Type5
from .v1_embeddings_create_response_500_type_5_code import V1EmbeddingsCreateResponse500Type5Code
from .v1_finetuning_create_data_body import V1FinetuningCreateDataBody, V1FinetuningCreateDataBodyDict
from .v1_finetuning_create_data_body_training_data_item import V1FinetuningCreateDataBodyTrainingDataItem
from .v1_finetuning_create_data_body_validaton_data_item import V1FinetuningCreateDataBodyValidatonDataItem
from .v1_finetuning_create_files_body import V1FinetuningCreateFilesBody, V1FinetuningCreateFilesBodyDict
from .v1_finetuning_create_files_body_training_data_item import V1FinetuningCreateFilesBodyTrainingDataItem
from .v1_finetuning_create_files_body_validaton_data_item import V1FinetuningCreateFilesBodyValidatonDataItem
from .v1_finetuning_create_json_body import V1FinetuningCreateJsonBody, V1FinetuningCreateJsonBodyDict
from .v1_finetuning_create_json_body_training_data_item import V1FinetuningCreateJsonBodyTrainingDataItem
from .v1_finetuning_create_json_body_validaton_data_item import V1FinetuningCreateJsonBodyValidatonDataItem
from .v1_finetuning_create_response_200 import V1FinetuningCreateResponse200
from .v1_finetuning_create_response_400 import V1FinetuningCreateResponse400
from .v1_finetuning_create_response_400_code import V1FinetuningCreateResponse400Code
from .v1_finetuning_create_response_400_details import V1FinetuningCreateResponse400Details
from .v1_finetuning_create_response_400_details_additional_property import (
    V1FinetuningCreateResponse400DetailsAdditionalProperty,
)
from .v1_finetuning_create_response_400_details_additional_property_error_messages_item import (
    V1FinetuningCreateResponse400DetailsAdditionalPropertyErrorMessagesItem,
)
from .v1_finetuning_create_response_401 import V1FinetuningCreateResponse401
from .v1_finetuning_create_response_401_code import V1FinetuningCreateResponse401Code
from .v1_finetuning_create_response_403 import V1FinetuningCreateResponse403
from .v1_finetuning_create_response_403_code import V1FinetuningCreateResponse403Code
from .v1_finetuning_create_response_404_type_0 import V1FinetuningCreateResponse404Type0
from .v1_finetuning_create_response_404_type_0_code import V1FinetuningCreateResponse404Type0Code
from .v1_finetuning_create_response_404_type_1 import V1FinetuningCreateResponse404Type1
from .v1_finetuning_create_response_404_type_1_code import V1FinetuningCreateResponse404Type1Code
from .v1_finetuning_create_response_409 import V1FinetuningCreateResponse409
from .v1_finetuning_create_response_409_code import V1FinetuningCreateResponse409Code
from .v1_finetuning_create_response_422 import V1FinetuningCreateResponse422
from .v1_finetuning_create_response_422_code import V1FinetuningCreateResponse422Code
from .v1_finetuning_create_response_429 import V1FinetuningCreateResponse429
from .v1_finetuning_create_response_429_code import V1FinetuningCreateResponse429Code
from .v1_finetuning_create_response_500_type_0 import V1FinetuningCreateResponse500Type0
from .v1_finetuning_create_response_500_type_0_code import V1FinetuningCreateResponse500Type0Code
from .v1_finetuning_create_response_500_type_1 import V1FinetuningCreateResponse500Type1
from .v1_finetuning_create_response_500_type_1_code import V1FinetuningCreateResponse500Type1Code
from .v1_finetuning_create_response_500_type_2 import V1FinetuningCreateResponse500Type2
from .v1_finetuning_create_response_500_type_2_code import V1FinetuningCreateResponse500Type2Code
from .v1_finetuning_create_response_500_type_3 import V1FinetuningCreateResponse500Type3
from .v1_finetuning_create_response_500_type_3_code import V1FinetuningCreateResponse500Type3Code
from .v1_finetuning_create_response_500_type_4 import V1FinetuningCreateResponse500Type4
from .v1_finetuning_create_response_500_type_4_code import V1FinetuningCreateResponse500Type4Code
from .v1_finetuning_create_response_500_type_5 import V1FinetuningCreateResponse500Type5
from .v1_finetuning_create_response_500_type_5_code import V1FinetuningCreateResponse500Type5Code
from .v1_finetuning_retrieve_response_200 import V1FinetuningRetrieveResponse200
from .v1_finetuning_retrieve_response_400 import V1FinetuningRetrieveResponse400
from .v1_finetuning_retrieve_response_400_code import V1FinetuningRetrieveResponse400Code
from .v1_finetuning_retrieve_response_400_details import V1FinetuningRetrieveResponse400Details
from .v1_finetuning_retrieve_response_400_details_additional_property import (
    V1FinetuningRetrieveResponse400DetailsAdditionalProperty,
)
from .v1_finetuning_retrieve_response_400_details_additional_property_error_messages_item import (
    V1FinetuningRetrieveResponse400DetailsAdditionalPropertyErrorMessagesItem,
)
from .v1_finetuning_retrieve_response_401 import V1FinetuningRetrieveResponse401
from .v1_finetuning_retrieve_response_401_code import V1FinetuningRetrieveResponse401Code
from .v1_finetuning_retrieve_response_403 import V1FinetuningRetrieveResponse403
from .v1_finetuning_retrieve_response_403_code import V1FinetuningRetrieveResponse403Code
from .v1_finetuning_retrieve_response_404_type_0 import V1FinetuningRetrieveResponse404Type0
from .v1_finetuning_retrieve_response_404_type_0_code import V1FinetuningRetrieveResponse404Type0Code
from .v1_finetuning_retrieve_response_404_type_1 import V1FinetuningRetrieveResponse404Type1
from .v1_finetuning_retrieve_response_404_type_1_code import V1FinetuningRetrieveResponse404Type1Code
from .v1_finetuning_retrieve_response_409 import V1FinetuningRetrieveResponse409
from .v1_finetuning_retrieve_response_409_code import V1FinetuningRetrieveResponse409Code
from .v1_finetuning_retrieve_response_422 import V1FinetuningRetrieveResponse422
from .v1_finetuning_retrieve_response_422_code import V1FinetuningRetrieveResponse422Code
from .v1_finetuning_retrieve_response_429 import V1FinetuningRetrieveResponse429
from .v1_finetuning_retrieve_response_429_code import V1FinetuningRetrieveResponse429Code
from .v1_finetuning_retrieve_response_500_type_0 import V1FinetuningRetrieveResponse500Type0
from .v1_finetuning_retrieve_response_500_type_0_code import V1FinetuningRetrieveResponse500Type0Code
from .v1_finetuning_retrieve_response_500_type_1 import V1FinetuningRetrieveResponse500Type1
from .v1_finetuning_retrieve_response_500_type_1_code import V1FinetuningRetrieveResponse500Type1Code
from .v1_finetuning_retrieve_response_500_type_2 import V1FinetuningRetrieveResponse500Type2
from .v1_finetuning_retrieve_response_500_type_2_code import V1FinetuningRetrieveResponse500Type2Code
from .v1_finetuning_retrieve_response_500_type_3 import V1FinetuningRetrieveResponse500Type3
from .v1_finetuning_retrieve_response_500_type_3_code import V1FinetuningRetrieveResponse500Type3Code
from .v1_finetuning_retrieve_response_500_type_4 import V1FinetuningRetrieveResponse500Type4
from .v1_finetuning_retrieve_response_500_type_4_code import V1FinetuningRetrieveResponse500Type4Code
from .v1_finetuning_retrieve_response_500_type_5 import V1FinetuningRetrieveResponse500Type5
from .v1_finetuning_retrieve_response_500_type_5_code import V1FinetuningRetrieveResponse500Type5Code
from .validation_detail import ValidationDetail
from .validation_detail_error_messages_item import ValidationDetailErrorMessagesItem
from .validation_error import ValidationError
from .validation_error_code import ValidationErrorCode
from .validation_error_code_enum import ValidationErrorCodeEnum
from .validation_error_details import ValidationErrorDetails
from .validation_error_details_additional_property import ValidationErrorDetailsAdditionalProperty
from .validation_error_details_additional_property_error_messages_item import (
    ValidationErrorDetailsAdditionalPropertyErrorMessagesItem,
)

__all__ = (
    "APIResponseValidationError",
    "APIResponseValidationErrorCode",
    "APIResponseValidationErrorCodeEnum",
    "AuthenticationError",
    "AuthenticationErrorCode",
    "AuthenticationErrorCodeEnum",
    "CatchAllError",
    "CatchAllErrorCode",
    "CatchAllErrorCodeEnum",
    "ChatCompletionInput",
    "ChatCompletionInputLogitBiasType0",
    "ChatCompletionInputMessagesItem",
    "ChatCompletionInputMessagesItemRole",
    "ChatCompletionInputResponseFormatType0",
    "ChatCompletionInputToolsItem",
    "ChatCompletionResponse",
    "ChatCompletionResponseChoicesItem",
    "ChatCompletionResponseUsage",
    "ConflictError",
    "ConflictErrorCode",
    "ConflictErrorCodeEnum",
    "DataPoint",
    "Embedding",
    "EmbeddingsInput",
    "EmbeddingsInputEncodingFormat",
    "EmbeddingsResponse",
    "EmbeddingsResponseDataItem",
    "EmbeddingsResponseUsage",
    "EncodingFormatEnum",
    "FineTuningInput",
    "FineTuningInputTrainingDataItem",
    "FineTuningInputValidatonDataItem",
    "FineTuningResponse",
    "FineTuningSample",
    "InputDataPoint",
    "InternalServerErrorType0",
    "InternalServerErrorType0Code",
    "InternalServerErrorType1",
    "InternalServerErrorType1Code",
    "InternalServerErrorType2",
    "InternalServerErrorType2Code",
    "InternalServerErrorType3",
    "InternalServerErrorType3Code",
    "InternalServerErrorType4",
    "InternalServerErrorType4Code",
    "InternalServerErrorType5",
    "InternalServerErrorType5Code",
    "Message",
    "MessageRole",
    "ModelNotFoundError",
    "ModelNotFoundErrorCode",
    "ModelNotFoundErrorCodeEnum",
    "NotFoundErrorType0",
    "NotFoundErrorType0Code",
    "NotFoundErrorType1",
    "NotFoundErrorType1Code",
    "PatchedDataPoint",
    "PermissionDeniedError",
    "PermissionDeniedErrorCode",
    "PermissionDeniedErrorCodeEnum",
    "ProviderAPIConnectionError",
    "ProviderAPIConnectionErrorCode",
    "ProviderAPIConnectionErrorCodeEnum",
    "ProviderAPIStatusError",
    "ProviderAPIStatusErrorCode",
    "ProviderAPIStatusErrorCodeEnum",
    "ProviderAPITimeoutError",
    "ProviderAPITimeoutErrorCode",
    "ProviderAPITimeoutErrorCodeEnum",
    "ProviderInternalServerError",
    "ProviderInternalServerErrorCode",
    "ProviderInternalServerErrorCodeEnum",
    "ProviderNotFoundError",
    "ProviderNotFoundErrorCode",
    "ProviderNotFoundErrorCodeEnum",
    "RateLimitError",
    "RateLimitErrorCode",
    "RateLimitErrorCodeEnum",
    "ResponseChoice",
    "RetrieveFineTuningResponse",
    "RoleEnum",
    "UnprocessableEntityError",
    "UnprocessableEntityErrorCode",
    "UnprocessableEntityErrorCodeEnum",
    "Usage",
    "V1ChatCompletionsCreateDataBody",
    "V1ChatCompletionsCreateDataBodyLogitBiasType0",
    "V1ChatCompletionsCreateDataBodyMessagesItem",
    "V1ChatCompletionsCreateDataBodyMessagesItemRole",
    "V1ChatCompletionsCreateDataBodyResponseFormatType0",
    "V1ChatCompletionsCreateDataBodyToolsItem",
    "V1ChatCompletionsCreateFilesBody",
    "V1ChatCompletionsCreateFilesBodyLogitBiasType0",
    "V1ChatCompletionsCreateFilesBodyMessagesItem",
    "V1ChatCompletionsCreateFilesBodyMessagesItemRole",
    "V1ChatCompletionsCreateFilesBodyResponseFormatType0",
    "V1ChatCompletionsCreateFilesBodyToolsItem",
    "V1ChatCompletionsCreateJsonBody",
    "V1ChatCompletionsCreateJsonBodyLogitBiasType0",
    "V1ChatCompletionsCreateJsonBodyMessagesItem",
    "V1ChatCompletionsCreateJsonBodyMessagesItemRole",
    "V1ChatCompletionsCreateJsonBodyResponseFormatType0",
    "V1ChatCompletionsCreateJsonBodyToolsItem",
    "V1ChatCompletionsCreateResponse200",
    "V1ChatCompletionsCreateResponse200ChoicesItem",
    "V1ChatCompletionsCreateResponse200Usage",
    "V1ChatCompletionsCreateResponse400",
    "V1ChatCompletionsCreateResponse400Code",
    "V1ChatCompletionsCreateResponse400Details",
    "V1ChatCompletionsCreateResponse400DetailsAdditionalProperty",
    "V1ChatCompletionsCreateResponse400DetailsAdditionalPropertyErrorMessagesItem",
    "V1ChatCompletionsCreateResponse401",
    "V1ChatCompletionsCreateResponse401Code",
    "V1ChatCompletionsCreateResponse403",
    "V1ChatCompletionsCreateResponse403Code",
    "V1ChatCompletionsCreateResponse404Type0",
    "V1ChatCompletionsCreateResponse404Type0Code",
    "V1ChatCompletionsCreateResponse404Type1",
    "V1ChatCompletionsCreateResponse404Type1Code",
    "V1ChatCompletionsCreateResponse409",
    "V1ChatCompletionsCreateResponse409Code",
    "V1ChatCompletionsCreateResponse422",
    "V1ChatCompletionsCreateResponse422Code",
    "V1ChatCompletionsCreateResponse429",
    "V1ChatCompletionsCreateResponse429Code",
    "V1ChatCompletionsCreateResponse500Type0",
    "V1ChatCompletionsCreateResponse500Type0Code",
    "V1ChatCompletionsCreateResponse500Type1",
    "V1ChatCompletionsCreateResponse500Type1Code",
    "V1ChatCompletionsCreateResponse500Type2",
    "V1ChatCompletionsCreateResponse500Type2Code",
    "V1ChatCompletionsCreateResponse500Type3",
    "V1ChatCompletionsCreateResponse500Type3Code",
    "V1ChatCompletionsCreateResponse500Type4",
    "V1ChatCompletionsCreateResponse500Type4Code",
    "V1ChatCompletionsCreateResponse500Type5",
    "V1ChatCompletionsCreateResponse500Type5Code",
    "V1DataPointsCreateDataBody",
    "V1DataPointsCreateFilesBody",
    "V1DataPointsCreateJsonBody",
    "V1DataPointsCreateResponse201",
    "V1DataPointsListResponse200Item",
    "V1DataPointsPartialUpdateDataBody",
    "V1DataPointsPartialUpdateFilesBody",
    "V1DataPointsPartialUpdateJsonBody",
    "V1DataPointsPartialUpdateResponse200",
    "V1DataPointsRetrieveResponse200",
    "V1DataPointsUpdateDataBody",
    "V1DataPointsUpdateFilesBody",
    "V1DataPointsUpdateJsonBody",
    "V1DataPointsUpdateResponse200",
    "V1EmbeddingsCreateDataBody",
    "V1EmbeddingsCreateDataBodyEncodingFormat",
    "V1EmbeddingsCreateFilesBody",
    "V1EmbeddingsCreateFilesBodyEncodingFormat",
    "V1EmbeddingsCreateJsonBody",
    "V1EmbeddingsCreateJsonBodyEncodingFormat",
    "V1EmbeddingsCreateResponse200",
    "V1EmbeddingsCreateResponse200DataItem",
    "V1EmbeddingsCreateResponse200Usage",
    "V1EmbeddingsCreateResponse400",
    "V1EmbeddingsCreateResponse400Code",
    "V1EmbeddingsCreateResponse400Details",
    "V1EmbeddingsCreateResponse400DetailsAdditionalProperty",
    "V1EmbeddingsCreateResponse400DetailsAdditionalPropertyErrorMessagesItem",
    "V1EmbeddingsCreateResponse401",
    "V1EmbeddingsCreateResponse401Code",
    "V1EmbeddingsCreateResponse403",
    "V1EmbeddingsCreateResponse403Code",
    "V1EmbeddingsCreateResponse404Type0",
    "V1EmbeddingsCreateResponse404Type0Code",
    "V1EmbeddingsCreateResponse404Type1",
    "V1EmbeddingsCreateResponse404Type1Code",
    "V1EmbeddingsCreateResponse409",
    "V1EmbeddingsCreateResponse409Code",
    "V1EmbeddingsCreateResponse422",
    "V1EmbeddingsCreateResponse422Code",
    "V1EmbeddingsCreateResponse429",
    "V1EmbeddingsCreateResponse429Code",
    "V1EmbeddingsCreateResponse500Type0",
    "V1EmbeddingsCreateResponse500Type0Code",
    "V1EmbeddingsCreateResponse500Type1",
    "V1EmbeddingsCreateResponse500Type1Code",
    "V1EmbeddingsCreateResponse500Type2",
    "V1EmbeddingsCreateResponse500Type2Code",
    "V1EmbeddingsCreateResponse500Type3",
    "V1EmbeddingsCreateResponse500Type3Code",
    "V1EmbeddingsCreateResponse500Type4",
    "V1EmbeddingsCreateResponse500Type4Code",
    "V1EmbeddingsCreateResponse500Type5",
    "V1EmbeddingsCreateResponse500Type5Code",
    "V1FinetuningCreateDataBody",
    "V1FinetuningCreateDataBodyTrainingDataItem",
    "V1FinetuningCreateDataBodyValidatonDataItem",
    "V1FinetuningCreateFilesBody",
    "V1FinetuningCreateFilesBodyTrainingDataItem",
    "V1FinetuningCreateFilesBodyValidatonDataItem",
    "V1FinetuningCreateJsonBody",
    "V1FinetuningCreateJsonBodyTrainingDataItem",
    "V1FinetuningCreateJsonBodyValidatonDataItem",
    "V1FinetuningCreateResponse200",
    "V1FinetuningCreateResponse400",
    "V1FinetuningCreateResponse400Code",
    "V1FinetuningCreateResponse400Details",
    "V1FinetuningCreateResponse400DetailsAdditionalProperty",
    "V1FinetuningCreateResponse400DetailsAdditionalPropertyErrorMessagesItem",
    "V1FinetuningCreateResponse401",
    "V1FinetuningCreateResponse401Code",
    "V1FinetuningCreateResponse403",
    "V1FinetuningCreateResponse403Code",
    "V1FinetuningCreateResponse404Type0",
    "V1FinetuningCreateResponse404Type0Code",
    "V1FinetuningCreateResponse404Type1",
    "V1FinetuningCreateResponse404Type1Code",
    "V1FinetuningCreateResponse409",
    "V1FinetuningCreateResponse409Code",
    "V1FinetuningCreateResponse422",
    "V1FinetuningCreateResponse422Code",
    "V1FinetuningCreateResponse429",
    "V1FinetuningCreateResponse429Code",
    "V1FinetuningCreateResponse500Type0",
    "V1FinetuningCreateResponse500Type0Code",
    "V1FinetuningCreateResponse500Type1",
    "V1FinetuningCreateResponse500Type1Code",
    "V1FinetuningCreateResponse500Type2",
    "V1FinetuningCreateResponse500Type2Code",
    "V1FinetuningCreateResponse500Type3",
    "V1FinetuningCreateResponse500Type3Code",
    "V1FinetuningCreateResponse500Type4",
    "V1FinetuningCreateResponse500Type4Code",
    "V1FinetuningCreateResponse500Type5",
    "V1FinetuningCreateResponse500Type5Code",
    "V1FinetuningRetrieveResponse200",
    "V1FinetuningRetrieveResponse400",
    "V1FinetuningRetrieveResponse400Code",
    "V1FinetuningRetrieveResponse400Details",
    "V1FinetuningRetrieveResponse400DetailsAdditionalProperty",
    "V1FinetuningRetrieveResponse400DetailsAdditionalPropertyErrorMessagesItem",
    "V1FinetuningRetrieveResponse401",
    "V1FinetuningRetrieveResponse401Code",
    "V1FinetuningRetrieveResponse403",
    "V1FinetuningRetrieveResponse403Code",
    "V1FinetuningRetrieveResponse404Type0",
    "V1FinetuningRetrieveResponse404Type0Code",
    "V1FinetuningRetrieveResponse404Type1",
    "V1FinetuningRetrieveResponse404Type1Code",
    "V1FinetuningRetrieveResponse409",
    "V1FinetuningRetrieveResponse409Code",
    "V1FinetuningRetrieveResponse422",
    "V1FinetuningRetrieveResponse422Code",
    "V1FinetuningRetrieveResponse429",
    "V1FinetuningRetrieveResponse429Code",
    "V1FinetuningRetrieveResponse500Type0",
    "V1FinetuningRetrieveResponse500Type0Code",
    "V1FinetuningRetrieveResponse500Type1",
    "V1FinetuningRetrieveResponse500Type1Code",
    "V1FinetuningRetrieveResponse500Type2",
    "V1FinetuningRetrieveResponse500Type2Code",
    "V1FinetuningRetrieveResponse500Type3",
    "V1FinetuningRetrieveResponse500Type3Code",
    "V1FinetuningRetrieveResponse500Type4",
    "V1FinetuningRetrieveResponse500Type4Code",
    "V1FinetuningRetrieveResponse500Type5",
    "V1FinetuningRetrieveResponse500Type5Code",
    "ValidationDetail",
    "ValidationDetailErrorMessagesItem",
    "ValidationError",
    "ValidationErrorCode",
    "ValidationErrorCodeEnum",
    "ValidationErrorDetails",
    "ValidationErrorDetailsAdditionalProperty",
    "ValidationErrorDetailsAdditionalPropertyErrorMessagesItem",
    "V1ChatCompletionsCreateJsonBodyDict",
    "V1ChatCompletionsCreateDataBodyDict",
    "V1ChatCompletionsCreateFilesBodyDict",
    "V1DataPointsCreateJsonBodyDict",
    "V1DataPointsCreateDataBodyDict",
    "V1DataPointsCreateFilesBodyDict",
    "V1DataPointsUpdateJsonBodyDict",
    "V1DataPointsUpdateDataBodyDict",
    "V1DataPointsUpdateFilesBodyDict",
    "V1DataPointsPartialUpdateJsonBodyDict",
    "V1DataPointsPartialUpdateDataBodyDict",
    "V1DataPointsPartialUpdateFilesBodyDict",
    "V1EmbeddingsCreateJsonBodyDict",
    "V1EmbeddingsCreateDataBodyDict",
    "V1EmbeddingsCreateFilesBodyDict",
    "V1FinetuningCreateJsonBodyDict",
    "V1FinetuningCreateDataBodyDict",
    "V1FinetuningCreateFilesBodyDict",
)
