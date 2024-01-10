from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone_number',
                  'address1', 'address2', 'city',
                  'county', 'postal_code']

    def __init__(self, *args, **kwargs):
        """
        Add autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs['autofocus'] = True
