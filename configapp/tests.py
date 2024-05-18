from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import *


class APITests(APITestCase):

    def setUp(self):
        self.home_url = reverse('home-list')
        self.shop_url = reverse('shop-list')
        self.product_url = reverse('product-list')
        self.contact_url = reverse('contactus-list')

    def test_create_home(self):
        data = {"title": "Home Page", "description": "Welcome to the home page"}
        response = self.client.post(self.home_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, "Home Page")


class ModelTests(TestCase):

    def test_create_product(self):
        shop = Shop.objects.create(name="Shop Name", location="Shop Location")
        product = Product.objects.create(shop=shop, name="Product Name", price=10.00)
        self.assertEqual(product.name, "Product Name")
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.shop, shop)

    def test_create_contact_us(self):
        contact = Contact.objects.create(name="Contact Name", email="shahzod@example.com", message="Helloworld")
        self.assertEqual(contact.name, "Contact Name")
        self.assertEqual(contact.email, "shahzod@example.com")
        self.assertEqual(contact.message, "Helloworld")
