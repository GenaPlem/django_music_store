from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'date_subscribed', 'date_unsubscribed')
    list_filter = ('is_subscribed',)
    search_fields = ('email',)
    ordering = ('-date_subscribed',)
