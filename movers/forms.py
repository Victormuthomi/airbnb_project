from django import forms 

from .models import Customer

class MoversCustomerForm(forms.ModelForm):
    """Define the model and fields to be displayed by the form"""
    class Meta:
        model = Customer
        fields = [ 'name', 'email', 'phone_number', 'service', 'relocate_from', 'relocate_to',]