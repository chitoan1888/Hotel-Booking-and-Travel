from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re
from .models import Register_tables

class RegistrationForm(forms.Form):
    username = forms.CharField(label=None, max_length=30)
    # first_name = forms.CharField(label=None, max_length=150)
    email = forms.EmailField(label='')
    password1 = forms.CharField(label='', widget=forms.PasswordInput())
    password2 = forms.CharField(label='', widget=forms.PasswordInput())

    def clean_password2 (self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("ten Tai khoan da ton tai")
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])


# class EditProfile (UserChangeForm):
class EditProfile (ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'last_name',
            'first_name', 
            'email', 
        )

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
    