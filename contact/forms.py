from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for contact us
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
