import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.obj = Product('Test', 'Testing Product', 0)

    def test_constructor(self):
        self.assertIsNotNone(self.obj)

    def test_get_id(self):
        expected_id = "Test"
        self.assertEqual(self.obj.getId(), expected_id)

    def test_get_name(self):
        expected_name = "Testing Product"
        self.assertEqual(self.obj.getName(), expected_name)

    def test_get_price(self):
        expected_price = 0
        self.assertEqual(self.obj.getPrice(), expected_price)

if __name__ == '__main__':
    unittest.main()