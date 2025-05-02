from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shared.constants import RESPONSE_MESSAGES
from shared.exceptions.custom_exceptions import NotFoundError, UnauthorizedError, BadRequestError

class BaseAPIView(APIView):
    """
    Base class for handling GET, POST, PUT and DELETE requests.
    Apply business logic via service injected into the view.
    Handles known exceptions gracefully.
    """
    service_class = None  # Should be set in the subclass

    def _handle_request(self, method, request):
        try:
            service = self.service_class()
            return getattr(service, method)(request.validated_data)
        except NotFoundError as e:
            return Response({"message": str(e)}, status=status.HTTP_404_NOT_FOUND)
        except UnauthorizedError as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except BadRequestError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": RESPONSE_MESSAGES["ERROR"], "detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, *args, **kwargs):
        """Handle GET request using service.retrieve."""
        result = self._handle_request("retrieve", request)
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Handle POST request using service.create."""
        result = self._handle_request("create", request)
        return Response(result, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        """Handle PUT request using service.update."""
        result = self._handle_request("update", request)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        """Handle DELETE request using service.delete."""
        result = self._handle_request("delete", request)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
