from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'created', 'stripe_pid', 'paid')
    fields = ('order_number', 'user', 'full_name', 'email', 'phone_number',
              'address1', 'address2', 'city', 'county', 'postal_code',
              'created', 'stripe_pid', 'paid')
    list_display = ('order_number', 'full_name', 'email', 'created', 'paid')
    search_fields = ('order_number', 'full_name', 'email')
    list_filter = ('created', 'paid')


admin.site.register(Order, OrderAdmin)
