from rest_framework.serializers import ModelSerializer
from .models import Quote
import bleach

class QuoteSerializer(ModelSerializer):
    """
    Serializer for the Quote model.

    Serializes and deserializes Quote instances, including the following fields:
        - id: Integer, unique identifier for the quote.
        - text: String, the content of the quote.
        - author: String, the author of the quote.
    """
    
    def validate(self, attrs):
        attrs["text"] = bleach.clean(attrs["text"]).strip()
        attrs["author"] = bleach.clean(attrs["author"]).strip()
        
        return super().validate(attrs)

    class Meta:
        model = Quote
        fields = ["id", "text", "author"]
