from django.urls import path 

from .views import ServiceListView, CustomerListView, m_customer_create_view

urlpatterns =[
    path('movers_service/', ServiceListView.as_view(), name= 'movers_service'),
    path('movers_customer/', CustomerListView.as_view(), name = 'movers_customer'),
    path('movers_customer_form/', m_customer_create_view, name= 'movers_customer_form'),

]

