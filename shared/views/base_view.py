from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shared.constants import RESPONSE_MESSAGES

class BaseAPIView(APIView):
    """
    Base class for handling GET, POST, PUT and DELETE requests.
    Apply business logic via service injected into the view.
    """
    service_class = None  # Should be set in the subclass

    def get(self, request, *args, **kwargs):
        """Handle GET request using service.retrieve."""
        service = self.service_class()
        result = service.retrieve(request.validated_data)
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handle POST request using service.create."""
        service = self.service_class()
        result = service.create(request.validated_data)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        """Handle PUT request using service.update."""
        service = self.service_class()
        result = service.update(request.validated_data)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """Handle DELETE request using service.delete."""
        service = self.service_class()
        result = service.delete(request.validated_data)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
