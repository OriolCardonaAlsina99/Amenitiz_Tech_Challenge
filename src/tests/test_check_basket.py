import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from Product import Product
from rules.check_basket import handle_basket

class TestCheckBasket (unittest.TestCase):
    def test_no_especial_products(self):
        prod1 = Product('HS', 'Shampoo HS', 9.99)
        prod2 = Product('OC', 'Oreo Cookies', 1.5)
        prod3 = Product('TS', 'Tomatoe Sauce', 4.99)
        arr_prods = [prod1, prod2, prod3]
        result = handle_basket(arr_prods, 0)
        self.assertEqual(result, 16.48)