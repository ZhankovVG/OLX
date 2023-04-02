from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class ProductView(ListView):
    model = Product
    queryset = Product.objects.filter(draft = False)