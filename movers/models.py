from django.db import models

# Create your models here.

class Services(models.Model):
    """Define the different services offered"""
    name = models.CharField(max_length=50)


class Customer(models.Model):
    """Define the customer fields"""
    name = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField()
    relocate_from  = models.CharField(max_length=50)
    relocate_to = models.CharField(max_length=50)

    def __str__(self):
        """Show the cusomers name"""
        return self.name
    
class Booking(models.Model):
    """Define the fields for the booking"""
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return  'Booking no ' + str(self.booking_id) + ' on ' + self.date.strftime('%d %B %Y %H:%M')


