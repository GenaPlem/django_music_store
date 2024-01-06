from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from home.forms import NewsletterForm
from home.models import NewsletterSubscriber
from products.models import Product
from wishlist.models import WishlistItem


def home_view(request):
    """ A view to return the index page """
    top_products = Product.objects.filter(is_top_product=True)[:6]

    if request.user.is_authenticated:
        # Получаем список идентификаторов продуктов из списка желаний пользователя
        wishlist_product_ids = WishlistItem.objects.filter(user=request.user).values_list('product_id', flat=True)
    else:
        wishlist_product_ids = []

    context = {
        'top_products': top_products,
        'wishlist_product_ids': wishlist_product_ids
    }

    return render(request, 'home/index.html', context)


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)

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
                settings.EMAIL_HOST_USER,
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            return redirect('home')
        else:
            form = NewsletterForm()
    return render(request, 'home', {'form': form})
