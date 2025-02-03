from django.urls import path
from .views import UsersViewSet

users_list = UsersViewSet.as_view({"get": "list", "post": "create"})

users_detail = UsersViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", users_list, name="users_list"),
    path("<int:pk>", users_detail, name="users_detail"),
]
