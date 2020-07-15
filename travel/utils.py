from .models import *
import json

def cookieCart(request):
	try:
		booking = json.loads(request.COOKIES['booking'])
	except:
		booking = {}
	print('Booking:', booking)
	items = []
	order = {
		'get_cart_total':0,
		'get_cart_items':0,
		'shipping':True
	}
	cartItems = order['get_cart_items']

	for i in booking:
		try:
			cartItems += booking[i]['quantity']

			place = Place.objects.get(id=i)
			total = (place.booking_price * booking[i]['quantity'])

			item = {
				'place':{
					'id':place.id,
					'title':place.title,
					'price':place.price,
					'imgURL':place.imgURL
				},
				'quantity':booking[i]['quantity'],
				'get_total':total
			}
			items.append(item)
		except:
			pass

	return {'cartItems':cartItems, 'Booking':booking, 'items':items}

def cartData(request):
	if request.user.is_authenticated:
		customer = request.user.customer
		booking, created = Order.objects.get_or_create(customer=customer, complete=False)
		# items = booking.bookingplace_set.all()
		cartItems = booking.get_cart_items
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		booking = cookieData['booking']
		items = cookieData['items']

	return {'cartItems':cartItems, 'order':order, 'items':items}


def guestOrder(request, data):
	print('Unauthenticated user..')
	print('COOKIES:', request.COOKIES)

	first_name = data['form']['fname']
	last_name = data['form']['lname']

	cookieData = cookieCart(request)
	items = cookieData['items']

	customer, created = Customer.objects.get_or_create(first_name=first_name, last_name=last_name)
	customer.first_name = first_name
	customer.last_name = last_name
	customer.save()

	booking = Booking.objects.create(customer=customer, complete=False)
	return customer, booking