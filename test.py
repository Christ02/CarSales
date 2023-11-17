import unittest
from flask import Flask
from flask_testing import TestCase
from app import app


class TestFlaskApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)

    def test_cars_route(self):
        response = self.client.get('/cars')
        self.assert200(response)

    def test_create_car_route(self):
        response = self.client.post('/create_car', data=dict(
        make='TestMake',
        model='TestModel',
        year='2022',
        color='TestColor',
        vehicle_type='TestVehicleType',
        mileage='10000',
        transmission='TestTransmission',
        engine='TestEngine',
        fuel_type='TestFuelType'
    ), follow_redirects=True)
        
        print(response.data)



if __name__ == '__main__':
    unittest.main()
