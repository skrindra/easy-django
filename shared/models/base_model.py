from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """
    Abstract base model that provides common fields to all models.
    - created_at: Timestamp when object is created
    - updated_at: Timestamp when object is last updated
    - is_active: Boolean flag to soft-delete records
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        """Mark the object as inactive instead of deleting it permanently."""
        self.is_active = False
        self.save()

    def restore(self):
        """Restore a soft-deleted object."""
        self.is_active = True
        self.save()

