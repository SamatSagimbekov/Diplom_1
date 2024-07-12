from praktikum.burger import Burger
from config import FLUORESCENT_BUN, INGREDIENT_RINGS


class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        ingredient = mock_ingredient
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) != 0
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, mock_ingredient):
        ingredient_first = mock_ingredient
        ingredient_second = mock_ingredient
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        burger.remove_ingredient(1)
        assert ingredient_first in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, mock_ingredient):
        ingredient_first = mock_ingredient
        ingredient_second = mock_ingredient
        burger = Burger()
        burger.add_ingredient(ingredient_first)
        burger.add_ingredient(ingredient_second)
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == ingredient_first

    def test_get_price_without_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        price = burger.get_price()
        assert FLUORESCENT_BUN["price"]*2 == price

    def test_get_price_with_ingredient(self, mock_bun, mock_ingredient):
        ingredient = mock_ingredient
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        price = burger.get_price()
        assert (FLUORESCENT_BUN["price"]*2) + INGREDIENT_RINGS["price"] == price

    def test_get_receipt_without_ingredient(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        print(burger.get_receipt())
        assert FLUORESCENT_BUN["name"] in burger.get_receipt()
        assert str((FLUORESCENT_BUN["price"]*2)) in burger.get_receipt()

    def test_get_receipt_with_ingredient(self, mock_bun, mock_ingredient):
        ingredient = mock_ingredient
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        assert FLUORESCENT_BUN["name"] in burger.get_receipt()
        assert str((FLUORESCENT_BUN["price"] * 2) + INGREDIENT_RINGS["price"]) in burger.get_receipt()

    def test_get_receipt_is_string(self, mock_bun, mock_ingredient):
        ingredient = mock_ingredient
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(ingredient)
        assert isinstance(burger.get_receipt(), str)
