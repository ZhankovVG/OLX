from .models import *
from django.forms import ModelForm
from django import forms


class AddNewPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'poster', 'category', 'url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'users': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class AddComentsForm(forms.ModelForm):
    class Meta:
        app_label = 'django_comments_xtd'
        model = Comments
        fields = ['name', 'text', 'email']