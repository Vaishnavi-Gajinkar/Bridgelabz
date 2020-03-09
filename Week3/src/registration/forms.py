from django import forms
from .models import *

class registration_form(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    last_name =  forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    emailID =  forms.EmailField(widget=forms.TextInput(), required=True, max_length=100)
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    class Meta();
        model = register
        fields = ['first_name','last_name','emailID','password','confirm_password']