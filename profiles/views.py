from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    return render(request, 'profiles/profile.html')


@login_required
def orders(request):
    return render(request, 'profiles/orders.html')


@login_required
def shipping_info(request):
    return render(request, 'profiles/shipping_info.html')
