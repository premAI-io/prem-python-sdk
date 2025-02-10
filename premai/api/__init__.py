""" Contains methods for accessing the API """








from typing_extensions import Unpack

from .repositories.api_repositories_repositories_create import api_repositories_repositories_create_wrapper
from ..types import Unset, UNSET

from ..models import(
    RepositoryDict,
    RepositoryDict,
    RepositoryDict,
)
from ..models.repository import Repository
from typing import Dict
from typing import cast

from .repository_document.api_repositories_repository_document_create import api_repositories_repository_document_create_wrapper
from ..types import Unset, UNSET

from ..models import(
    DocumentInputDict,
)
from typing import Dict
from typing import cast
from ..models.document_input import DocumentInput
from ..models.document_output import DocumentOutput

from .chat_completions.v1_chat_completions_create import v1_chat_completions_create_wrapper
from ..types import Unset, UNSET

from ..models import(
    ChatCompletionInputDict,
    ChatCompletionInputDict,
    ChatCompletionInputDict,
)
from ..models.conflict_error import ConflictError
from typing import Dict
from ..models.provider_internal_server_error import ProviderInternalServerError
from typing import cast
from ..models.model_not_found_error import ModelNotFoundError
from ..models.provider_api_connection_error import ProviderAPIConnectionError
from ..models.provider_not_found_error import ProviderNotFoundError
from ..models.rate_limit_error import RateLimitError
from ..models.unprocessable_entity_error import UnprocessableEntityError
from ..models.provider_api_timeout_error import ProviderAPITimeoutError
from ..models.validation_error import ValidationError
from ..models.chat_completion_input import ChatCompletionInput
from ..models.catch_all_error import CatchAllError
from typing import cast, Union
from ..models.permission_denied_error import PermissionDeniedError
from ..models.api_response_validation_error import APIResponseValidationError
from ..models.provider_api_status_error import ProviderAPIStatusError
from ..models.authentication_error import AuthenticationError
from ..models.chat_completion_response import ChatCompletionResponse

from .embeddings.v1_embeddings_create import v1_embeddings_create_wrapper
from ..types import Unset, UNSET

from ..models import(
    EmbeddingsInputDict,
    EmbeddingsInputDict,
    EmbeddingsInputDict,
)
from ..models.conflict_error import ConflictError
from typing import Dict
from ..models.provider_internal_server_error import ProviderInternalServerError
from typing import cast
from ..models.model_not_found_error import ModelNotFoundError
from ..models.provider_api_connection_error import ProviderAPIConnectionError
from ..models.provider_not_found_error import ProviderNotFoundError
from ..models.embeddings_input import EmbeddingsInput
from ..models.rate_limit_error import RateLimitError
from ..models.unprocessable_entity_error import UnprocessableEntityError
from ..models.provider_api_timeout_error import ProviderAPITimeoutError
from ..models.validation_error import ValidationError
from ..models.catch_all_error import CatchAllError
from typing import cast, Union
from ..models.permission_denied_error import PermissionDeniedError
from ..models.api_response_validation_error import APIResponseValidationError
from ..models.embeddings_response import EmbeddingsResponse
from ..models.provider_api_status_error import ProviderAPIStatusError
from ..models.authentication_error import AuthenticationError

from .v1.v1_get_dataset_retrieve import v1_get_dataset_retrieve_wrapper
from ..types import Unset, UNSET


from .models.v1_models_list import v1_models_list_wrapper
from ..types import Unset, UNSET

from ..models.model import Model
from typing import cast
from typing import cast, List
from typing import Dict

from .models.v1_models_retrieve import v1_models_retrieve_wrapper
from ..types import Unset, UNSET

from ..models.model import Model
from typing import cast
from typing import Dict

from .feedbacks.v1_set_trace_feedback_create import v1_set_trace_feedback_create_wrapper
from ..types import Unset, UNSET

from ..models import(
    FeedbackCreateDict,
    FeedbackCreateDict,
    FeedbackCreateDict,
)
from typing import Dict
from typing import cast
from ..models.feedback_create import FeedbackCreate

from .traces.v1_traces_list import v1_traces_list_wrapper
from ..types import Unset, UNSET

from typing import cast, List
from typing import Dict
from typing import Union
from ..models.v1_traces_list_admin_filter import V1TracesListAdminFilter
from typing import cast
from ..models.v1_traces_list_date_filter import V1TracesListDateFilter
from ..types import UNSET, Unset
from ..models.trace_list import TraceList

from .traces.v1_traces_retrieve import v1_traces_retrieve_wrapper
from ..types import Unset, UNSET

from typing import Dict
from typing import cast
from ..models.trace_retrieve import TraceRetrieve

class RepositoriesModule:
    def __init__(self, client):
      self._client = client

    def create(self,
        **kwargs: Unpack[RepositoryDict]
    ): 
        return api_repositories_repositories_create_wrapper(self._client)(
            **kwargs
        )

class RepositoryDocumentModule:
    def __init__(self, client):
      self._client = client

    def create(self,
        repository_id: int,
        **kwargs: Unpack[DocumentInputDict]
    ): 
        return api_repositories_repository_document_create_wrapper(self._client)(
            repository_id,
            **kwargs
        )

class ChatCompletionsModule:
    def __init__(self, client):
      self._client = client

    def create(self,
        **kwargs: Unpack[ChatCompletionInputDict]
    ): 
        return v1_chat_completions_create_wrapper(self._client)(
            **kwargs
        )

class EmbeddingsModule:
    def __init__(self, client):
      self._client = client

    def create(self,
        **kwargs: Unpack[EmbeddingsInputDict]
    ): 
        return v1_embeddings_create_wrapper(self._client)(
            **kwargs
        )

class V1Module:
    def __init__(self, client):
      self._client = client

    def retrieve(self,
    ): 
        return v1_get_dataset_retrieve_wrapper(self._client)(
        )

class ModelsModule:
    def __init__(self, client):
      self._client = client

    def list(self,
    ): 
        return v1_models_list_wrapper(self._client)(
        )
    def retrieve(self,
        id: int,
    ): 
        return v1_models_retrieve_wrapper(self._client)(
            id,
        )

class FeedbacksModule:
    def __init__(self, client):
      self._client = client

    def create(self,
        **kwargs: Unpack[FeedbackCreateDict]
    ): 
        return v1_set_trace_feedback_create_wrapper(self._client)(
            **kwargs
        )

class TracesModule:
    def __init__(self, client):
      self._client = client

    def list(self,
        admin_filter: V1TracesListAdminFilter = UNSET,
        date_filter: V1TracesListDateFilter = UNSET,
        from_date: str = UNSET,
        project_id: int,
        search: str = UNSET,
        sort: str = UNSET,
        to_date: str = UNSET,
    ): 
        return v1_traces_list_wrapper(self._client)(
     
            admin_filter,
            date_filter,
            from_date,
            project_id,
            search,
            sort,
            to_date,
        )
    def retrieve(self,
        id: str,
    ): 
        return v1_traces_retrieve_wrapper(self._client)(
            id,
        )



class RepositoryModuleWrapper:
    document: RepositoryDocumentModule

    def __init__(self, client):
        self.document = RepositoryDocumentModule(client)


class ChatModuleWrapper:
    completions: ChatCompletionsModule

    def __init__(self, client):
        self.completions = ChatCompletionsModule(client)
