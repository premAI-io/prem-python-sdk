""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    ChatCompletionInputDict,
    DocumentInputDict,
    EmbeddingsInputDict,
    FineTuningInputDict,
    InputDataPointDict,
    PatchedDataPointDict,
)
from .chat_completions.v1_chat_completions_create import v1_chat_completions_create_wrapper
from .datapoints.v1_data_points_create import v1_data_points_create_wrapper
from .datapoints.v1_data_points_destroy import v1_data_points_destroy_wrapper
from .datapoints.v1_data_points_list import v1_data_points_list_wrapper
from .datapoints.v1_data_points_partial_update import v1_data_points_partial_update_wrapper
from .datapoints.v1_data_points_retrieve import v1_data_points_retrieve_wrapper
from .datapoints.v1_data_points_update import v1_data_points_update_wrapper
from .embeddings.v1_embeddings_create import v1_embeddings_create_wrapper
from .finetuning.v1_finetuning_create import v1_finetuning_create_wrapper
from .finetuning.v1_finetuning_retrieve import v1_finetuning_retrieve_wrapper
from .models.v1_models_list import v1_models_list_wrapper
from .models.v1_models_retrieve import v1_models_retrieve_wrapper
from .repository_document.v1_repository_document_create import v1_repository_document_create_wrapper


class ChatCompletionsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[ChatCompletionInputDict]):
        return v1_chat_completions_create_wrapper(self._client)(**kwargs)


class DatapointsModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
    ):
        return v1_data_points_list_wrapper(self._client)()

    def create(self, **kwargs: Unpack[InputDataPointDict]):
        return v1_data_points_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        id: int,
    ):
        return v1_data_points_retrieve_wrapper(self._client)(
            id,
        )

    def update(self, id: int, **kwargs: Unpack[InputDataPointDict]):
        return v1_data_points_update_wrapper(self._client)(id, **kwargs)

    def delete(
        self,
        id: int,
    ):
        return v1_data_points_destroy_wrapper(self._client)(
            id,
        )

    def patch(self, id: int, **kwargs: Unpack[PatchedDataPointDict]):
        return v1_data_points_partial_update_wrapper(self._client)(id, **kwargs)


class EmbeddingsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[EmbeddingsInputDict]):
        return v1_embeddings_create_wrapper(self._client)(**kwargs)


class FinetuningModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[FineTuningInputDict]):
        return v1_finetuning_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        job_id: str,
    ):
        return v1_finetuning_retrieve_wrapper(self._client)(
            job_id,
        )


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


class RepositoryDocumentModule:
    def __init__(self, client):
        self._client = client

    def create(self, repository_id: int, **kwargs: Unpack[DocumentInputDict]):
        return v1_repository_document_create_wrapper(self._client)(repository_id, **kwargs)


class ChatModuleWrapper:
    completions: ChatCompletionsModule

    def __init__(self, client):
        self.completions = ChatCompletionsModule(client)


class RepositoryModuleWrapper:
    document: RepositoryDocumentModule

    def __init__(self, client):
        self.document = RepositoryDocumentModule(client)
