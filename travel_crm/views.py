from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.views.generic import ListView
from travel.models import *


# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class DashboardUsers(ListView):
	model = Customer
	template_name = 'travel_crm/dashboard-users.html'
	context_object_name = 'posts'
	extra_context = {
		'title':'Users',
		'users':User.objects.all()
	}

@method_decorator(staff_member_required, name='dispatch')
class DashboardCustomers(ListView):
	model = Customer
	template_name = 'travel_crm/dashboard-customers.html'
	context_object_name = 'customers'
	extra_context = {
		'title':'Customers'
	}

@method_decorator(staff_member_required, name='dispatch')
class DashboardBookings(ListView):
	model = Booking
	template_name = 'travel_crm/dashboard-bookings.html'
	context_object_name = 'bookings'
	extra_context = {
		'title':'Bookings'
	}

@method_decorator(staff_member_required, name='dispatch')
class DashboardCustomerInfos(ListView):
	model = CustomerInfo
	template_name = 'travel_crm/dashboard-customer-infos.html'
	context_object_name = 'customerinfos'
	extra_context = {
		'title':'Customer Infos'
	}

@method_decorator(staff_member_required, name='dispatch')
class DashboardPlaces(ListView):
	model = Place
	template_name = 'travel_crm/dashboard-places.html'
	context_object_name = 'places'
	extra_context = {
		'title':'Places'
	}