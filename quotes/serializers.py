from rest_framework.serializers import ModelSerializer
from .models import Quote


class QuoteSerializer(ModelSerializer):
    """
    Serializer for the Quote model.

    Serializes and deserializes Quote instances, including the following fields:
        - id: Integer, unique identifier for the quote.
        - text: String, the content of the quote.
        - author: String, the author of the quote.
    """

    class Meta:
        model = Quote
        fields = ["id", "text", "author"]
