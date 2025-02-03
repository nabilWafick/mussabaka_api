from django.urls import path
from .views import ResultsViewSet

results_list = ResultsViewSet.as_view({"get": "list", "post": "create"})

results_detail = ResultsViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
)

urlpatterns = [
    path("", results_list, name="results_list"),
    path("<int:pk>", results_detail, name="results_detail"),
]
