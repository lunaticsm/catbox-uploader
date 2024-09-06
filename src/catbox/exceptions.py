class CatboxError(Exception):
    """Custom exception for Catbox errors."""
    pass

class FileNotFoundError(CatboxError):
    """Exception raised when a file is not found."""
    pass

class URLError(CatboxError):
    """Exception raised when there's an issue with the provided URL."""
    pass