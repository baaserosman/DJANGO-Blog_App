from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username','password1','password2','profile_pic')


class ProfileUpdateForm(forms.ModelForm):

    class Meta():
        model = User
        fields = ("username", "bio", "profile_pic")