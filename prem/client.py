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
    """

    completions: resources.Completions
    embeddings: resources.Embeddings
    datapoints: resources.DataPoints

    def __init__(
        self, api_key: str, base_url: str = "https://app.prod.prem.ninja"
    ) -> None:
        """
        Initialize Prem with the provided API key and base URL.

        :param api_key: The API key for authentication.
        :type api_key: str
        :param base_url: The base URL of the API.
        :type base_url: str
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = (
            {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        )

        self.completions = resources.Completions(self)
        self.embeddings = resources.Embeddings(self)
        self.datapoints = resources.DataPoints(self)

    def _get(self, endpoint: str, status_code: int = 200) -> Dict:
        """
        Make a GET request to the API.

        :param endpoint: The API endpoint.
        :type endpoint: str
        :param status_code: The expected status code of the response.
        :type status_code: int

        :return: The response object.
        :rtype: Dict
        """
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def _post(
        self, endpoint: str, body: Dict, stream: bool = False, status_code: int = 200
    ) -> Union[Dict, List[Dict]]:
        """
        Make a POST request to the API.

        :param endpoint: The API endpoint.
        :type endpoint: str
        :param body: The JSON body of the request.
        :type body: Dict
        :param stream: If True, stream the response; otherwise, return the response as JSON.
        :type stream: bool
        :param status_code: The expected status code of the response.
        :type status_code: int

        :return: The response object.
        :rtype: Union[Dict, List[Dict]]
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

    def _put(self, endpoint: str, body: Dict, status_code: int = 201) -> Dict:
        """
        Make a PUT request to the API.

        :param endpoint: The API endpoint.
        :type endpoint: str
        :param body: The JSON body of the request.
        :type body: Dict
        :param status_code: The expected status code of the response.
        :type status_code: int

        :return: The response object.
        :rtype: Dict
        """
        response = requests.put(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def _patch(self, endpoint: str, body: Dict, status_code: int = 200) -> Dict:
        """
        Make a PATCH request to the API.

        :param endpoint: The API endpoint.
        :type endpoint: str
        :param body: The JSON body of the request.
        :type body: Dict
        :param status_code: The expected status code of the response.
        :type status_code: int

        :return: The response object.
        :rtype: Dict
        """
        response = requests.patch(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != status_code:
            error_to_exception(response)
        return response.json()

    def _delete(self, endpoint: str, status_code: int = 204) -> None:
        """
        Make a DELETE request to the API.

        :param endpoint: The API endpoint.
        :type endpoint: str
        :param status_code: The expected status code of the response.
        :type status_code: int
        """
        response = requests.delete(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code != status_code:
            error_to_exception(response)
