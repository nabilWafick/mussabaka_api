from django.urls import path
from .views import SurahsViewSet

surahs_list = SurahsViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

surahs_detail = SurahsViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("", surahs_list, name="surahs_list"),
    path("<int:pk>", surahs_detail, name="surahs_detail"),
]
