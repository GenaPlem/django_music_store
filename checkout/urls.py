from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/<order_number>', views.checkout_success_view, name='checkout_success')
]
