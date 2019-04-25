
from .models import MyUser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'password']
        labels = {
            'email': 'email',
            "password": "password"
        }


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    is_student = forms.CharField(max_length=1)
    class Meta:
        model = MyUser
        fields = ('email', 'is_student', 'username', 'password1', 'password2')

class ChangePasswardForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['password']
        labels = {
            "password": "New"
        }
