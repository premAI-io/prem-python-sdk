from functools import wraps
from typing import Any, Dict

from .exceptions import PremError


def required_args(mandatory_params):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            missing_params = [
                param for param in mandatory_params if param not in kwargs
            ]
            if missing_params:
                raise PremError(
                    f"Missing mandatory parameters: {', '.join(missing_params)}"
                )
            return func(*args, **kwargs)

        return wrapper

    return decorator


def filter_none_values(body: Dict[str, Any]) -> Dict[str, Any]:
    """
    Filters out key-value pairs with None values from a dictionary.

    This function is useful for creating a proper request body by removing
    fields with None values, ensuring that only relevant and non-null data
    is included.

    Parameters:
    - body (dict): The input dictionary to filter.

    Returns:
    dict: A new dictionary containing only the key-value pairs where the
          values are not None.
    """
    return {key: value for key, value in body.items() if value is not None}
