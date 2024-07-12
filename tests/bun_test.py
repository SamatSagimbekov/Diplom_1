from praktikum.bun import Bun
from config import FLUORESCENT_BUN


class TestBun:

    def test_get_name(self):
        name = FLUORESCENT_BUN["name"]
        price = FLUORESCENT_BUN["price"]
        bun = Bun(name, price)
        assert name == bun.get_name()

    def test_get_name_is_string(self):
        name = FLUORESCENT_BUN["name"]
        price = FLUORESCENT_BUN["price"]
        bun = Bun(name, price)
        assert isinstance(bun.get_name(), str)

    def test_get_price(self):
        name = FLUORESCENT_BUN["name"]
        price = FLUORESCENT_BUN["price"]
        bun = Bun(name, price)
        assert price == bun.get_price()

    def test_get_price_is_integer(self):
        name = FLUORESCENT_BUN["name"]
        price = FLUORESCENT_BUN["price"]
        bun = Bun(name, price)
        assert isinstance(bun.get_price(), int)
