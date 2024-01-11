from django import forms


class NewsletterForm(forms.Form):
    """
    Form for newsletters subscription
    """
    email = forms.EmailField()
