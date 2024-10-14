import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product
from modules.check_rules import handle_rules

class TestCheckRules (unittest.TestCase):

    # Test to check if each method is accessed
    def test_one_of_each(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3]
        result = handle_rules(arr_prods)
        self.assertEqual(result, 19.34)

    # Test when no products are introduced
    def test_no_products(self):
        arr_prods = []
        result = handle_rules(arr_prods)
        self.assertEqual(result, 0)

    # Test for the example number 2 of the assignment
    def test_case_2_assignment(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('GR1', 'Green Tea', 3.11)
        prod4 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2, prod3, prod4]
        result = handle_rules(arr_prods)
        self.assertEqual(result, 16.61)

    # Test for the example number 3 of the assignment
    def test_case_3_assignment(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('CF1', 'Coffee', 11.23)
        prod3 = Product('SR1', 'Strawberries', 5)
        prod4 = Product('CF1', 'Coffee', 11.23)
        prod5 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3, prod4, prod5]
        result = handle_rules(arr_prods)
        self.assertEqual(result, 30.57)

    # Test to check when many special offers are applied
    def test_long_shopping(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1] * 2 + [prod2] * 9 + [prod3] * 8
        result = handle_rules(arr_prods)
        self.assertEqual(result, 110.99)
        
if __name__ == '__main__':
    unittest.main()

        
