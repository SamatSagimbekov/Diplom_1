import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from config import INGREDIENT_RINGS


class TestIngredient:

    def test_get_name(self):
        name = INGREDIENT_RINGS["name"]
        price = INGREDIENT_RINGS["price"]
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert name == ingredient.get_name()

    def test_get_price(self):
        name = INGREDIENT_RINGS["name"]
        price = INGREDIENT_RINGS["price"]
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, price)
        assert price == ingredient.get_price()

    @pytest.mark.parametrize(
        "ingredient_types", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_types):
        name = INGREDIENT_RINGS["name"]
        price = INGREDIENT_RINGS["price"]
        ingredient = Ingredient(ingredient_types, name, price)
        assert ingredient_types == ingredient.get_type()
