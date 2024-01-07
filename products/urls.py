from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products_view, name='products'),
    path('<slug:category_slug>/', views.all_products_view, name='products_by_category'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    path('product/add', views.add_product, name='add_product'),
    path('product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
]
