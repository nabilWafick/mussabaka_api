from django.urls import path
from .views import CandidatesViewSet

candidates_list = CandidatesViewSet.as_view(
    {
        "get": "list",
        "post": "create",
    }
)

candidates_detail = CandidatesViewSet.as_view(
    {
        "get": "retrieve",
        "put": "update",
        "patch": "update",
        "delete": "destroy",
    }
)

urlpatterns = [
    path("", candidates_list, name="candidates_list"),
    path("<int:pk>", candidates_detail, name="candidates_detail"),
]
