from typing import Optional

from pydantic import BaseModel


class DataPoint(BaseModel):
    """
    Represents a data point with input and output information.

    Attributes:

    - id (int): The unique identifier of the data point.
    - created_at (str): The timestamp when the data point was created.
    - updated_at (str): The timestamp when the data point was last updated.
    - input (Optional[str]): The input information for the data point (optional).
    - output (Optional[str]): The output information for the data point (optional).
    - positive (bool): A boolean indicating whether the data point is positive or not.
    - trace (Optional[str]): Additional trace information for the data point (optional).
    """

    id: int
    created_at: str
    updated_at: str
    input: Optional[str] = None
    output: Optional[str] = None
    positive: bool
    trace: Optional[str] = None


class PatchedDataPoint(BaseModel):
    """
    Represents a patched data point with optional attributes for updating.

    Attributes:

    - id (Optional[int]): The unique identifier of the data point (optional).
    - created_at (Optional[str]): The timestamp when the data point was created (optional).
    - updated_at (Optional[str]): The timestamp when the data point was last updated (optional).
    - input (Optional[str]): The updated input information for the data point (optional).
    - output (Optional[str]): The updated output information for the data point (optional).
    - positive (Optional[bool]): The updated boolean indicating whether the data point is positive or not (optional).
    - trace (Optional[str]): The updated additional trace information for the data point (optional).
    """

    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None
    positive: Optional[bool] = None
    trace: Optional[str] = None
