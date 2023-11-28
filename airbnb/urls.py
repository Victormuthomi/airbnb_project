from django.urls import path 

from .views import AirbnbListView, HomeListView, CustomerListView, customer_create_view, BookedListView

urlpatterns =[
    path('', HomeListView.as_view(), name ='home'),
    path('airbnb/', AirbnbListView.as_view(), name= 'airbnb'),
    path('airbnb_customer/', CustomerListView.as_view(), name = 'airbnb_customer'),
    path('airbnb_customer_form/', customer_create_view, name = 'airbnb_customer_form'),
    path('booked/', BookedListView.as_view(), name='booked'),


]

