from django.urls import path
from .views import home_view, newsletter_subscribe, privacy_policy_view

urlpatterns = [
    path('', home_view, name='home'),
    path('newsletter_subscribe/', newsletter_subscribe, name='newsletter_subscribe'),
    path('privacy_policy/', privacy_policy_view, name='privacy_policy'),
]
