import unittest
from Product import Product
from vp_rule import VP_rule

class TestVPRule (unittest.TestCase):

    def test_one_green_tea(self):
        prod = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod]
        result = VP_rule(arr_prods)
        self.assertEqual(result, 11.23)

    def test_three_green_tea(self):
        prod1 = Product('CF1', 'Coffee', 11.23)
        prod2 = Product('CF1', 'Coffee', 11.23)
        prod3 = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod1, prod2, prod3]
        result = VP_rule(arr_prods)
        self.assertEqual(result, 22.46)

    def test_no_green_tea(self):
        arr_prods = []
        result = VP_rule(arr_prods)
        self.assertEqual(result, 0)
    
    def test_many_coffies(self):
        prod = Product('CF1', 'Coffee', 11.23)
        arr_prods = [prod] * 7
        result = VP_rule(arr_prods)
        self.assertEqual(result, 56.15)

if __name__ == '__main__':
    unittest.main()