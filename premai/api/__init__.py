""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    ChatCompletionInputDict,
    DeleteFinetuningJobRequestDict,
    DocumentInputDict,
    DownloadFinetunedModelRequestDict,
    EmbeddingsInputDict,
    FeedbackCreateDict,
    FineTunedModelTryRequestDict,
    FineTuningJobCreateDict,
    FineTuningJobDetailsRequestDict,
    InitPageDataRequestDict,
    RepositoryDict,
)
from ..models.v1_traces_list_admin_filter import V1TracesListAdminFilter
from ..models.v1_traces_list_date_filter import V1TracesListDateFilter
from ..types import UNSET
from .chat_completions.v1_chat_completions_create import v1_chat_completions_create_wrapper
from .embeddings.v1_embeddings_create import v1_embeddings_create_wrapper
from .feedbacks.v1_set_trace_feedback_create import v1_set_trace_feedback_create_wrapper
from .finetuning.v1_create_finetuning_job_create import v1_create_finetuning_job_create_wrapper
from .finetuning.v1_delete_finetuning_job_create import v1_delete_finetuning_job_create_wrapper
from .finetuning.v1_download_finetuned_model_create import v1_download_finetuned_model_create_wrapper
from .finetuning.v1_finetuned_model_try_create import v1_finetuned_model_try_create_wrapper
from .finetuning.v1_finetuning_job_details_create import v1_finetuning_job_details_create_wrapper
from .finetuning.v1_init_page_data_create import v1_init_page_data_create_wrapper
from .models.v1_models_list import v1_models_list_wrapper
from .models.v1_models_retrieve import v1_models_retrieve_wrapper
from .repositories.api_repositories_repositories_create import api_repositories_repositories_create_wrapper
from .repository_document.api_repositories_repository_document_create import (
    api_repositories_repository_document_create_wrapper,
)
from .traces.v1_traces_list import v1_traces_list_wrapper
from .traces.v1_traces_retrieve import v1_traces_retrieve_wrapper
from .v1.v1_get_dataset_retrieve import v1_get_dataset_retrieve_wrapper


class RepositoriesModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[RepositoryDict]):
        return api_repositories_repositories_create_wrapper(self._client)(**kwargs)


class RepositoryDocumentModule:
    def __init__(self, client):
        self._client = client

    def create(self, repository_id: int, **kwargs: Unpack[DocumentInputDict]):
        return api_repositories_repository_document_create_wrapper(self._client)(repository_id, **kwargs)


class ChatCompletionsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[ChatCompletionInputDict]):
        return v1_chat_completions_create_wrapper(self._client)(**kwargs)


class FinetuningModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[FineTuningJobCreateDict]):
        return v1_create_finetuning_job_create_wrapper(self._client)(**kwargs)

    def create(self, **kwargs: Unpack[DeleteFinetuningJobRequestDict]):
        return v1_delete_finetuning_job_create_wrapper(self._client)(**kwargs)

    def create(self, **kwargs: Unpack[DownloadFinetunedModelRequestDict]):
        return v1_download_finetuned_model_create_wrapper(self._client)(**kwargs)

    def create(self, **kwargs: Unpack[FineTunedModelTryRequestDict]):
        return v1_finetuned_model_try_create_wrapper(self._client)(**kwargs)

    def create(self, **kwargs: Unpack[FineTuningJobDetailsRequestDict]):
        return v1_finetuning_job_details_create_wrapper(self._client)(**kwargs)

    def v1_init_page_data_create(self, **kwargs: Unpack[InitPageDataRequestDict]):
        return v1_init_page_data_create_wrapper(self._client)(**kwargs)


class EmbeddingsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[EmbeddingsInputDict]):
        return v1_embeddings_create_wrapper(self._client)(**kwargs)


class V1Module:
    def __init__(self, client):
        self._client = client

    def retrieve(
        self,
    ):
        return v1_get_dataset_retrieve_wrapper(self._client)()


class ModelsModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
    ):
        return v1_models_list_wrapper(self._client)()

    def retrieve(
        self,
        id: int,
    ):
        return v1_models_retrieve_wrapper(self._client)(
            id,
        )


class FeedbacksModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[FeedbackCreateDict]):
        return v1_set_trace_feedback_create_wrapper(self._client)(**kwargs)


class TracesModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
        project_id: int,
        admin_filter: V1TracesListAdminFilter = UNSET,
        date_filter: V1TracesListDateFilter = UNSET,
        from_date: str = UNSET,
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

    def retrieve(
        self,
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
