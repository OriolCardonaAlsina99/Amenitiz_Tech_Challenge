import unittest
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.Product import Product

class TestProduct(unittest.TestCase):

    # Test for the test runner (no executed, prior to the tests)
    def setUp(self):
        self.obj = Product('Test', 'Testing Product', 0)

    # Test for the constructor class
    def test_constructor(self):
        self.assertIsNotNone(self.obj)

    # Test for getter of the identifier
    def test_get_id(self):
        expected_id = "Test"
        self.assertEqual(self.obj.getId(), expected_id)

    # Test for getter of the name
    def test_get_name(self):
        expected_name = "Testing Product"
        self.assertEqual(self.obj.getName(), expected_name)

    # Test for getter of the price
    def test_get_price(self):
        expected_price = 0
        self.assertEqual(self.obj.getPrice(), expected_price)

if __name__ == '__main__':
    unittest.main()