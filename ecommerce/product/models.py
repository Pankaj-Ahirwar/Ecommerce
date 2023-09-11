from django.db import models
from django.contrib.auth.models import User
from .managers import MYManager

# Create your models here.

class SoapItem(models.Model):
    name=models.CharField(max_length=40)
    cat=models.CharField(max_length=40)
    image=models.ImageField(upload_to="Soap_image")
    price=models.FloatField()
    Quantity=models.IntegerField()
    Available=models.BooleanField(default=True)
    desc=models.TextField(default='')

    #objects = models.Manager() #BY DEFAULT #YE LETA H ,BUT APAN NE MANAGER BANAYA H TO ISKO 
                                #LENA PDEGA
class SurfItem(models.Model):
    name=models.CharField(max_length=40)
    cat=models.CharField(max_length=40)
    image=models.ImageField(upload_to="Soap_image")
    price=models.FloatField()
    Quantity=models.IntegerField()
    Available=models.BooleanField(default=True)
    desc=models.TextField(default='')

