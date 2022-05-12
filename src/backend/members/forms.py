from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from home.models import Comments
from django.forms import ModelForm


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


class Profile(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'profile_pic', 'is_premium_user')
        help_texts = {
            'username': None,
        }


class SignUpForm(UserCreationForm):
    class Meta:
        model = User

        first_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        )

        last_name = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            )
        )

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

        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

        widgets = {
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }
