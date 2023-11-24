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

    def __str__(self):
          """Print the name of the airbnb """
          return self.name

class Customer(models.Model):
     """Define the fields for the customers"""
     name = models.CharField(max_length=20)
     email = models.EmailField()
     phone_number = models.PositiveIntegerField()

     def __str__(self):
          """Print the name of the customer"""
          return self.name
     
class Booking(models.Model):
     """Define the booking fields"""
     booking_id= models.AutoField(primary_key=True)
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     airbnb = models.ForeignKey(Airbnb, on_delete=models.CASCADE, default=1)
     date = models.DateTimeField(auto_now=True)
     
     
     def __str__(self):
        return  'Booking no ' + str(self.booking_id) + ' on ' + self.date.strftime('%d %B %Y %H:%M')


    
          

     



