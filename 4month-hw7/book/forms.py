from django import forms
from . import models


class BooksForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.RatingBook
        fields = '__all__'