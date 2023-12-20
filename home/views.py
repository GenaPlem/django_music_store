from django.shortcuts import render
from products.models import Product


def home(request):
    """ A view to return the index page """
    top_products = Product.objects.filter(is_top_product=True)
    return render(request, 'home/index.html', {'top_products': top_products})
