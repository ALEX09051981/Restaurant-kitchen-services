from django.contrib import admin
from .models import Chef, DishType, Ingredient, Dish


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ("username", "phone", "email", "first_name", "last_name")
    search_fields = ("username", "phone", "email", "first_name", "last_name")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "dish_type",
    )
    search_fields = ("name",)
    list_filter = ("dish_type", "chefs")
    filter_horizontal = ("chefs", "ingredients")
