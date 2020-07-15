from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Place(models.Model):
	destination = models.CharField(max_length=100)
	booking_price = models.DecimalField(default=10, decimal_places=2, max_digits=7)
	description = models.TextField(default="", null=True)
	img = models.ImageField(null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.destination

	@property
	def imgURL(self):
		try:
			url = self.img.url
		except:
			url = ''
		return url

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	

	def __str__(self):
		return self.first_name

class Booking(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	date_booked = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False, null=True, blank=True)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class CustomerInfo(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
	booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, blank=True, null=True)
	full_address = models.CharField(max_length=100, null=True)
	destination = models.CharField(max_length=100, null=True)
	email = models.CharField(max_length=100, null=True)
	zipcode = models.CharField(max_length=100, null=True)
	booking_date = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.full_address)
