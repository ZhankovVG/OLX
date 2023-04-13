from .models import Product
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