import unittest
from Product import Product
from ceo_rule import CEO_rule

class TestCEORule (unittest.TestCase):

    def test_no_offer(self):
        prod = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 3.11)

    def test_especial_offer(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod1, prod2]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 3.11)

    def test_no_products(self):
        arr_prods = []
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 0)

    def test_many_products(self):
        prod1 = Product('GR1', 'Green Tea', 3.11)
        prod2 = Product('GR1', 'Green Tea', 3.11)
        prod3 = Product('GR1', 'Green Tea', 3.11)
        arr_prods = [prod1, prod2, prod3]
        result = CEO_rule(arr_prods)
        self.assertEqual(result, 6.22)

if __name__ == '__main__':
    unittest.main()