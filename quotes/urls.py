from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.QuotesViewSet)

app_name = "quotes"

urlpatterns = [
    path("quotes/random/", views.RandomQuote.as_view(), name="random_quote"),
    path("quotes/", include(router.urls)),
]
