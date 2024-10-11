import unittest
from Product import Product
from ceo_rule import CEO_rule

class TestCEORule (unittest.TestCase):

    def test_one_green_tea(self):
        prod = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 3.11)

    def test_two_green_tea(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod1, prod2]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 3.11)

    def test_three_green_tea(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('GR1', 'Green Tea', 3.11)
        prod3 = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod1, prod2, prod3]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 6.22)

    def test_no_green_tea(self):
        arr_prods = []
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()