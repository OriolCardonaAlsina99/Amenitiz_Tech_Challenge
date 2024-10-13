import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product
from modules.check_rules import check_rules

class TestCheckRules (unittest.TestCase):

    def test_one_of_each(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3]
        result = check_rules(arr_prods)
        self.assertEqual(result, 19.34)
    
    def test_case_2_assignment(self):
        prod1 = Product('SR1', 'Strawberries', 5)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('GR1', 'Green Tea', 3.11)
        prod4 = Product('SR1', 'Strawberries', 5)
        arr_prods = [prod1, prod2, prod3, prod4]
        result = check_rules(arr_prods)
        self.assertEqual(result, 16.61)

    def test_case_3_assignment(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('CF1', 'Coffee', 11.23)
        prod3 = Product('SR1', 'Strawberries', 5)
        prod4 = Product('CF1', 'Coffee', 11.23)
        prod5 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3, prod4, prod5]
        result = check_rules(arr_prods)
        self.assertEqual(result, 30.57)

    def test_long_shopping(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('SR1', 'Strawberries', 5)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1] * 2 + [prod2] * 9 + [prod3] * 8
        result = check_rules(arr_prods)
        self.assertEqual(result, 110.99)
        


        