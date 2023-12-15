from __future__ import annotations


class SyncAPIResource:
    _client = None

    def __init__(self, client) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._delete = client.delete
