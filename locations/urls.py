from django.urls import path
from .views import LocationsViewSet

locations_list = LocationsViewSet.as_view({"get": "list", "post": "create"})

locations_detail = LocationsViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", locations_list, name="locations_list"),
    path("<int:pk>", locations_detail, name="locations_detail"),
]
