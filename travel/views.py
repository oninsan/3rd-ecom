from django.shortcuts import render
import json
import datetime
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from .filters import OrderFilter
from .utils import guestOrder
from django.db.models import Q
from django.shortcuts import render,redirect
from .forms import UserRegisterForm

class home(ListView):
	model = Place
	template_name = 'travel/home.html'
	context_object_name = 'posts'
	extra_context = {'title':'Home'}
	ordering = ['-date']
	paginate_by = 6

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
		return context
		
class DestinationDetail(DetailView):
	model = Place
	extra_context = {'title':'Place Details'}

class SearchView(ListView):
	model = Place
	templat_name = "travel/place_list.html"
	extra_context = {'title':'Home'}
	context_object_name = "posts"
	ordering = ['-date']
	paginate_by = 6
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['filter'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
		return context


def register(request):
	form = UserRegisterForm(request.POST)
	if form.is_valid():
		form.save()
		username = form.cleaned_data.get('username')
		return redirect('travel-sign-in')
	return render(request, 'users/register.html', {"form":form, "title":"Sign up"})

@csrf_exempt
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		booking, created = Booking.objects.get_or_create(customer=customer, complete=False)

		CustomerInfo.objects.create(
			customer = customer,
			booking = booking,
			email = data['customer']['email'],
			full_address = data['customer']['faddress'],
			destination = data['customer']['destination'],
			booking_date = data['customer']['bookingDate'],
			zipcode = data['customer']['zipcode']
			)
			
	else:
		customer, booking = guestOrder(request ,data)

		CustomerInfo.objects.create(
			customer = customer,
			booking = booking,
			email = data['customer']['email'],
			full_address = data['customer']['faddress'],
			destination = data['customer']['destination'],
			booking_date = data['customer']['bookingDate'],
			zipcode = data['customer']['zipcode']
			)

	booking.transaction_id = transaction_id

	
	booking.save()
	return JsonResponse('Payment completed..', safe=False)