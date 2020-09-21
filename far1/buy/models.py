from django.db import models

# Create your models here.
class Buyer(models.Model):
    Name=models.CharField(max_length=20)
    Aadhar_Number=models.BigIntegerField()
    Type=models.CharField(max_length=15)
    Phone_Numbers=models.BigIntegerField()
    UserName=models.CharField(max_length=10)
    Password=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    District=models.CharField(max_length=10)
    Area=models.CharField(max_length=10)
    Email=models.CharField(max_length=30)
    Company_name=models.CharField(max_length=20)
    LNO=models.CharField(max_length=10)
    Company_Reg=models.CharField(max_length=10)


class Bid(models.Model):
    Buyer=models.CharField(max_length=20)
    Farmer=models.CharField(max_length=20)
    Crop=models.CharField(max_length=10)
    Quantity=models.IntegerField()
    Price=models.IntegerField()
    FPhone=models.BigIntegerField(default=0)
    BPhone=models.BigIntegerField(default=0)
