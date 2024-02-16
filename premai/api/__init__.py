""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    V1ChatCompletionsCreateJsonBodyDict,
    V1DataPointsCreateJsonBodyDict,
    V1DataPointsPartialUpdateJsonBodyDict,
    V1DataPointsUpdateJsonBodyDict,
    V1EmbeddingsCreateJsonBodyDict,
    V1FinetuningCreateJsonBodyDict,
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


class ChatCompletionsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[V1ChatCompletionsCreateJsonBodyDict]):
        return v1_chat_completions_create_wrapper(self._client)(**kwargs)


class DatapointsModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
    ):
        return v1_data_points_list_wrapper(self._client)()

    def create(self, **kwargs: Unpack[V1DataPointsCreateJsonBodyDict]):
        return v1_data_points_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        id: int,
    ):
        return v1_data_points_retrieve_wrapper(self._client)(
            id,
        )

    def update(self, id: int, **kwargs: Unpack[V1DataPointsUpdateJsonBodyDict]):
        return v1_data_points_update_wrapper(self._client)(id, **kwargs)

    def delete(
        self,
        id: int,
    ):
        return v1_data_points_destroy_wrapper(self._client)(
            id,
        )

    def patch(self, id: int, **kwargs: Unpack[V1DataPointsPartialUpdateJsonBodyDict]):
        return v1_data_points_partial_update_wrapper(self._client)(id, **kwargs)


class EmbeddingsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[V1EmbeddingsCreateJsonBodyDict]):
        return v1_embeddings_create_wrapper(self._client)(**kwargs)


class FinetuningModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[V1FinetuningCreateJsonBodyDict]):
        return v1_finetuning_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        job_id: str,
    ):
        return v1_finetuning_retrieve_wrapper(self._client)(
            job_id,
        )


class ChatModuleWrapper:
    completions: ChatCompletionsModule

    def __init__(self, client):
        self.completions = ChatCompletionsModule(client)
