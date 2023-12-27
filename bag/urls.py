from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag'),
    path('add/<int:product_id>/', views.add_to_bag_view, name='add_to_bag'),
]
