from django.urls import path
from .views import CategoriesViewSet

categories_list = CategoriesViewSet.as_view({
    'get': 'list',     
    'post': 'create'    
})

categories_detail = CategoriesViewSet.as_view({
    'get': 'retrieve',  
    'put': 'update',    
    'patch': 'update', 
    'delete': 'destroy'
})

urlpatterns = [
   
    path('', categories_list, name='categories_list'),
    path('<int:pk>', categories_detail, name='categories_detail'),
]
