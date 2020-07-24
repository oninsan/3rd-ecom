from django.urls import path
from .views import *

urlpatterns = [
	path('dashboard-users/', DashboardUsers.as_view(), name="travel-dashboard-users"),
	path('dashboard-customers/', DashboardCustomers.as_view(), name="travel-dashboard-customers"),
	path('dashboard-bookings/', DashboardBookings.as_view(), name="travel-dashboard-bookings"),
	path('dashboard-customer-infos/',DashboardCustomerInfos.as_view(), name="travel-dashboard-customer-infos"),
	path('dashboard-places/', DashboardPlaces.as_view(), name="travel-dashboard-places"),
]