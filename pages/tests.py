from django.test import TestCase
from django.test import SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_lara_page_status_code(self):
        response = self.client.get('/lara/')
        self.assertEqual(response.status_code, 200)

    def test_marcos_page_status_code(self):
        response = self.client.get('/marcos/')
        self.assertEqual(response.status_code, 200)

    def test_helena_page_status_code(self):
        response = self.client.get('/helena/')
        self.assertEqual(response.status_code, 200)
