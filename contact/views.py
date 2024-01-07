from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_form = form.save()

            send_mail(
                subject=f"New contact inquiry from {contact_form.name}",
                message=(
                    f"Email: {contact_form.email}\n"
                    f"Subject: {contact_form.subject if contact_form.subject else 'Blank'}\n"
                    f"Name: {contact_form.name}\n"
                    f"Message: {contact_form.message}"
                ),
                from_email=contact_form.email,
                recipient_list=[settings.EMAIL_HOST_USER],
            )

            messages.success(request, 'Your message has been successfully sent.')
            return redirect('/')
        else:
            form = ContactForm()
            messages.error(request, 'Something went wrong.')
    return render(request, 'contact/contact.html', {'form': form})
