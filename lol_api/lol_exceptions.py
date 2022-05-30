class LoLException(Exception):
    pass


class BadRequest(LoLException):
    pass


class Unauthorized(LoLException):
    pass


class Forbidden(LoLException):
    pass


class NotFound(LoLException):
    pass


class NotAllowed(LoLException):
    pass


class UnsupportedMediaType(LoLException):
    pass


class RateLimitExceeded(LoLException):
    pass


class InternalServerError(LoLException):
    pass


class BadGateway(LoLException):
    pass


class ServiceUnavailable(LoLException):
    pass


class GatewayTimeout(LoLException):
    pass
