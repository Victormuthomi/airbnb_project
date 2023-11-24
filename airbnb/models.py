from django.db import models

# Create your models here.

class Airbnb(models.Model):
    """Define the fields for the airbnb"""
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    rooms = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    avalability = models.BooleanField(default=True)
    services = models.TextField()

class Customer(models.Model):
     """Define the fields for the customers"""
     name = models.CharField(max_length=20)
     email = models.EmailField()
     phone_number = models.PositiveSmallIntegerField()
     
class Booking(models.Model):
     """Define the booking fields"""
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     date = models.TimeField(auto_now_add=True)



