from django.db import models
from customer.models import Customer

# Create your models here.



class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class AddProduct(models.Model):
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customers/')



class Purchase(models.Model):
    product = models.ForeignKey(AddProduct, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)