import uuid
from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='orders')
    order_number = models.CharField(max_length=32, unique=True, editable=False)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=80, null=False, blank=False)
    postal_code = models.CharField(max_length=20)
    delivery = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    @staticmethod
    def _generate_order_number():
        """
        Generate a unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = Order._generate_order_number()
        super().save(*args, **kwargs)

    def update_total(self):
        """
        Update the order total by aggregating the prices of the line items.
        This should also include the delivery cost if applicable.
        """
        self.total = sum(lineitem.lineitem_total for lineitem in self.items.all())
        # Include any additional calculations for delivery, etc.
        if self.total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery = settings.STANDARD_DELIVERY_PRICE
        else:
            self.delivery = 0

        self.grand_total = self.total + self.delivery
        self.save()

    def __str__(self):
        return f'Order {self.order_number}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    lineitem_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        if self.product.discount_percentage:
            discount = (self.product.price * self.product.discount_percentage / 100)
            discounted_price = self.product.price - discount
            self.price = discounted_price
            self.lineitem_total = discounted_price * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} - Order: {self.order.order_number} - Product: {self.product.name}'
