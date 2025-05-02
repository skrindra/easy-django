class NotFoundError(Exception):
    """Custom exception for not found resources."""
    pass

class UnauthorizedError(Exception):
    """Custom exception for unauthorized access."""
    pass

class BadRequestError(Exception):
    """Custom exception for bad requests or validation errors."""
    pass
