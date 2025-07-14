from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from kitchen.models import Dish, DishType, Ingredient, Chef


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "dish_type", "cook", "ingredients"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save Dish"))


class DishTypeForm(forms.ModelForm):
    class Meta:
        model = DishType
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save Type"))


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save Ingredient"))


class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ["name", "email", "experience"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Save Chef"))
