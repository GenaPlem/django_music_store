def add_to_bag(request, product_id, quantity=1):
    bag = request.session.get('bag', {})
    bag[str(product_id)] = bag.get(str(product_id), 0) + quantity
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
