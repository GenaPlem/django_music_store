from django import forms
from .models import Product
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    Form to add products as admin
    """

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 15}),

        }

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)
