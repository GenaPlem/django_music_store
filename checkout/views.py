from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
import stripe
from .forms import OrderForm
from .models import Order, OrderLineItem
from bag.context_processors import bag_contents
from django.contrib import messages
from products.models import Product


def checkout_view(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key
    bag = request.session.get('bag', {})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            pid = request.POST.get('payment_intent_id', '')
            order.stripe_pid = pid
            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = None
            order.save()

            for item_id, quantity in bag.items():
                product = Product.objects.get(id=item_id)

                if product.quantity_in_stock >= quantity:
                    product.quantity_in_stock -= quantity
                    product.save()
                else:
                    messages.error(request, f"Not enough {product.name} in stock.")
                    return redirect(reverse('bag'))

                OrderLineItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=product.price
                )

            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "There was an error with your form. Please double check your information.")
    else:
        form = OrderForm()

    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, 'checkout/checkout.html', context)


def checkout_success_view(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! Your order number is {order_number}.')

    context = {
        'order': order,
    }

    if 'bag' in request.session:
        del request.session['bag']

    return render(request, 'checkout/checkout_success.html', context)
