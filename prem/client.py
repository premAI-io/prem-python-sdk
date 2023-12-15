from __future__ import annotations

import json
from typing import Dict, List, Union

import requests
from sseclient import SSEClient

from . import resources
from .exceptions import error_to_exception


class PremAI:
    """
    PremAI class for making API requests.

    Attributes:
    - api_key (str): The API key for authentication.
    - base_url (str): The base URL of the API.
    """

    completions: resources.Completions
    embeddings: resources.Embeddings

    def __init__(self, api_key: str, base_url: str) -> None:
        """
        Initialize PremAI with the provided API key and base URL.

        Parameters:
        - api_key (str): The API key for authentication.
        - base_url (str): The base URL of the API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = (
            {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        )

        self.completions = resources.Completions(self)
        self.embeddings = resources.Embeddings(self)

    def get(self, endpoint: str) -> Union[Dict, List[Dict]]:
        """
        Make a GET request to the API.

        Parameters:
        - endpoint (str): The API endpoint.

        Returns:
        - Union[Dict, List[Dict]]: The response object.
        """
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code != 200:
            error_to_exception(response)
        return response.json()

    def post(
        self, endpoint: str, body: Dict, stream: bool = False
    ) -> Union[Dict, List[Dict]]:
        """
        Make a POST request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - body (Dict): The JSON body of the request.
        - stream (bool): If True, stream the response; otherwise, return the response as JSON.

        Returns:
        - Union[Dict, List[Dict]]: The response object.
        """
        response = requests.post(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != 200:
            error_to_exception(response)
        if not stream:
            return response.json()
        else:
            client = SSEClient(response)
            events = []
            for event in client.events():
                if event.data != "[DONE]":
                    events.append(json.loads(event.data))
            return events
