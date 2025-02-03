from django.urls import path
from .views import SchoolsViewSet

schools_list = SchoolsViewSet.as_view({"get": "list", "post": "create"})

schools_detail = SchoolsViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", schools_list, name="schools_list"),
    path("<int:pk>", schools_detail, name="schools_detail"),
]
