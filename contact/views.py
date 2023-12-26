from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact(request):
    form = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save()  # This will save the data to the database
            # Optionally send an email here if required
            return redirect('thank_you')  # Redirect to a 'thank you' page
        else:
            form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
