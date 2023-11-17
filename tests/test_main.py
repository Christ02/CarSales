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
            self.assertEqual(len(data), 1)

    @patch('builtins.open', new_callable=mock_open, read_data='{"motos": [{"id": 1, "make": "Honda"}]}')
    def test_motos_route(self, mock_file):
        with app.test_client() as client:
            response = client.get('/motos')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            
            if data:
                self.assertTrue(all('model' in moto for moto in data))

    @patch('builtins.open', new_callable=mock_open, read_data='{"sales": [{"id": 1, "buyer_name": "John"}]}')
    def test_sales_route(self, mock_file):
        with app.test_client() as client:
            response = client.get('/sales')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            
            if data:
                self.assertTrue(all('car_id' in sale for sale in data))
            


if __name__ == '__main__':
    unittest.main()
