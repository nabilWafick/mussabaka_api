from django.urls import path
from .views import NotesViewSet

notes_list = NotesViewSet.as_view({"get": "list", "post": "create"})

notes_detail = NotesViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", notes_list, name="notes_list"),
    path("<int:pk>", notes_detail, name="notes_detail"),
]
