from django.contrib import admin

from .models import Service, Customer, Booking

# Register your models here.

admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Booking)
