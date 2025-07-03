from django.views.generic import ListView, DetailView
from .models import DishType


class DishTypeListView(ListView):
    model = DishType
    template_name = 'catalog/dishtype_list.html'
    context_object_name = 'dishtypes'


class DishTypeDetailView(DetailView):
    model = DishType
    template_name = 'catalog/dishtype_detail.html'
    context_object_name = 'dishtype'
