import django_filters
from django import forms
from .models import Place

class OrderFilter(django_filters.FilterSet):
	# name = django_filters.CharFilter(lookup_expr='iexact')
	class Meta:
		model = Place
		fields = {
			'destination':['icontains'],
			'continent':['icontains'],
		}

	 # class Meta:
  #       model = Place
  #       fields = ['destination', 'continent']