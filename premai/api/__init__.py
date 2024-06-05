""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    ChatCompletionInputDict,
    DocumentInputDict,
    EmbeddingsInputDict,
    FeedbackCreateDict,
    RepositoryDict,
)
from .chat_completions.v1_chat_completions_create import v1_chat_completions_create_wrapper
from .embeddings.v1_embeddings_create import v1_embeddings_create_wrapper
from .feedbacks.v1_set_trace_feedback_create import v1_set_trace_feedback_create_wrapper
from .models.v1_models_list import v1_models_list_wrapper
from .models.v1_models_retrieve import v1_models_retrieve_wrapper
from .repositories.v1_repositories_create import v1_repositories_create_wrapper
from .repository_document.v1_repository_document_create import v1_repository_document_create_wrapper
from .traces.v1_traces_list import v1_traces_list_wrapper
from .traces.v1_traces_retrieve import v1_traces_retrieve_wrapper


class ChatCompletionsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[ChatCompletionInputDict]):
        return v1_chat_completions_create_wrapper(self._client)(**kwargs)


class EmbeddingsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[EmbeddingsInputDict]):
        return v1_embeddings_create_wrapper(self._client)(**kwargs)


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


class RepositoriesModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[RepositoryDict]):
        return v1_repositories_create_wrapper(self._client)(**kwargs)


class RepositoryDocumentModule:
    def __init__(self, client):
        self._client = client

    def create(self, repository_id: int, **kwargs: Unpack[DocumentInputDict]):
        return v1_repository_document_create_wrapper(self._client)(repository_id, **kwargs)


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
    ):
        return v1_traces_list_wrapper(self._client)(
            project_id,
        )

    def retrieve(
        self,
        id: str,
    ):
        return v1_traces_retrieve_wrapper(self._client)(
            id,
        )


class ChatModuleWrapper:
    completions: ChatCompletionsModule

    def __init__(self, client):
        self.completions = ChatCompletionsModule(client)


class RepositoryModuleWrapper:
    document: RepositoryDocumentModule

    def __init__(self, client):
        self.document = RepositoryDocumentModule(client)
