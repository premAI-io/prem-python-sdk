""" Contains methods for accessing the API """


from typing_extensions import Unpack

from ..models import (
    ChatCompletionInputDict,
    DataPointDict,
    DataSetCreateGymAdminDict,
    DocumentInputDict,
    EmbeddingsInputDict,
    FineTunedModelPromotionDict,
    FineTuningInputDict,
    FineTuningJobCreateGymAdminDict,
    FineTuningMessageCreateGymAdminDict,
    FineTuningRequestChangeStateGymAdminDict,
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
from .finetuning_admin.projects_gym_admin_datasets_create import projects_gym_admin_datasets_create_wrapper
from .finetuning_admin.projects_gym_admin_datasets_list import projects_gym_admin_datasets_list_wrapper
from .finetuning_admin.projects_gym_admin_datasets_retrieve import projects_gym_admin_datasets_retrieve_wrapper
from .finetuning_admin.projects_gym_admin_finetunedmodels_list import projects_gym_admin_finetunedmodels_list_wrapper
from .finetuning_admin.projects_gym_admin_finetunedmodels_promote_create import (
    projects_gym_admin_finetunedmodels_promote_create_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetunedmodels_retrieve import (
    projects_gym_admin_finetunedmodels_retrieve_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningjobs_create import projects_gym_admin_finetuningjobs_create_wrapper
from .finetuning_admin.projects_gym_admin_finetuningjobs_list import projects_gym_admin_finetuningjobs_list_wrapper
from .finetuning_admin.projects_gym_admin_finetuningjobs_retrieve import (
    projects_gym_admin_finetuningjobs_retrieve_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningmessages_create import (
    projects_gym_admin_finetuningmessages_create_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningmessages_list import (
    projects_gym_admin_finetuningmessages_list_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningrequests_list import (
    projects_gym_admin_finetuningrequests_list_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningrequests_retrieve import (
    projects_gym_admin_finetuningrequests_retrieve_wrapper,
)
from .finetuning_admin.projects_gym_admin_finetuningrequests_set_started_create import (
    projects_gym_admin_finetuningrequests_set_started_create_wrapper,
)
from .models.v1_models_list import v1_models_list_wrapper
from .models.v1_models_retrieve import v1_models_retrieve_wrapper
from .repository_document.v1_repository_document_create import v1_repository_document_create_wrapper


class FinetuningAdminModule:
    def __init__(self, client):
        self._client = client

    def list(
        self,
        project_id: str,
    ):
        return projects_gym_admin_datasets_list_wrapper(self._client)(
            project_id,
        )

    def create(self, **kwargs: Unpack[DataSetCreateGymAdminDict]):
        return projects_gym_admin_datasets_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        id: int,
    ):
        return projects_gym_admin_datasets_retrieve_wrapper(self._client)(
            id,
        )

    def list(
        self,
        fine_tuning_request_id: str,
    ):
        return projects_gym_admin_finetunedmodels_list_wrapper(self._client)(
            fine_tuning_request_id,
        )

    def retrieve(
        self,
        id: int,
    ):
        return projects_gym_admin_finetunedmodels_retrieve_wrapper(self._client)(
            id,
        )

    def create(self, **kwargs: Unpack[FineTunedModelPromotionDict]):
        return projects_gym_admin_finetunedmodels_promote_create_wrapper(self._client)(**kwargs)

    def list(
        self,
        fine_tuning_request_id: str,
    ):
        return projects_gym_admin_finetuningjobs_list_wrapper(self._client)(
            fine_tuning_request_id,
        )

    def create(self, **kwargs: Unpack[FineTuningJobCreateGymAdminDict]):
        return projects_gym_admin_finetuningjobs_create_wrapper(self._client)(**kwargs)

    def retrieve(
        self,
        id: int,
    ):
        return projects_gym_admin_finetuningjobs_retrieve_wrapper(self._client)(
            id,
        )

    def list(
        self,
        fine_tuning_request_id: str,
    ):
        return projects_gym_admin_finetuningmessages_list_wrapper(self._client)(
            fine_tuning_request_id,
        )

    def create(self, **kwargs: Unpack[FineTuningMessageCreateGymAdminDict]):
        return projects_gym_admin_finetuningmessages_create_wrapper(self._client)(**kwargs)

    def list(
        self,
        project_id: str,
    ):
        return projects_gym_admin_finetuningrequests_list_wrapper(self._client)(
            project_id,
        )

    def retrieve(
        self,
        id: int,
    ):
        return projects_gym_admin_finetuningrequests_retrieve_wrapper(self._client)(
            id,
        )

    def create(
        self, **kwargs: Unpack[FineTuningRequestChangeStateGymAdminDict]
    ):
        return projects_gym_admin_finetuningrequests_set_started_create_wrapper(self._client)(**kwargs)


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

    def update(self, id: int, **kwargs: Unpack[DataPointDict]):
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
