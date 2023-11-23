from django import forms
from django.forms import fields, widgets
from .models import *

class CommonRegForm(forms.ModelForm):
    """Form definition for CustomerReg."""

    class Meta:
        """Meta definition for CustomerRegform."""

        model = CommonTable
        fields = ('first_name','last_name','email','phone','city','place','pin_code','username','password',)
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'class':'form-control'}
            ),
            'phone': forms.NumberInput(
                attrs={'class':'form-control','value':''}
            ),
            'city': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'place': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'pin_code': forms.NumberInput(
                attrs={'class':'form-control'}
            ),
            'username': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'password': forms.PasswordInput(
                attrs={'class':'form-control'}
            ),
        }
        help_texts = {'username':None}

class TimeInput(forms.TimeInput):
    input_type = 'time'

class ShopRegForm(forms.ModelForm):
    """Form definition for ShopReg."""

    class Meta:
        """Meta definition for ShopRegform."""

        model = ShopTable
        exclude = ('shop',)
        widgets = {
            'name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'latitude': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'longitude': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'open_on': TimeInput(
                attrs={'class':'form-control'}
            ),
            'closed_on': TimeInput(
                attrs={'class':'form-control'}
            ),
        }


