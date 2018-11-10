from django import forms
from .models import Board


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("title", "content")
