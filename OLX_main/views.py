from django.shortcuts import render, get_object_or_404
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


class SearchView(CategoryOutput, ListView):
    # поиск по сайту
    def get_queryset(self):
        query = self.request.GET.get('search')
        queryset = Product.objects.filter(title__icontains=query)
        return queryset


class CategoryView(CategoryOutput, ListView):
    # вывод товар по категории
    model = Product
    template_name = 'OLX_main/product_list.html'

    def get_queryset(self):
        category = get_object_or_404(Category, url=self.kwargs['slug'])
        return Product.objects.filter(category=category, draft=False)
