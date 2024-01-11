from django.shortcuts import get_object_or_404
from products.models import Product


def add_to_bag(request, product_id, quantity=1):
    """
    Function to add products to the bag
    """
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=product_id)

    if quantity > product.quantity_in_stock:
        return False
    else:
        bag[str(product_id)] = min(bag.get(str(product_id), 0) + quantity, product.quantity_in_stock)
        request.session['bag'] = bag
        return True


def remove_from_bag(request, product_id):
    """
    Function to remove products from the bag
    """
    bag = request.session.get('bag', {})
    bag.pop(str(product_id), None)
    request.session['bag'] = bag


def update_bag(request, product_id, quantity):
    """
    Function to update products quantity in the bag
    """
    bag = request.session.get('bag', {})
    product = get_object_or_404(Product, pk=product_id)

    if quantity > product.quantity_in_stock:
        return False
    else:
        bag[str(product_id)] = quantity
        request.session['bag'] = bag
        return True
