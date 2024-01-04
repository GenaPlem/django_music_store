from django.urls import path
from .views import home_view, newsletter_subscribe

urlpatterns = [
    path('', home_view, name='home'),
    path('newsletter_subscribe/', newsletter_subscribe, name='newsletter_subscribe'),
]
