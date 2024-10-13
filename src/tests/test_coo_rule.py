import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from Product import Product
from rules.coo_rule import COO_rule

class TestCOORule (unittest.TestCase):

    def test_no_offer(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2]
        result = COO_rule(arr_prods)
        self.assertEqual(result, 10)

    def test_especial_offer(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2, prod3]
        result = COO_rule(arr_prods)
        self.assertEqual(result, 13.5)

    def test_no_products(self):
        arr_prods = []
        result = COO_rule(arr_prods)
        self.assertEqual(result, 0)
    
    def test_many_products(self):
        prod = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod] * 8
        result = COO_rule(arr_prods)
        self.assertEqual(result, 37)

if __name__ == '__main__':
    unittest.main()