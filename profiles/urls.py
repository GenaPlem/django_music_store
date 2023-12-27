from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path('orders/', views.orders_view, name='orders'),
    path('shipping_info/', views.shipping_info_view, name='shipping_info'),
]
