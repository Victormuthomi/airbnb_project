from django.contrib import admin

from .models import Airbnb, Customer,  Airbnbimage

# Register your models here.

admin.site.register(Airbnb)
admin.site.register(Customer)
admin.site.register(Airbnbimage)

