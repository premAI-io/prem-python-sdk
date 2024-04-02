from .client import AuthenticatedClient

from .api import (
    ApiModule,
    DatapointsModule,
    EmbeddingsModule,
    FinetuningModule,
    ModelsModule,
    ChatModuleWrapper,
    RepositoryModuleWrapper,
)

class Prem:
    api: ApiModule
    datapoints: DatapointsModule
    embeddings: EmbeddingsModule
    finetuning: FinetuningModule
    models: ModelsModule
    chat: ChatModuleWrapper
    repository: RepositoryModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.api = ApiModule(client)
        self.datapoints = DatapointsModule(client)
        self.embeddings = EmbeddingsModule(client)
        self.finetuning = FinetuningModule(client)
        self.models = ModelsModule(client)
        self.chat = ChatModuleWrapper(client)
        self.repository = RepositoryModuleWrapper(client)

__all__ = [
    "Prem"
]