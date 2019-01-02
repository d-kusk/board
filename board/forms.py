from django import forms
from .models import Board, BoardComment


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("title", "content")


class CommentForm(forms.ModelForm):
    class Meta:
        model = BoardComment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'card w-100'})
        }
