from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'about', 'city', 'password', 'image')

        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'about': '',
            'city': '',
            'password': '',
            'image': ''
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
