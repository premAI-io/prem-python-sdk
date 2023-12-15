from __future__ import annotations

from typing import List, Optional, Union

from ...resource import SyncAPIResource
from ...utils import filter_none_values, required_args
from .models import EmbeddingsResponse


class Embeddings(SyncAPIResource):
    """
    Embeddings class for making API requests related to embeddings.

    Attributes:
    - client (PremAI): The client for making API requests.
    """

    def __init__(self, client) -> None:
        """
        Initializes the Embeddings resource.

        Parameters:
        - client (PremAI): The client for making API requests.
        """
        super().__init__(client)

    @required_args(["project_id", "input"])
    def create(
        self,
        project_id: int,
        input: Union[str, List[str], List[int], List[List[int]]],
        model: Optional[str] = None,
        encoding_format: Optional[str] = "float",
    ) -> EmbeddingsResponse:
        body = {
            "project_id": project_id,
            "input": input,
            "model": model,
            "encoding_format": encoding_format,
        }

        response = self._post(
            "v1/chat/embeddings", body=filter_none_values(body), stream=False
        )
        return EmbeddingsResponse(**response)
