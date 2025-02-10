from enum import Enum


class V1TracesListDateFilter(str, Enum):
    LAST_DAY = "last_day"
    LAST_HOUR = "last_hour"
    LAST_MONTH = "last_month"
    LAST_WEEK = "last_week"
    LAST_YEAR = "last_year"

    def __str__(self) -> str:
        return str(self.value)
