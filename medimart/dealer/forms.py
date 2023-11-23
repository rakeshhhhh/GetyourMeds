from django import forms
from django.forms import fields, widgets
from .models import *

class MedForm(forms.ModelForm):
    class Meta:
        model = MedicineTable
        exclude = ['dealer']
        widgets = {
            'code' :  forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'name' :  forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'mf_name' :  forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'price' :  forms.NumberInput(
                attrs={'class':'form-control'}
            ),
            'image' :  forms.FileInput(
                attrs={'class':'form-control'}
            ),
            'status' :  forms.Select(
                attrs={'class':'form-control'}
            ),
        }