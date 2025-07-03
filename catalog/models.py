from django.contrib.auth.models import AbstractUser
from django.db import models

class Chef(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


class DishType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes')
    chefs = models.ManyToManyField(Chef, related_name='dishes')
    ingredients = models.ManyToManyField(Ingredient, blank=True, related_name='dishes')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
