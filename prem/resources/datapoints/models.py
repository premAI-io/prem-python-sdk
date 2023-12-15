from typing import Optional

from pydantic import BaseModel


class DataPoint(BaseModel):
    id: int
    created_at: str
    updated_at: str
    input: Optional[str] = None
    output: Optional[str] = None
    positive: bool
    trace: Optional[str] = None


class PatchedDataPoint(BaseModel):
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    input: Optional[str] = None
    output: Optional[str] = None
    positive: Optional[bool] = None
    trace: Optional[str] = None
