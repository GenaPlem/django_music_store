from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from products.models import Product
from .models import WishlistItem


def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    already_in_wishlist = WishlistItem.objects.filter(user=request.user, product=product).exists()

    if not already_in_wishlist:
        WishlistItem.objects.create(user=request.user, product=product)
        messages.success(request, f'Added {product.name} to your wishlist!')
    else:
        messages.error(request, f'{product.name} is already in your wishlist.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'wishlist'))


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    WishlistItem.objects.filter(user=request.user, product=product).delete()
    messages.success(request, f'{product.name} has been removed from your wishlist.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'wishlist'))
