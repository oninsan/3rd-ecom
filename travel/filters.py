import django_filters
from django import forms
from .models import Place

class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = Place
		fields = {
			'destination':['icontains'],
			'continent':['icontains'],
		}