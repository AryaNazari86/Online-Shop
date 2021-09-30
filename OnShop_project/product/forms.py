from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price','phone_number', 'city', 'image')

        labels = {
            'name': '',
            'description': '',
            'price': '',
            'phone_number': '',
            'city': '',
            'image': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Product Description...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Products Price...'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product City...'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': ''})
        }
