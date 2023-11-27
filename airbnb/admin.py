from django.contrib import admin

from .models import Airbnb, Customer, Booking, Airbnbimage

# Register your models here.

admin.site.register(Airbnb)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Airbnbimage)

