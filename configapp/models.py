from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
