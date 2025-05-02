# Centralized constants (choices, messages, etc.)

USER_ROLES = (
    ("admin", "Admin"),
    ("researcher", "Researcher"),
    ("qa", "Quality Assurance"),
)

DEFAULT_PAGE_SIZE = 20
MAX_UPLOAD_SIZE_MB = 10

RESPONSE_MESSAGES = {
    "NOT_FOUND": "Resource not found.",
    "INVALID_PAYLOAD": "Invalid data provided.",
    "SUCCESS": "Request processed successfully.",
    "ERROR": "An error occurred. Please try again.",
    "UNAUTHORIZED": "You are not authorized to perform this action."
}
