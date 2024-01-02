from django.shortcuts import get_object_or_404
from products.models import Product


def add_to_bag(request, product_id, quantity=1):
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=product_id)

    current_quantity = bag.get(str(product_id), 0)
    new_quantity = current_quantity + quantity

    if new_quantity > product.quantity_in_stock:
        bag[str(product_id)] = product.quantity_in_stock
    else:
        bag[str(product_id)] = new_quantity

    request.session['bag'] = bag


def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})
    bag.pop(str(product_id), None)
    request.session['bag'] = bag


def update_bag(request, product_id, quantity):
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[str(product_id)] = quantity
    else:
        remove_from_bag(request, product_id)
    request.session['bag'] = bag
