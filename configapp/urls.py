from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeListCreateView.as_view(), name='home-list'),
    path('shops/', ShopListCreateView.as_view(), name='shop-list-create'),
    path('shops/<int:pk>/', ShopDetailView.as_view(), name='shop-detail'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
]
