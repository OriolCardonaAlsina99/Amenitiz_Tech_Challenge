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
    def test_one_product(self, stdout_mock, mock_input):
        mock_input.side_effect = ["GR1", "Green Tea", 3.11, '', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| GR1 | Green Tea | 3.11€ |\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '| GR1 | 3.11€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 6)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_products(self, stdout_mock, mock_input):
        mock_input.side_effect = ['', 'close_cash_register', '']
        compute()
        output = stdout_mock.getvalue().strip()
        result = '| Product Code | Name | Price |\n' + '|--|--|--|\n' + '| Basket | Total price expected |\n' + '|--|--|\n' + '|  | 0€ |'
        self.assertEqual(output, result) 
        self.assertEqual(mock_input.call_count, 3)

if __name__ == '__main__':
    unittest.main()