from django.urls import path
from .views import (
	home,
	DestinationDetail,
	SearchView,
	processOrder
)

urlpatterns = [
    path('',home.as_view() , name='travel-home'),
    path('destination/<int:pk>/', DestinationDetail.as_view(), name="destination-detail"),
    path('process_order/', processOrder, name='process-order'),
    path('search/', SearchView.as_view(), name="travel-search")
]