from django.db import models

# Create your models here.
#????
from django.conf import settings  
from django.db import models
from django.utils import timezone

class User(models.Model):
    UserName = models.CharField(max_length=200,default='')
    FirstName = models.CharField(max_length=100,default ='')
    '''MiddleName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    CellPhoneNumber = models.CharField(max_length=50)
    CreateDate = models.DateTimeField(default = timezone.now)
    Balance = models.DecimalField(max_digits=20,decimal_places=2)'''
    
    def __init__(self,user=User()):
         self.user = user

    def get_userinfo_by_id(self,id):
        self.user.objects.get(id = id)
        print(user)

    def add_user(self,user=User()):
        self.user.objects.add(User(){})
    
    def delete_user(self,id):
        

    def __str__(self):
        return self.UserName

    
        
        
    

class Item(models.Model):
    EnglishName = models.CharField(max_length=200,blank=True)
    '''ChineseName = models.CharField(max_length=200,blank=True)
    MarketPrice = models.DecimalField(max_digits=20,decimal_places=2,blank=True)
    MarketDate = models.DateTimeField(default = timezone.now,blank=True)
    CreateDate = models.DateTimeField(default = timezone.now,blank=True)
    Seller = models.ForeignKey(User,on_delete=models.DO_NOTHING,blank=True)'''


    
class Order(models.Model):
    #ItemId = models.ForeignKey(Item,on_delete=models.DO_NOTHING)
    Amount = models.DecimalField(max_digits=20,decimal_places=2,default=0.0)
    '''Quality = models.DecimalField(max_digits=20,decimal_places=2)
    Buyer = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    CreateDate = models.DateTimeField(default = timezone.now)'''
