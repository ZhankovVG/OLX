from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class CategoryOutput:
    # Вывод категорий
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categoryes'] = Category.objects.all()
        return context


class ProductView(CategoryOutput, ListView):
    # Вывод товара
    model = Product
    queryset = Product.objects.filter(draft=False)


class ProductDatailView(DetailView):
    # полное описание товара
    model = Product
    slug_field = 'url'
