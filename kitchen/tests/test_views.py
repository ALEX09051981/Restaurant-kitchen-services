from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import Dish, Chef, DishType, Ingredient

User = get_user_model()

class BaseViewTestMixin:
    """Mixin for creating and logging in a user before each test."""
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

# -------------------- Dish --------------------

class DishListViewTest(BaseViewTestMixin, TestCase):
    def test_list_view_status_and_template(self):
        url = reverse("kitchen:dish-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

class DishCreateViewTest(BaseViewTestMixin, TestCase):
    def setUp(self):
        super().setUp()
        self.dishtype = DishType.objects.create(name="Soup")

    def test_create_dish(self):
        url = reverse("kitchen:dish-create")
        data = {
            "name": "Tomato Soup",
            "dish_type": self.dishtype.id,
            "chefs": [self.user.id],
            "ingredients": [],
            "description": "Delicious soup",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Tomato Soup").exists())

# -------------------- Chef --------------------

class ChefListViewTest(BaseViewTestMixin, TestCase):
    def test_list_view(self):
        url = reverse("kitchen:chef-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/chef_list.html")

# -------------------- DishType --------------------

class DishTypeListViewTest(BaseViewTestMixin, TestCase):
    def test_list_view(self):
        url = reverse("kitchen:dishtype-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dishtype_list.html")

# -------------------- Ingredient --------------------

class IngredientListViewTest(BaseViewTestMixin, TestCase):
    def test_list_view(self):
        url = reverse("kitchen:ingredient-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/ingredient_list.html")
