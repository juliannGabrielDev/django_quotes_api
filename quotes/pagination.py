from rest_framework.pagination import PageNumberPagination


class Paginator(PageNumberPagination):
    """
    Custom paginator class that extends PageNumberPagination to control pagination behavior.

    Attributes:
        page_size (int): The default number of items to include on each page. Defaults to 5.
        page_size_query_param (str): The query parameter name that allows clients to set a custom page size. Defaults to "per_page".
        max_page_size (int): The maximum number of items allowed per page when specified by the client. Defaults to 20.
    """
    page_size = 5
    page_size_query_param = "per_page"
    max_page_size = 20
