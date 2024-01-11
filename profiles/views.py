from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from checkout.models import Order


@login_required
def profile_view(request):
    """
    View to render profile template
    """
    return render(request, 'profiles/profile.html')


@login_required
def orders_view(request):
    """
    View to render orders list in profile
    """
    orders = Order.objects.filter(user=request.user).order_by('-created')

    context = {
        'orders': orders,
    }

    return render(request, 'profiles/orders.html', context)


@login_required
def shipping_info_view(request):
    """
    View to render shipping info in profile
    """
    return render(request, 'profiles/shipping_info.html')
