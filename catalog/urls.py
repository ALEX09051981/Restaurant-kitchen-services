from django.urls import path
from .views import DishTypeListView, DishTypeDetailView

app_name = 'catalog'

urlpatterns = [
    path('dishtypes/', DishTypeListView.as_view(), name='dishtype-list'),
    path('dishtypes/<int:pk>/', DishTypeDetailView.as_view(), name='dishtype-detail'),
]
