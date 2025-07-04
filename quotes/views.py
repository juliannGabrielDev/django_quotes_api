from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Quote
from .serializers import QuoteSerializer
from .pagination import Paginator


class RandomQuote(APIView):
    """API view to retrieve a random quote."""

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


class QuotesViewSet(ReadOnlyModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    pagination_class = Paginator
    ordering_fields = ["quote", "author"]
    search_fields = ["quote", "author"]
