from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from .models import Quote
from .serializers import QuoteSerializer
from .pagination import Paginator


class RandomQuote(APIView):
    """API view to retrieve a random quote."""
    
    throttle_classes = [UserRateThrottle]

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests to return a random quote from the database.
        If no quotes are available, it returns a 404 Not Found response.
        """
        quotes_count = Quote.objects.count()

        if not quotes_count:
            return Response(
                {"message": "No quotes available."}, status=status.HTTP_404_NOT_FOUND
            )

        random_quote = Quote.objects.order_by("?").first()

        serializer = QuoteSerializer(random_quote)

        return Response(serializer.data, status=status.HTTP_200_OK)


class QuotesViewSet(ModelViewSet):
    """
    A viewset for viewing, creating, updating and deleting quotes.

    This viewset provides full CRUD access to the Quote model, supporting pagination,
    ordering, and search functionality.
    """
    queryset = Quote.objects.all()
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
    serializer_class = QuoteSerializer
    pagination_class = Paginator
    ordering_fields = ["quote", "author"]
    search_fields = ["quote", "author"]
