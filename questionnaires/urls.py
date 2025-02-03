from django.urls import path
from .views import QuestionnairesViewSet

questionnaires_list = QuestionnairesViewSet.as_view({"get": "list", "post": "create"})

questionnaires_detail = QuestionnairesViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", questionnaires_list, name="questionnaires_list"),
    path("<int:pk>", questionnaires_detail, name="questionnaires_detail"),
]
