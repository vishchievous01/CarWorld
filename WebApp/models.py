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
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductID = models.IntegerField(null=True, blank=True)
    Carname = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=250, null=True, blank=True)

class OrderDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)