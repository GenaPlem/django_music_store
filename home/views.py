from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from home.forms import NewsletterForm
from home.models import NewsletterSubscriber
from products.models import Product
from wishlist.models import WishlistItem


def home_view(request):
    """ A view to return the home page """
    top_products = Product.objects.filter(is_top_product=True)[:6]

    if request.user.is_authenticated:
        wishlist_product_ids = WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        wishlist_product_ids = []

    context = {
        'top_products': top_products,
        'wishlist_product_ids': wishlist_product_ids
    }

    return render(request, 'home/index.html', context)


def newsletter_subscribe(request):
    """
    View to handle newsletter subscribe
    """
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
            else:
                messages.error(request, 'This email already subscribed')
                return redirect('home')

            message = (
                "Hello!\n\n"
                "We're excited to let you know that you've successfully subscribed to our newsletter. "
                "Now you'll be among the first to hear about our latest news, special offers, and exclusive events. "
                "We promise to bring you valuable content that's both informative and enjoyable.\n\n"
                "Thank you for joining our community, and welcome aboard!\n\n"
                "Best regards,\n"
                "The M-TUNE Team"
            )

            send_mail(
                'Subscription Confirmation',
                message,
                settings.DEFAULT_FROM_EMAIL,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            messages.success(request, 'Subscribed successfully')
            return redirect('home')

        else:
            form = NewsletterForm()
            messages.error(request, 'Invalid email')
            return redirect('home')

    return render(request, 'home/index.html', {'form': form})


def privacy_policy_view(request):
    """
    View to render privacy policy template
    """
    return render(request, 'privacy_policy.html')
