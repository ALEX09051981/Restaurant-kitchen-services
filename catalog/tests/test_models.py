from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Chef, DishType, Ingredient, Dish

User = get_user_model()

class ChefModelTest(TestCase):
    def test_str_returns_username(self):
        chef = Chef.objects.create_user(username="chef1", password="pass1234")
        self.assertEqual(str(chef), "chef1")

class DishTypeModelTest(TestCase):
    def test_str_returns_name(self):
        dish_type = DishType.objects.create(name="Salad", description="Fresh salads")
        self.assertEqual(str(dish_type), "Salad")

class IngredientModelTest(TestCase):
    def test_str_returns_name(self):
        ingredient = Ingredient.objects.create(name="Tomato")
        self.assertEqual(str(ingredient), "Tomato")

class DishModelTest(TestCase):
    def setUp(self):
        self.chef = Chef.objects.create_user(username="chef1", password="pass1234")
        self.dish_type = DishType.objects.create(name="Salad")
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Cucumber")

    def test_str_returns_name(self):
        dish = Dish.objects.create(name="Greek Salad", dish_type=self.dish_type)
        dish.chefs.add(self.chef)
        dish.ingredients.add(self.ingredient1, self.ingredient2)
        self.assertEqual(str(dish), "Greek Salad")

    def test_dish_has_chefs_and_ingredients(self):
        dish = Dish.objects.create(name="Greek Salad", dish_type=self.dish_type)
        dish.chefs.add(self.chef)
        dish.ingredients.add(self.ingredient1, self.ingredient2)
        self.assertIn(self.chef, dish.chefs.all())
        self.assertIn(self.ingredient1, dish.ingredients.all())
        self.assertIn(self.ingredient2, dish.ingredients.all())
