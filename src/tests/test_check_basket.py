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
    
    def test_with_especial_products(self):
        prod1 = Product('HS', 'Shampoo HS', 9.99)
        prod2 = Product('GR1', 'Green Tea', 3.11)
        prod3 = Product('SC', 'Sea Crab', 25)
        prod4 = Product('GR1', 'Green Tea', 3.11)
        prod5 = Product('FE', 'Fresh Eggs', 0.5)
        arr_prods = [prod1] + [prod2] + [prod3] + [prod4] + [prod5] * 6
        result = handle_basket(arr_prods, 3.11)
        self.assertEqual(result, 41.1)

    def test_no_normal_products(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1] * 4 + [prod2] * 5 + [prod3] * 13
        result = handle_basket(arr_prods, 130.79)
        self.assertEqual(result, 130.79)

    def test_long_shopping(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('FE', 'Fresh Eggs', 0.5)
        prod3 = Product('SR1', 'Strawberries', 5)
        prod4 = Product('SC', 'Sea Crab', 25)
        prod5 = Product('CF1', 'Coffee', 11.23)
        prod6 = Product('OJ', 'Orange Juice', 3)
        arr_prods = [prod1] * 2 + [prod3] * 9 + [prod6] * 8 + [prod1] + [prod5] + [prod4] * 2 + [prod5] + [prod2] * 12 + [prod3] + [prod1]
        result = handle_basket(arr_prods, 74.18)
        self.assertEqual(result, 154.18)

    def test_no_products(self):
        arr_prods = []
        result = handle_basket(arr_prods, 0)
        self.assertEqual(result, 0)