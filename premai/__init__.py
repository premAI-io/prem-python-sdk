from .client import AuthenticatedClient

from .api import (
    RepositoriesModule,
    EmbeddingsModule,
    ModelsModule,
    V1Module,
    FeedbacksModule,
    TracesModule,
    RepositoryModuleWrapper,
    ChatModuleWrapper,
)

class Prem:
    repositories: RepositoriesModule
    embeddings: EmbeddingsModule
    models: ModelsModule
    v1: V1Module
    feedbacks: FeedbacksModule
    traces: TracesModule
    repository: RepositoryModuleWrapper
    chat: ChatModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.repositories = RepositoriesModule(client)
        self.embeddings = EmbeddingsModule(client)
        self.models = ModelsModule(client)
        self.v1 = V1Module(client)
        self.feedbacks = FeedbacksModule(client)
        self.traces = TracesModule(client)
        self.repository = RepositoryModuleWrapper(client)
        self.chat = ChatModuleWrapper(client)

__all__ = [
    "Prem"
]