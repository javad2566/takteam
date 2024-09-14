# forms.py
from django import forms
from .models import User


class UserImageForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['image']