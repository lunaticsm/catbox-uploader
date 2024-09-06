class CatboxError(Exception):
    """Base exception for Catbox errors."""
    pass

class FileNotFoundError(CatboxError):
    """Exception raised when a file is not found."""
    pass

class TimeoutError(CatboxError):
    """Exception raised when the request times out."""
    pass

class ConnectionError(CatboxError):
    """Exception raised when there is a connection error."""
    pass

class HTTPError(CatboxError):
    """Exception raised for HTTP errors."""
    pass
