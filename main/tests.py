from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus as status

# Create your tests here.


class MainTests(TestCase):
    def test_main_page(self):
        response = self.client.get(reverse("main:main"))

        self.assertEqual(response.status_code, status.OK)
