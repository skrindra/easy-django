from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer to standardize update logic and representation.
    """
    def update(self, instance, validated_data):
        """Update model instance from validated data."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        """Customize outgoing serialized response if needed."""
        rep = super().to_representation(instance)
        return rep
