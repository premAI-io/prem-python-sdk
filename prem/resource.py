from __future__ import annotations


class SyncAPIResource:
    _client = None

    def __init__(self, client) -> None:
        self._client = client
        self._get = client._get
        self._post = client._post
        self._put = client._put
        self._patch = client._patch
        self._delete = client._delete
