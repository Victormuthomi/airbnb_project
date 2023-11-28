from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
     """Initialize the fields for the customer template"""
     class Meta:
          model = Customer
          fields = ['name', 'email', 'phone_number', 'airbnb']