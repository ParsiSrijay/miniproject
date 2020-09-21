
from django.db import models
from django.utils import timezone
# Create your models here.

class Farmer(models.Model):
    Name=models.CharField(max_length=20)
    Aadhar_Number=models.BigIntegerField()
    Phone_Numbers=models.BigIntegerField()
    UserName=models.CharField(max_length=10)
    Password=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=10)
    Area=models.CharField(max_length=10)


class Crop(models.Model):
    Username=models.CharField(max_length=10)
    CropName=models.CharField(max_length=10)
    CropType=models.CharField(max_length=10)
    MinCost=models.IntegerField(default=0)
    Quantity=models.IntegerField()
    Quality=models.ImageField(upload_to='images/')


class Bill(models.Model):
    BuyerName=models.CharField(max_length=20)
    FarmerName=models.CharField(max_length=20)
    Date=models.DateField(default=timezone.now)
    Cost=models.IntegerField()
    Crop=models.CharField(max_length=10)
    FPhone = models.BigIntegerField(default=0)
    BPhone = models.BigIntegerField(default=0)
