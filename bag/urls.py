from django.urls import path
from . import views

urlpatterns = [
    path('', views.bag_view, name='bag'),
    path('add/<int:product_id>/', views.add_to_bag_view, name='add_to_bag'),
    path('remove/<int:product_id>/', views.remove_from_bag_view, name='remove_from_bag')
]
