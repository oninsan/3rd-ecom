from .models import *
import json

def guestOrder(request, data):
	user = data['form']['user']
	first_name = data['form']['fname']
	last_name = data['form']['lname']

	customer, created = Customer.objects.get_or_create(user=user, first_name=first_name, last_name=last_name)
	customer.user = user
	customer.first_name = first_name
	customer.last_name = last_name
	customer.save()

	if request.user.is_authenticated:
		booking = Booking.objects.get_or_create(customer=customer, complete=False)
	else:
		booking = Booking.objects.create(customer=customer, complete=False)
	
	return customer, booking