from django.shortcuts import render, redirect, reverse, get_object_or_404
from bag.context_processors import bag_contents
from products.models import Product
from .forms import OrderForm
from .models import OrderLineItem, Order


def checkout_view(request):
    bag = request.session.get('bag', {})
    if not bag:
        # Redirect to bag page if bag is empty
        return redirect('bag')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            bag = bag_contents(request)
            order.total = bag['total']
            order.delivery = bag['delivery']
            order.grand_total = bag['grand_total']

            if request.user.is_authenticated:
                order.user = request.user

            order.save()

            for item in bag['bag_items']:
                product_id = int(item['item_id'])
                quantity = item['quantity']
                product = Product.objects.get(id=product_id)
                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    price=product.price,
                    quantity=quantity
                )

            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        form = OrderForm()

    return render(request, 'checkout/checkout.html', {'form': form})


def checkout_success_view(request, order_number):
    """
    Handle successful checkouts
    """
    order = get_object_or_404(Order, order_number=order_number)

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
