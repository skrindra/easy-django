from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from shared.constants import RESPONSE_MESSAGES

# Decorator to validate combined request data (body + query params) using a single serializer

def validate_request(serializer_class):
    """
    Validates combined query parameters and body data with the given serializer.
    Attaches cleaned data to request.validated_data.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            combined_data = {**request.query_params.dict(), **request.data}
            serializer = serializer_class(data=combined_data)
            if not serializer.is_valid():
                return Response({
                    "message": RESPONSE_MESSAGES["INVALID_PAYLOAD"],
                    "errors": serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)
            request.validated_data = serializer.validated_data
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
  
