from .client import AuthenticatedClient

from .api import (
    RepositoriesModule,
    FinetuningModule,
    EmbeddingsModule,
    V1Module,
    ModelsModule,
    FeedbacksModule,
    TracesModule,
    RepositoryModuleWrapper,
    ChatModuleWrapper,
)

class Prem:
    repositories: RepositoriesModule
    finetuning: FinetuningModule
    embeddings: EmbeddingsModule
    v1: V1Module
    models: ModelsModule
    feedbacks: FeedbacksModule
    traces: TracesModule
    repository: RepositoryModuleWrapper
    chat: ChatModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.repositories = RepositoriesModule(client)
        self.finetuning = FinetuningModule(client)
        self.embeddings = EmbeddingsModule(client)
        self.v1 = V1Module(client)
        self.models = ModelsModule(client)
        self.feedbacks = FeedbacksModule(client)
        self.traces = TracesModule(client)
        self.repository = RepositoryModuleWrapper(client)
        self.chat = ChatModuleWrapper(client)

__all__ = [
    "Prem"
]