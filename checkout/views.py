from django.shortcuts import render, redirect
from .forms import OrderForm


def checkout_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('bag')
    else:
        form = OrderForm()

    return render(request, 'checkout/checkout.html', {'form': form})
