from django import forms
from .models import Post


class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'category',
           'author'
       ]


class ArticlesForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'title',
           'text',
           'category',
           'author'
       ]