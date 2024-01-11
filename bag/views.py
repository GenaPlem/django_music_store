from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from products.models import Product
from .utils import add_to_bag, remove_from_bag, update_bag


def bag_view(request):
    """
    View to render bag template
    """
    return render(request, 'bag/bag.html')


def add_to_bag_view(request, product_id):
    """
    View to add product to the bag
    """
    quantity = int(request.POST.get('quantity', 1))
    product = get_object_or_404(Product, pk=product_id)
    success = add_to_bag(request, product.id, quantity)

    if success:
        messages.success(request, f'{product.name} added to your bag!')
    else:
        messages.warning(request,
                         f'There is only {product.quantity_in_stock} {product.name} in stock. You can\'t add more.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))


def remove_from_bag_view(request, product_id):
    """
    View to remove product from the bag
    """
    product = get_object_or_404(Product, pk=product_id)
    remove_from_bag(request, product_id)
    messages.success(request, f'{product.name} removed from your bag!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))


def update_bag_view(request, product_id):
    """
    View to update products quantity in the bag
    """
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    success = update_bag(request, product_id, quantity)

    if success:
        messages.success(request, f'{product.name} quantity updated in your bag!')
    else:
        messages.warning(request,
                         f'There is only {product.quantity_in_stock} {product.name} in stock. You can\'t add more.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'bag_view'))
