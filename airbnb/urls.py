from django.urls import path 

from .views import AirbnbListView, HomeListView, BookingListView, CustomerListView

urlpatterns =[
    path('', HomeListView.as_view(), name ='home'),
    path('airbnb/', AirbnbListView.as_view(), name= 'airbnb'),
    path('airbnb_booking/', BookingListView.as_view(), name='airbnb_booking'),
    path('airbnb_customer/', CustomerListView.as_view(), name = 'airbnb_ustomer')


]

