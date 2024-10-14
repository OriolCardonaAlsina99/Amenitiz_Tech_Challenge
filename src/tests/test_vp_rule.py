import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product
from modules.vp_rule import VP_rule

class TestVPRule (unittest.TestCase):

    # Test for the edge case of not enough products to test the discount
    def test_no_offer(self):
        prod = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod]
        result = VP_rule(arr_prods)
        self.assertEqual(result, 11.23)

    # Test when we are have enough products for a discount
    def test_especial_offer(self):
        prod1 = Product('CF1', 'Coffee', 11.23)
        prod2 = Product('CF1', 'Coffee', 11.23)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3]
        result = VP_rule(arr_prods)
        self.assertEqual(result, 22.46)

    # Test when no products are introduced
    def test_no_products(self):
        arr_prods = []
        result = VP_rule(arr_prods)
        self.assertEqual(result, 0)

    # Test when there are enough products that some do not apply for discount
    def test_many_products(self):
        prod = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod] * 7
        result = VP_rule(arr_prods)
        self.assertEqual(result, 56.15)

if __name__ == '__main__':
    unittest.main()
