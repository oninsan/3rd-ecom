from django.urls import path
from django.contrib.auth import views as auth_views
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
    path('search/', SearchView.as_view(), name="travel-search"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='travel/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='travel/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='travel/password_reset_done.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='travel/password_reset_complete.html'), name='password_reset_complete'),
]