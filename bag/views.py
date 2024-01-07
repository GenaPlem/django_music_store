from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from products.models import Product
from .utils import add_to_bag, remove_from_bag, update_bag


def bag_view(request):
    return render(request, 'bag/bag.html')


def add_to_bag_view(request, product_id):
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, pk=product_id)
    add_to_bag(request, product.id, quantity)
    messages.success(request, f'{product.name} added to your bag!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))


def remove_from_bag_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    remove_from_bag(request, product_id)
    messages.success(request, f'{product.name} removed from your bag!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))


def update_bag_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    update_bag(request, product_id, quantity)
    messages.success(request, f'{product.name} quantity updated in your bag!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))
