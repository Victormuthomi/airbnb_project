from django.shortcuts import render, redirect

from django.views.generic import ListView

from .models import Service,Customer

from .forms import MoversCustomerForm

# Create your views here.


class ServiceListView(ListView):
    """Define the model and the template to use for the airbnbs"""
    model = Service
    template_name = 'movers_service.html'
    context_object_name = 'all_services_list'


class CustomerListView(ListView):
    """Define the model and temlate to use for the customers"""
    model = Customer 
    template_name = 'movers_customer.html'

def m_customer_create_view(request):
    if request.method == 'POST':
        form = MoversCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booked')
    else:
        form = MoversCustomerForm()

    return render(request, 'movers_customer_form.html', {'form' : form})


