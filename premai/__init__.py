from .client import AuthenticatedClient

from .api import (
    PlaygroundsModule,
    DatapointsModule,
    TracesModule,
    ProvidersModule,
    ApiModule,
    EmbeddingsModule,
    FinetuningModule,
    AuthModuleWrapper,
    ChatModuleWrapper,
)

class Prem:
    playgrounds: PlaygroundsModule
    datapoints: DatapointsModule
    traces: TracesModule
    providers: ProvidersModule
    api: ApiModule
    embeddings: EmbeddingsModule
    finetuning: FinetuningModule
    auth: AuthModuleWrapper
    chat: ChatModuleWrapper

    def __init__(self, api_key: str, base_url='https://app.premai.io'):
        client = AuthenticatedClient(token=api_key, base_url=base_url)
        # Init modules
        self.playgrounds = PlaygroundsModule(client)
        self.datapoints = DatapointsModule(client)
        self.traces = TracesModule(client)
        self.providers = ProvidersModule(client)
        self.api = ApiModule(client)
        self.embeddings = EmbeddingsModule(client)
        self.finetuning = FinetuningModule(client)
        self.auth = AuthModuleWrapper(client)
        self.chat = ChatModuleWrapper(client)

__all__ = [
    "Prem"
]