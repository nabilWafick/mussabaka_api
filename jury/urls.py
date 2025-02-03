from django.urls import path
from .views import JuryViewSet

jury_list = JuryViewSet.as_view({"get": "list", "post": "create"})

jury_detail = JuryViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", jury_list, name="jury_list"),
    path("<int:pk>", jury_detail, name="jury_detail"),
]
