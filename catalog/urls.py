from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("", views.HomeRedirectView.as_view(), name="home"),
    # Dish
    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish-delete"),

    # Chef
    path("chefs/", views.ChefListView.as_view(), name="chef-list"),
    path("chefs/create/", views.ChefCreateView.as_view(), name="chef-create"),
    path("chefs/<int:pk>/update/", views.ChefUpdateView.as_view(), name="chef-update"),
    path("chefs/<int:pk>/delete/", views.ChefDeleteView.as_view(), name="chef-delete"),

    # DishType
    path("dishtypes/", views.DishTypeListView.as_view(), name="dishtype-list"),
    path("dishtypes/create/", views.DishTypeCreateView.as_view(), name="dishtype-create"),
    path("dishtypes/<int:pk>/update/", views.DishTypeUpdateView.as_view(), name="dishtype-update"),
    path("dishtypes/<int:pk>/delete/", views.DishTypeDeleteView.as_view(), name="dishtype-delete"),

    # Ingredient
    path("ingredients/", views.IngredientListView.as_view(), name="ingredient-list"),
    path("ingredients/create/", views.IngredientCreateView.as_view(), name="ingredient-create"),
    path("ingredients/<int:pk>/update/", views.IngredientUpdateView.as_view(), name="ingredient-update"),
    path("ingredients/<int:pk>/delete/", views.IngredientDeleteView.as_view(), name="ingredient-delete"),
]
