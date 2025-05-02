from shared.constants import DEFAULT_PAGE_SIZE
from shared.exceptions.custom_exceptions import NotFoundError

class BaseService:
    """
    Base service for writing business logic over repositories.
    Provides standard CRUD methods.
    """
    def __init__(self, repository):
        self.repository = repository

    def retrieve(self, filters):
        """Retrieve resource(s) based on filters."""
        return self.repository.filter(**filters)

    def paginated(self, filters, page=1, page_size=DEFAULT_PAGE_SIZE):
        """Retrieve paginated list of resources."""
        queryset = self.repository.filter(**filters)
        offset = (page - 1) * page_size
        return queryset[offset:offset + page_size]

    def create(self, data):
        """Create a resource with the given data."""
        return self.repository.create(**data)

    def update(self, data):
        """Update an existing resource identified by ID."""
        instance = self.repository.get_by_id(data.get("id"))
        if not instance:
            raise NotFoundError("Resource not found")
        return self.repository.update(instance, **data)

    def delete(self, data):
        """Delete a resource identified by ID."""
        instance = self.repository.get_by_id(data.get("id"))
        if not instance:
            raise NotFoundError("Resource not found")
        return self.repository.delete(instance)

