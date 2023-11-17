import unittest
from flask_testing import TestCase
from app.app import app

class TestIntegration(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_cars_route(self):
        response = self.client.get('/cars')
        self.assert200(response)
        self.assertIn(b'', response.data)

    def test_motos_route(self):
        response = self.client.get('/motos')
        self.assert200(response)
        self.assertIn(b'', response.data)

    def test_sales_route(self):
        response = self.client.get('/sales')
        self.assert200(response)
        self.assertIn(b'', response.data)

if __name__ == '__main__':
    unittest.main()
