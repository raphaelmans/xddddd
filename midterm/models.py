from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birthdate = models.DateField()
    mobile_number = models.CharField(max_length=25)

class DVD(models.Model):
    dvd_id = models.AutoField(primary_key=True)
    genre = models.CharField(max_length=25)
    title = models.CharField(max_length=25)
    release_year = models.DateField()

class Rent(models.Model):
    customer= models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    dvd= models.ForeignKey(DVD, on_delete=models.DO_NOTHING)