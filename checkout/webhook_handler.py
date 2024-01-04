import json
import time
from django.conf import settings
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
        """Отправка email-подтверждения заказа"""
        from_email = settings.EMAIL_HOST_USER
        subject = render_to_string('email/confirmation_email_subject.txt', {'order': order})
        body = render_to_string('email/confirmation_email_body.txt', {'order': order})
        send_mail(subject, body, from_email, [order.email])

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        pid = intent.id
        bag = json.loads(intent.metadata.bag)

        order_exists = False

        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    stripe_pid=pid,
                    grand_total=intent.amount / 100
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        else:
            try:
                for item_id, quantity in bag.items():
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                        price=product.price
                    )
                    order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
                status=200)

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
