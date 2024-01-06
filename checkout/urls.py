from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('success/<order_number>', views.checkout_success_view, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
