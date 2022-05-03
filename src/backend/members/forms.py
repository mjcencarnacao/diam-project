from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    fields = ('username', 'password')


class SignUpForm(UserCreationForm):
    class Meta:
        model = User

        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        )
        password1 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control"
                }
            )
        )

        password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    "class": "form-control"
                }
            )
        )

        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
