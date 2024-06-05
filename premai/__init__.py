from .client import AuthenticatedClient

from .api import (
    EmbeddingsModule,
    ModelsModule,
    RepositoriesModule,
    FeedbacksModule,
    TracesModule,
    ChatModuleWrapper,
    RepositoryModuleWrapper,
)

class Prem:
    embeddings: EmbeddingsModule
    models: ModelsModule
    repositories: RepositoriesModule
    feedbacks: FeedbacksModule
    traces: TracesModule
    chat: ChatModuleWrapper
    repository: RepositoryModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.embeddings = EmbeddingsModule(client)
        self.models = ModelsModule(client)
        self.repositories = RepositoriesModule(client)
        self.feedbacks = FeedbacksModule(client)
        self.traces = TracesModule(client)
        self.chat = ChatModuleWrapper(client)
        self.repository = RepositoryModuleWrapper(client)

__all__ = [
    "Prem"
]