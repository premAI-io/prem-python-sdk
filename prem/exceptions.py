from typing import Optional

from requests import Response


class PremError(Exception):
    pass


class PremProviderError(PremError):
    def __init__(
        self,
        message: str,
        provider: Optional[str],
        model: Optional[str],
        provider_message: Optional[str],
    ):
        super().__init__(message)
        self.provider = provider
        self.model = model
        self.provider_message = provider_message


class PremProviderNotFoundError(PremProviderError):
    pass


class PremProviderAPIError(PremProviderError):
    pass


class PremProviderAuthenticationError(PremProviderError):
    pass


class PremProviderConflictError(PremProviderError):
    pass


class PremProviderAPIStatusError(PremProviderError):
    pass


class PremProviderAPITimeoutError(PremProviderError):
    pass


class PremProviderRateLimitError(PremProviderError):
    pass


class PremProviderBadRequestError(PremProviderError):
    pass


class PremProviderAPIConnectionError(PremProviderError):
    pass


class PremProviderInternalServerError(PremProviderError):
    pass


class PremProviderPermissionDeniedError(PremProviderError):
    pass


class PremProviderUnprocessableEntityError(PremProviderError):
    pass


class PremProviderAPIResponseValidationError(PremProviderError):
    pass


class PremProviderResponseValidationError(PremProviderError):
    pass


class ModelNotFoundError(PremError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ValidationError(PremError):
    def __init__(self, message, details):
        self.message = message
        self.details = details
        super().__init__(self.message)


def error_to_exception(error: Response) -> PremError:
    """
    Map an API response to the corresponding exception class.

    Args:
        error (dict): The API response containing error information.

    Returns:
        PremError: An instance of the corresponding exception class.
    """
    error = error.json()
    error_code = error.get("code", None)
    message = error.get("message", "Unknown Error")
    provider = error.get("provider", None)
    model = error.get("model", None)
    provider_message = error.get("provider_message", None)

    error_mapping = {
        "NotFound": PremProviderNotFoundError,
        "APIError": PremProviderAPIError,
        "AuthenticationError": PremProviderAuthenticationError,
        "ConflictError": PremProviderConflictError,
        "APIStatusError": PremProviderAPIStatusError,
        "APITimeoutError": PremProviderAPITimeoutError,
        "RateLimitError": PremProviderRateLimitError,
        "BadRequestError": PremProviderBadRequestError,
        "APIConnectionError": PremProviderAPIConnectionError,
        "InternalServerError": PremProviderInternalServerError,
        "PermissionDeniedError": PremProviderPermissionDeniedError,
        "UnprocessableEntityError": PremProviderUnprocessableEntityError,
        "APIResponseValidationError": PremProviderAPIResponseValidationError,
        "ResponseValidationError": PremProviderResponseValidationError,
        "ModelNotFoundError": PremProviderResponseValidationError,
    }
    exception_class = error_mapping.get(error_code, PremError)
    raise exception_class(message, provider, model, provider_message)
