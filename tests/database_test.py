from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_list_not_empty(self):
        database = Database()
        print(vars(database.available_buns()[0]))
        assert database.buns != 0

    def test_available_ingredients_sauce_type_present(self):
        database = Database()
        assert INGREDIENT_TYPE_SAUCE == vars(database.available_ingredients()[0])['type']

    def test_available_ingredients_filling_type_present(self):
        database = Database()
        assert INGREDIENT_TYPE_FILLING == vars(database.available_ingredients()[-1])['type']
