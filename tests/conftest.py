import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from config import FLUORESCENT_BUN, INGREDIENT_RINGS
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)

    bun.get_name.return_value = FLUORESCENT_BUN["name"]
    bun.get_price.return_value = FLUORESCENT_BUN["price"]
    return bun


@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = INGREDIENT_RINGS["name"]
    ingredient.get_price.return_value = INGREDIENT_RINGS["price"]
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient
