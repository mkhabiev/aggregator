from django.forms import ModelForm
from django import forms
from films.models import Comment, Film, TVShow


class CommentForm(forms.ModelForm):
    film = forms.ModelChoiceField(disabled=True, required=False, queryset=Film.objects.all())

    class Meta:
        model = Comment
        fields = [
            'film',
            'comment',
        ]

class CommentsForm(forms.ModelForm):
    show = forms.ModelChoiceField(disabled=True, required=False, queryset=TVShow.objects.all())

    class Meta:
        model = Comment
        fields = [
            'show',
            'comment',
        ]