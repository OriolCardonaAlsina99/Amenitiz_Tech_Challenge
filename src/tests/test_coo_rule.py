import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product
from modules.coo_rule import COO_rule

class TestCOORule (unittest.TestCase):

    # Test for the edge case of not enough products to test the discount
    def test_no_offer(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2]
        result = COO_rule(arr_prods)
        self.assertEqual(result, 10)

    # Test when we are have enough products for a discount
    def test_especial_offer(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2, prod3]
        result = COO_rule(arr_prods)
        self.assertEqual(result, 13.5)

    # Test when no products are introduced
    def test_no_products(self):
        arr_prods = []
        result = COO_rule(arr_prods)
        self.assertEqual(result, 0)

    # Test when there are enough products that some do not apply for discount
    def test_many_products(self):
        prod = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod] * 8
        result = COO_rule(arr_prods)
        self.assertEqual(result, 37)

if __name__ == '__main__':
    unittest.main()
