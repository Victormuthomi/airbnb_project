from django.db import models

# Create your models here.

class Service(models.Model):
    """Define the different services offered"""
    name = models.CharField(max_length=50)
    available_areas = models.TextField(default='kisumu')
    
    context_object_name ='all_services_list'
     
    def __str__(self):
        """Show the service name"""
        return self.name



class Customer(models.Model):
    """Define the customer fields"""
    name = models.CharField(max_length=50)
    phone_number = models.PositiveBigIntegerField()
    email = models.EmailField()
    relocate_from  = models.CharField(max_length=50)
    relocate_to = models.CharField(max_length=50)
    booking_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete = models.CASCADE, default = 1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Show the cusomers name"""
        return 'Booking no ' + str(self.booking_id) + ' user ' + self.name + ' booking ' + str(self.service) + ' on '  + self.date.strftime('%d %B %Y %H:%M')
    

        

