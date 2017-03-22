from django.shortcuts import render
from django.views import generic
from .models import Product


class ProductView(generic.DetailView):
    model = Product
    template = 'products/products.html'
