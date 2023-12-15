from __future__ import annotations

import requests

from . import resources
from .exceptions import error_to_exception


class PremAI:
    """
    PremAI class for making API requests.

    Attributes:
    - api_key (str): The API key for authentication.
    - base_url (str): The base URL of the API.
    - timeout (Optional[float]): The timeout for API requests in seconds (default: 30).
    - max_retries (Optional[int]): The maximum number of retries for failed requests (default: 3).
    """

    completions: resources.Completions

    def __init__(self, api_key: str, base_url: str) -> None:
        """
        Initialize PremAI with the provided API key, base URL, timeout, and max retries.

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

    def get(self, endpoint: str, **kwargs):
        """
        Make a GET request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - **kwargs: Additional keyword arguments to pass to the requests library.

        Returns:
        - Response: The response object.
        """
        return requests.get(
            f"{self.base_url}/{endpoint}", headers=self.headers, **kwargs
        )

    def post(self, endpoint: str, **kwargs):
        """
        Make a POST request to the API.

        Parameters:
        - endpoint (str): The API endpoint.
        - **kwargs: Additional keyword arguments to pass to the requests library.

        Returns:
        - Response: The response object.
        """
        body = kwargs.get("body", None)
        response = requests.post(
            f"{self.base_url}/{endpoint}", json=body, headers=self.headers
        )
        if response.status_code != 200:
            error_to_exception(response)
        return response.json()
