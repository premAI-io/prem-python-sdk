from __future__ import annotations

import json
from typing import Dict, List, Union

import requests
from sseclient import SSEClient

from . import resources
from .exceptions import error_to_exception


class Prem:
    """
    Prem class for making API requests.

    Attributes:
    - api_key (str): The API key for authentication.
    - base_url (str): The base URL of the API.
    """

    completions: resources.Completions
    embeddings: resources.Embeddings

    def __init__(self, api_key: str, base_url: str) -> None:
        """
        Initialize Prem with the provided API key and base URL.

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
        self.datapoints = resources.DataPoints(self)

    def get(self, endpoint: str, status_code: int = 200) -> Dict:
        """
        Make a GET request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - status_code (int): The expected status code of the response.

        Returns:
        - Dict: The response object.
        """
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def post(
        self, endpoint: str, body: Dict, stream: bool = False, status_code: int = 200
    ) -> Union[Dict, List[Dict]]:
        """
        Make a POST request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - body (Dict): The JSON body of the request.
        - stream (bool): If True, stream the response; otherwise, return the response as JSON.
        - status_code (int): The expected status code of the response.

        Returns:
        - Union[Dict, List[Dict]]: The response object.
        """
        response = requests.post(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != status_code:
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

    def put(self, endpoint: str, body: Dict, status_code: int = 201) -> Dict:
        """
        Make a PUT request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - body (Dict): The JSON body of the request.
        - status_code (int): The expected status code of the response.

        Returns:
        - Dict: The response object.
        """
        response = requests.put(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def patch(self, endpoint: str, body: Dict, status_code: int = 200) -> Dict:
        """
        Make a PATCH request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - body (Dict): The JSON body of the request.
        - status_code (int): The expected status code of the response.

        Returns:
        - Dict: The response object.
        """
        response = requests.patch(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def delete(self, endpoint: str, status_code: int = 204) -> None:
        """
        Make a DELETE request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - status_code (int): The expected status code of the response.
        """
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code != status_code:
            error_to_exception(response)
