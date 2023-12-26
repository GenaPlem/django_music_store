from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save()

            return redirect('/')
        else:
            form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
