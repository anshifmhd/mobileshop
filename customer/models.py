from django.db import models

# Create your models here.



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)



class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)



