""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    ApiProjectsDataPointsCreateJsonBodyDict,
    ApiProjectsDataPointsPartialUpdateJsonBodyDict,
    ApiProjectsDataPointsUpdateJsonBodyDict,
    ApiProjectsTracesCreateJsonBodyDict,
    AuthTokenCreateDataBodyDict,
    V1ChatCompletionsCreateJsonBodyDict,
    V1EmbeddingsCreateJsonBodyDict,
    V1FinetuningCreateJsonBodyDict,
)
from ..models.api_schema_retrieve_format import ApiSchemaRetrieveFormat
from ..models.api_schema_retrieve_lang import ApiSchemaRetrieveLang
from .api.api_schema_retrieve import api_schema_retrieve_wrapper
from .auth_token.auth_token_create import auth_token_create_wrapper
from .chat_completions.v1_chat_completions_create import v1_chat_completions_create_wrapper
from .datapoints.api_projects_data_points_create import api_projects_data_points_create_wrapper
from .datapoints.api_projects_data_points_destroy import api_projects_data_points_destroy_wrapper
from .datapoints.api_projects_data_points_list import api_projects_data_points_list_wrapper
from .datapoints.api_projects_data_points_partial_update import api_projects_data_points_partial_update_wrapper
from .datapoints.api_projects_data_points_retrieve import api_projects_data_points_retrieve_wrapper
from .datapoints.api_projects_data_points_update import api_projects_data_points_update_wrapper
from .embeddings.v1_embeddings_create import v1_embeddings_create_wrapper
from .finetuning.v1_finetuning_create import v1_finetuning_create_wrapper
from .finetuning.v1_finetuning_retrieve import v1_finetuning_retrieve_wrapper
from .playgrounds.api_playgrounds_image_retrieve import api_playgrounds_image_retrieve_wrapper
from .playgrounds.api_playgrounds_ot_info_retrieve import api_playgrounds_ot_info_retrieve_wrapper
from .providers.api_providers_leaderboard_retrieve import api_providers_leaderboard_retrieve_wrapper
from .providers.api_providers_retrieve import api_providers_retrieve_wrapper
from .traces.api_projects_traces_create import api_projects_traces_create_wrapper


class PlaygroundsModule:
    def __init__(self, client):
        self._client = client

    def retrieve_image(
        self,
        sharable_playground_uuid: str,
    ):
        return api_playgrounds_image_retrieve_wrapper(self._client)(
            sharable_playground_uuid,
        )

    def retrieve_ot_info(
        self,
        sharable_playground_uuid: str,
    ):
        return api_playgrounds_ot_info_retrieve_wrapper(self._client)(
            sharable_playground_uuid,
        )


class DatapointsModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
    ):
        return api_projects_data_points_list_wrapper(self._client)()

    def create(self, **kwargs: Unpack[ApiProjectsDataPointsCreateJsonBodyDict]):
        return api_projects_data_points_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        id: int,
    ):
        return api_projects_data_points_retrieve_wrapper(self._client)(
            id,
        )

    def update(self, id: int, **kwargs: Unpack[ApiProjectsDataPointsUpdateJsonBodyDict]):
        return api_projects_data_points_update_wrapper(self._client)(id, **kwargs)

    def delete(
        self,
        id: int,
    ):
        return api_projects_data_points_destroy_wrapper(self._client)(
            id,
        )

    def patch(
        self, id: int, **kwargs: Unpack[ApiProjectsDataPointsPartialUpdateJsonBodyDict]
    ):
        return api_projects_data_points_partial_update_wrapper(self._client)(id, **kwargs)


class TracesModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[ApiProjectsTracesCreateJsonBodyDict]):
        return api_projects_traces_create_wrapper(self._client)(**kwargs)


class ProvidersModule:
    def __init__(self, client):
        self._client = client

    def retrieve_providers(
        self,
        days: int = None,
    ):
        return api_providers_retrieve_wrapper(self._client)(
            days,
        )

    def retrieve_leaderboard(
        self,
        days: int = None,
    ):
        return api_providers_leaderboard_retrieve_wrapper(self._client)(
            days,
        )


class ApiModule:
    def __init__(self, client):
        self._client = client

    def retrieve(
        self,
        format: ApiSchemaRetrieveFormat = None,
        lang: ApiSchemaRetrieveLang = None,
    ):
        return api_schema_retrieve_wrapper(self._client)(
            format,
            lang,
        )


class AuthTokenModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[AuthTokenCreateDataBodyDict]):
        return auth_token_create_wrapper(self._client)(**kwargs)


class ChatCompletionsModule:
    def __init__(self, client):
        self._client = client

    def create(self, **kwargs: Unpack[V1ChatCompletionsCreateJsonBodyDict]):
        return v1_chat_completions_create_wrapper(self._client)(**kwargs)


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


class AuthModuleWrapper:
    token: AuthTokenModule

    def __init__(self, client):
        self.token = AuthTokenModule(client)


class ChatModuleWrapper:
    completions: ChatCompletionsModule

    def __init__(self, client):
        self.completions = ChatCompletionsModule(client)
