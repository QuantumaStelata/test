from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from main.models import Term, Brand, Style

# Create your tests here.


class ApiTests(APITestCase):
    def setUp(self):
        super().setUp()

        self.term = Term.objects.first()
        self.brand = Brand.objects.first()
        self.style = Style.objects.first()

    def test_get_terms(self):
        response = self.client.get(reverse("api:term-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_get_brands(self):
        response = self.client.get(reverse("api:brand-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_styles(self):
        response = self.client.get(reverse("api:style-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_search(self):
        url = reverse("api:search") + f"?s={self.term.slug if self.term else ''}&b={self.brand.slug if self.brand else ''}&st={self.style.slug if self.style else ''}"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, {
            "term_id": self.term.id if self.term else None,
            "brand_id": self.brand.id if self.brand else None,
            "style_id": self.style.id if self.style else None
        })
