from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Dish, Chef, DishType, Ingredient
from django.shortcuts import redirect
from django.views import View


class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        return redirect("/admin/")


# ==================== Dish Views ====================
class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "catalog/dish_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context


class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = "__all__"
    template_name = "catalog/dish_form.html"
    success_url = reverse_lazy("dish-list")


class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "catalog/dish_form.html"
    success_url = reverse_lazy("dish-list")


class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    template_name = "catalog/dish_confirm_delete.html"
    success_url = reverse_lazy("dish-list")


# ==================== Chef Views ====================
class ChefListView(LoginRequiredMixin, ListView):
    model = Chef
    context_object_name = "chef_list"
    template_name = "catalog/chef_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context


class ChefCreateView(LoginRequiredMixin, CreateView):
    model = Chef
    fields = "__all__"
    template_name = "catalog/chef_form.html"
    success_url = reverse_lazy("chef-list")


class ChefUpdateView(LoginRequiredMixin, UpdateView):
    model = Chef
    fields = "__all__"
    template_name = "catalog/chef_form.html"
    success_url = reverse_lazy("chef-list")


class ChefDeleteView(LoginRequiredMixin, DeleteView):
    model = Chef
    template_name = "catalog/chef_confirm_delete.html"
    success_url = reverse_lazy("chef-list")


# ==================== DishType Views ====================
class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "catalog/dishtype_list.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishTypeCreateView(LoginRequiredMixin, CreateView):
        model = DishType
        fields = "__all__"
        template_name = "catalog/dishtype_form.html"
        success_url = reverse_lazy("catalog:dishtype-list")

class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "catalog/dishtype_form.html"
    success_url = reverse_lazy("dishtype-list")


class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = "catalog/dishtype_confirm_delete.html"
    success_url = reverse_lazy("dishtype-list")


# ==================== Ingredient Views ====================
class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "catalog/ingredient_list.html"


class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "catalog/ingredient_form.html"
    success_url = reverse_lazy("ingredient-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context


class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = "__all__"
    template_name = "catalog/ingredient_form.html"
    success_url = reverse_lazy("ingredient-list")


class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "catalog/ingredient_confirm_delete.html"
    success_url = reverse_lazy("ingredient-list")
