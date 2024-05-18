from rest_framework import generics
from rest_framework.response import Response
from .models import Product, Shop, Contact
from .serializers import ProductSerializer, ShopSerializer, ContactSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# HOME
class HomeListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category"]
    search_fields = ['name', 'description']


# PRODUCTS
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# SHOPS
class ShopListCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# CONTACTS
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


