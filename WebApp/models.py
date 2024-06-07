from django.db import models


# Create your models here.
class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Message = models.TextField(null=True, blank=True)


class RegisterDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)


class WishlistDB(models.Model):
    ProductID = models.IntegerField(null=True, blank=True)
    Carname = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=250, null=True, blank=True)
