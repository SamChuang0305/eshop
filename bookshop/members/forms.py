
from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={
                                   'name': 'username',
                                   'placeholder': 'Username',
                                   'required': True,
                                   'autofocus': True,
                                   'class': 'form-control'}))

    password = forms.CharField(label='Password', max_length=30,
                               widget=forms.PasswordInput(attrs={
                                   'name': 'password',
                                   'placeholder': 'Password',
                                   'class': 'form-control'}))
