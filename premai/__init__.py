from .client import AuthenticatedClient

from .api import (
    RepositoriesModule,
    EmbeddingsModule,
    ModelsModule,
    FeedbacksModule,
    TracesModule,
    RepositoryModuleWrapper,
    ChatModuleWrapper,
)

class Prem:
    repositories: RepositoriesModule
    embeddings: EmbeddingsModule
    models: ModelsModule
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
        self.feedbacks = FeedbacksModule(client)
        self.traces = TracesModule(client)
        self.repository = RepositoryModuleWrapper(client)
        self.chat = ChatModuleWrapper(client)

__all__ = [
    "Prem"
]