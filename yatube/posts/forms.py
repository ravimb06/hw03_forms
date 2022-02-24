from tokenize import group
from attr import fields
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('text', 'group')
