from typing import Optional

from pydantic import BaseModel


class InputDataPoint(BaseModel):
    """
    Represents an input data point with information about input, output, positivity,
    associated project, and an optional trace.

    Attributes:

    - input (Optional[str]): The input information for the data point.
    - output (Optional[str]): The output information for the data point.
    - positive (bool): A boolean indicating whether the data point is positive or not.
    - project (int): The ID of the project associated with the data point.
    - trace (Optional[str]): Additional trace information for the data point.
    """

    input: str = None
    output: str = None
    positive: bool
    project: int
    trace: Optional[str] = None


class DataPoint(BaseModel):
    """
    Represents a data point with input and output information.

    Attributes:

    - id (int): The unique identifier of the data point.
    - created_at (Optional[str]): The timestamp when the data point was created.
    - updated_at (Optional[str]): The timestamp when the data point was last updated.
    - input (Optional[str]): The input information for the data point.
    - output (Optional[str]): The output information for the data point.
    - positive (bool): A boolean indicating whether the data point is positive or not.
    - project (Optional[int]): The ID of the project.
    - trace (Optional[str]): Additional trace information for the data point.
    """

    id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    input: str = None
    output: str = None
    positive: bool
    project: Optional[int] = None
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
