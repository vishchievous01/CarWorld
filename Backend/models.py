from django.db import models


# Create your models here.
class CategoryDB(models.Model):
    CategoryName = models.CharField(max_length=100, null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    CategoryImage = models.ImageField(upload_to="Category Images", null=True, blank=True)

class ProductDB(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    ProductImage = models.ImageField(upload_to="Product Images", null=True, blank=True)
