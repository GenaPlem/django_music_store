from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from home.forms import NewsletterForm
from home.models import NewsletterSubscriber
from products.models import Product


def home_view(request):
    """ A view to return the index page """
    top_products = Product.objects.filter(is_top_product=True)[:6]
    return render(request, 'home/index.html', {'top_products': top_products})


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
            send_mail(
                'Subscription Confirmation',
                'Thank you for subscribing to our newsletter!',
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('home')
        else:
            form = NewsletterForm()
    return render(request, 'home', {'form': form})
