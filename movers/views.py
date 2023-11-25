from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import Service, Booking, Customer

# Create your views here.

#class HomeListView(TemplateView):
    #"""Define the template to use for the homepage"""
   # template_name = 'home.html'


class ServiceListView(ListView):
    """Define the model and the template to use for the airbnbs"""
    model = Service
    template_name = 'movers_service.html'

class BookingListView(ListView):
    """Define the model and temlate to use for the bookings"""
    model = Booking
    template_name = 'movers_booking.html'

class CustomerListView(ListView):
    """Define the model and temlate to use for the customers"""
    model = Customer 
    template_name = 'movers_customer.html'


