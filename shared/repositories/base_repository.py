from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    """
    Base repository to encapsulate all data access methods
    and enforce query logic reuse across services.
    """
    def __init__(self, model: models.Model):
        self.model = model

    def get_by_id(self, id):
        """Retrieve a model instance by its primary key."""
        try:
            return self.model.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    def filter(self, **filters):
        """Filter records based on provided keyword arguments."""
        return self.model.objects.filter(**filters)

    def get_or_none(self, **filters):
        """Return first match or None if not found."""
        return self.model.objects.filter(**filters).first()

    def all(self):
        """Return all objects for the model."""
        return self.model.objects.all()

    def create(self, **data):
        """Create a new object with the given data."""
        return self.model.objects.create(**data)

    def update(self, instance, **data):
        """Update an existing instance with new data."""
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        """Delete a model instance."""
        instance.delete()
        return True

    def bulk_create(self, objects):
        """Bulk insert model objects."""
        return self.model.objects.bulk_create(objects)

    def exists(self, **filters):
        """Check if any object matches the filters."""
        return self.model.objects.filter(**filters).exists()

