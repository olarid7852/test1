from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Car

class CarAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/cars/'

    def test_list_cars(self):
        # Create some cars
        Car.objects.create(make='Toyota', model='Corolla', production_date='2020-01-01', color='Silver', price=20000)
        Car.objects.create(make='Honda', model='Civic', production_date='2019-06-01', color='Black', price=25000)

        # Get the list of cars
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_car(self):
        # Create a new car
        data = {'make': 'Ford', 'model': 'Mustang', 'production_date': '2020-06-01', 'color': 'Red', 'price': 30000}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Car.objects.count(), 1)

    def test_retrieve_car(self):
        # Create a car
        car = Car.objects.create(make='Toyota', model='Camry', production_date='2018-01-01', color='Gold', price=22000)

        # Get the car
        response = self.client.get(f'{self.url}{car.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['make'], 'Toyota')

    def test_update_car(self):
        # Create a car
        car = Car.objects.create(make='Honda', model='Accord', production_date='2019-01-01', color='Blue', price=28000)

        # Update the car
        data = {'make': 'Honda', 'model': 'Accord', 'production_date': '2019-01-01', 'color': 'Red', 'price': 29000}
        response = self.client.put(f'{self.url}{car.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        car.refresh_from_db()
        self.assertEqual(car.color, 'Red')

    def test_delete_car(self):
        # Create a car
        car = Car.objects.create(make='Ford', model='Fusion', production_date='2018-06-01', color='Silver', price=24000)

        # Delete the car
        response = self.client.delete(f'{self.url}{car.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Car.objects.count(), 0)