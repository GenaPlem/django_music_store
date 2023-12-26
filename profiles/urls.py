from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
    path('shipping_info/', views.shipping_info, name='shipping_info'),
]
