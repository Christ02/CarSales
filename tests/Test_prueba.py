'''# test_integration.py
import unittest
from app.app import app

class TestIntegration(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_cars_route(self):
        response = self.app.get('/cars')
        self.assertEqual(response.status_code, 200)

    def test_motos_route(self):
        response = self.app.get('/motos')
        self.assertEqual(response.status_code, 200)

    def test_sales_route(self):
        response = self.app.get('/sales')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
'''