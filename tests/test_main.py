# test_main.py
import unittest
from unittest.mock import mock_open, patch
from app.app import app

class TestApp(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='{"cars": [{"id": 1, "make": "Toyota"}]}')
    def test_cars_route(self, mock_file):
        with app.test_client() as client:
            response = client.get('/cars')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)  

if __name__ == '__main__':
    unittest.main()
