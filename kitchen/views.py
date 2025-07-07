from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.shortcuts import redirect
from django.views import View

from .models import Dish, Chef, DishType, Ingredient


class HomeRedirectView(View):
    def get(self, request, *args, **kwargs):
        return redirect("/admin/")


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "kitchen/dish_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishCreateView(LoginRequiredMixin, CreateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishUpdateView(LoginRequiredMixin, UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishDeleteView(LoginRequiredMixin, DeleteView):
    model = Dish
    template_name = "kitchen/confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-list")


class ChefListView(LoginRequiredMixin, ListView):
    model = Chef
    context_object_name = "chef_list"
    template_name = "kitchen/chef_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class ChefCreateView(LoginRequiredMixin, CreateView):
    model = Chef
    fields = "__all__"
    template_name = "kitchen/chef_form.html"
    success_url = reverse_lazy("kitchen:chef-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class ChefUpdateView(LoginRequiredMixin, UpdateView):
    model = Chef
    fields = "__all__"
    template_name = "kitchen/chef_form.html"
    success_url = reverse_lazy("kitchen:chef-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class ChefDeleteView(LoginRequiredMixin, DeleteView):
    model = Chef
    template_name = "kitchen/confirm_delete.html"
    success_url = reverse_lazy("kitchen:chef-list")


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "kitchen/dishtype_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishTypeCreateView(LoginRequiredMixin, CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dishtype-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class DishTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = DishType
    template_name = "kitchen/confirm_delete.html"
    success_url = reverse_lazy("kitchen:dishtype-list")


class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    context_object_name = "ingredient_list"
    template_name = "kitchen/ingredient_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = "__all__"
    template_name = "kitchen/ingredient_form.html"
    success_url = reverse_lazy("kitchen:ingredient-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = "__all__"
    template_name = "kitchen/ingredient_form.html"
    success_url = reverse_lazy("kitchen:ingredient-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model._meta.model_name
        context["model_name_plural"] = self.model._meta.verbose_name_plural.title()
        return context

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "kitchen/confirm_delete.html"
    success_url = reverse_lazy("kitchen:ingredient-list")
