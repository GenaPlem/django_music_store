import json
import time
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from .models import Order, OrderLineItem
from products.models import Product


class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def _send_confirmation_email(self, order):
        from_email = settings.EMAIL_HOST_USER
        subject = render_to_string('checkout/email/confirmation_email_subject.txt', {'order': order})
        body = render_to_string('checkout/email/confirmation_email_body.txt', {'order': order})
        send_mail(subject, body, from_email, [order.email])

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        # username = intent.metadata.get('username', 'AnonymousUser')

        # user = None
        # if username != 'AnonymousUser':
        #     try:
        #         user = User.objects.get(username=username)
        #     except User.DoesNotExist:
        #         user = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(stripe_pid=pid, grand_total=intent.amount / 100)
                order_exists = True
                order.paid = True
                # order.user = user
                order.save()
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if not order_exists:
            try:
                order = Order.objects.create(
                    # user=user,
                    full_name=intent.billing_details.name,
                    email=intent.billing_details.email,
                    phone_number=intent.billing_details.phone,
                    address1=intent.billing_details.address.line1,
                    address2=intent.billing_details.address.line2,
                    city=intent.billing_details.address.city,
                    county=intent.billing_details.address.state,
                    postal_code=intent.billing_details.address.postal_code,
                    delivery=settings.STANDARD_DELIVERY_PRICE,
                    total=intent.amount / 100 - settings.STANDARD_DELIVERY_PRICE,
                    grand_total=intent.amount / 100,
                    stripe_pid=pid,
                    paid=True
                )

                # for item_id, quantity in bag.items():
                #     product = Product.objects.get(id=item_id)
                #     order_line_item = OrderLineItem(
                #         order=order,
                #         product=product,
                #         quantity=quantity,
                #         price=product.price
                #     )
                #     order_line_item.save()
            except Exception as e:
                # if order:
                #     order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
