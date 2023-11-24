from django.contrib import admin

from .models import Airbnb, Customer, Booking

# Register your models here.

admin.site.register(Airbnb)
admin.site.register(Customer)
admin.site.register(Booking)

