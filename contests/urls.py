from django.urls import path
from .views import ContestsViewSet

contests_list = ContestsViewSet.as_view({"get": "list", "post": "create"})

contests_detail = ContestsViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", contests_list, name="contests_list"),
    path("<int:pk>", contests_detail, name="contests_detail"),
]
