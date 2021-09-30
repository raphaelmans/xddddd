from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name','address','birthdate','mobile_number')

class DVDForm(forms.ModelForm):
    class Meta:
        model = DVD
        fields = '__all__'
