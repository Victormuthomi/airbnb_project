from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from .models import Airbnb, Booking, Customer

# Create your views here.

class HomeListView(TemplateView):
    """Define the template to use for the homepage"""
    template_name = 'home.html'


class AirbnbListView(ListView):
    """Define the model and the template to use for the airbnbs"""
    model = Airbnb
    template_name = 'airbnb.html'

class BookingListView(ListView):
    """Define the model and temlate to use for the bookings"""
    model = Booking
    template_name = 'airbnb_booking.html'

class CustomerListView(ListView):
    """Define the model and temlate to use for the customers"""
    model = Customer 
    template_name = 'airbnb_customer.html'


