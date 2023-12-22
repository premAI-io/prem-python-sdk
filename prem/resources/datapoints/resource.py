from __future__ import annotations

from typing import Dict, List, Optional

from ...resource import SyncAPIResource
from ...utils import required_args
from .models import DataPoint, InputDataPoint, PatchedDataPoint


class DataPoints(SyncAPIResource):
    """
    DataPoints class for handling the datapoint endpoint.

    Attributes:
    - client (Prem): The client for making API requests.
    """

    def __init__(self, client) -> None:
        """
        Initializes the DataPoints.

        Parameters:
        - client (Prem): The client for making API requests.
        """
        super().__init__(client)

    @required_args(["project_id", "input", "positive", "input", "output"])
    def create(
        self,
        project_id: int,
        input: str,
        positive: bool,
        output: Optional[str] = None,
        trace: Optional[str] = None,
    ) -> DataPoint:
        """
        Create a new data point using the provided parameters.

        Parameters:
        - project_id (int): The ID of the project.
        - input (str): The input data.
        - positive (bool): Boolean indicating whether the data point is positive.
        - output (Optional[str]): The output data (nullable).
        - trace (Optional[str]): The trace identifier (nullable).

        Returns:
        - DataPoint: The created data point.
        """
        body = {
            "project": project_id,
            "input": input,
            "output": output,
            "positive": positive,
            "trace": trace,
        }
        InputDataPoint(**body)
        response = self._post("api/projects/data-points/", body=body, status_code=201)
        print("create", response)
        return DataPoint(**response)

    @required_args(["datapoint_id"])
    def retrieve(self, datapoint_id: int) -> DataPoint:
        """
        Retrieve a data point by its ID.

        Parameters:
        - datapoint_id (int): The ID of the data point to retrieve.

        Returns:
        - DataPoint: The retrieved data point.
        """
        response = self._get(f"api/projects/data-points/{datapoint_id}/")
        print("retrieve", response)
        return DataPoint(**response)

    def list(self) -> List[DataPoint]:
        """
        Retrieve a list of data points.

        Returns:
        - List[DataPoint]: A list of data points.
        """
        response = self._get("api/projects/data-points/")
        print("list", response)
        return [DataPoint(**data_point) for data_point in response]

    @required_args(["datapoint_id", "data"])
    def update(self, datapoint_id: int, data: Dict) -> DataPoint:
        """
        Update a data point by its ID.

        Parameters:
        - datapoint_id (int): The ID of the data point to update.
        - data (Dict): The data to update.

        Returns:
        - DataPoint: The updated data point.
        """
        _ = PatchedDataPoint(**data)
        response = self._patch(f"api/projects/data-points/{datapoint_id}/", body=data)
        print("update", response)
        return DataPoint(**response)

    @required_args(["datapoint_id"])
    def delete(self, datapoint_id: int) -> None:
        """
        Delete a data point by its ID.

        Parameters:
        - datapoint_id (int): The ID of the data point to delete.
        """
        self._delete(f"api/projects/data-points/{datapoint_id}/")
