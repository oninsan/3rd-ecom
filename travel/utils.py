from .models import *
import json

def guestOrder(request, data):
	print('Unauthenticated user..')

	first_name = data['form']['fname']
	last_name = data['form']['lname']

	customer, created = Customer.objects.get_or_create(first_name=first_name, last_name=last_name)
	customer.first_name = first_name
	customer.last_name = last_name
	customer.save()

	booking = Booking.objects.create(customer=customer, complete=False)
	return customer, booking