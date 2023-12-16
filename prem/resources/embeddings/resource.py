from __future__ import annotations

from typing import List, Optional, Union

from ...resource import SyncAPIResource
from ...utils import filter_none_values, required_args
from .models import EmbeddingsResponse


class Embeddings(SyncAPIResource):
    """
    Embeddings class for making API requests related to embeddings.

    Attributes:

    - client (Prem): The client for making API requests.
    """

    def __init__(self, client) -> None:
        """
        Initializes the Embeddings resource.

        Parameters:

        - client (Prem): The client for making API requests.
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
        """
        Create embeddings based on the provided parameters.

        Parameters:

        - project_id (int): The ID of the project.
        - input (Union[str, List[str], List[int], List[List[int]]]): The input data for which embeddings are requested.
        - model (Optional[str]): The language model to use for generating embeddings.
        - encoding_format (Optional[str]): The encoding format for the embeddings (default is "float").

        Returns:

        - EmbeddingsResponse: The response containing the generated embeddings.
        """
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
