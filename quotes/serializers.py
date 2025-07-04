from rest_framework.serializers import ModelSerializer
from .models import Quote


class QuoteSerializer(ModelSerializer):
    """Serializer for the Quote model."""

    class Meta:
        model = Quote
        fields = ["id", "text", "author"]
