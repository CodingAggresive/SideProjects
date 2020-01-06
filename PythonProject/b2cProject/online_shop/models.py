from django.db import models

# Create your models here.
from django.conf import settings  #????
from django.db import models
from django.utils import timezone

class User(models.Model):
    UserName = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=100)
    MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    CellPhoneNumber = models.CharField(max_length=50)
    CreateDate = models.DateTimeField(default = timezone.now)
    Balance = models.DecimalField(max_digits=20,decimal_places=2)
    


class Order(models.Model):
    ItemId = models.IntegerField(max_length=12)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=20,decimal_places=2)
    Quality = models.DecimalField(max_digits=20,decimal_places=2)
    Buyer = models.CharField(max_length=12)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    CreateDate = models.DateTimeField(default = timezone.now)


class Item(models.Model):
    EnglishName = models.CharField(max_length=200)
    ChineseName = models.CharField(max_length=200)
    MarketPrice = models.DecimalField(max_digits=20,decimal_places=2)
    MarketDate = models.DateTimeField(default = timezone.now)
    CreateDate = models.DateTimeField(default = timezone.now)
    Seller = models.CharField(max_length=12)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)