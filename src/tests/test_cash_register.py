import unittest
from unittest.mock import patch
from io import StringIO
import sys
parent_dir = ".."
sys.path.append(parent_dir)
from modules.cash_register import compute

class TestCashRegister (unittest.TestCase):
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)

    # Test to check the input of only one product
    def test_one_product(self, stdout_mock, mock_input):
        mock_input.side_effect = ["GR1", "Green Tea", 3.11, '', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| GR1 | Green Tea | 3.11€ |\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '| GR1 | 3.11€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 6)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)

    # Test to check when no products are introduced
    def test_no_products(self, stdout_mock, mock_input):
        mock_input.side_effect = ['', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '|  | 0€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 3)
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)

    # Test to check that not fully introducing a product leads to the product not being added
    def test_wrong_input_1(self, stdout_mock, mock_input):
        mock_input.side_effect = ['GR1', '', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '|  | 0€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 4)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)

    # Test to check that not fully introducing a product leads to the product not being added
    def test_wrong_input_2(self, stdout_mock, mock_input):
        mock_input.side_effect = ['GR1', 'Green Tea', '', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '|  | 0€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 5)
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)

    # Test to check the input of multiple products
    def test_two_products(self, stdout_mock, mock_input):
        mock_input.side_effect = ["GR1", "Green Tea", 3.11, "SR1", "Strawberries", 5, '', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| GR1 | Green Tea | 3.11€ |\n' + '| SR1 | Strawberries | 5.0€ |\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '| GR1,SR1 | 8.11€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 9)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    
    # Test to check that the price is a number
    def test_wrong_price(self, stdout_mock, mock_input):
        mock_input.side_effect = ["Test", "Test", "Test", 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + 'Price must be a number'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 5)

if __name__ == '__main__':
    unittest.main()
