from django.urls import path 

from .views import ServiceListView, CustomerListView, BookingListView

urlpatterns =[
    path('movers_service/', ServiceListView.as_view(), name= 'movers_service'),
    path('movers_booking/', BookingListView.as_view(), name='movers_booking'),
    path('movers_customer/', CustomerListView.as_view(), name = 'movers_customer')
]

