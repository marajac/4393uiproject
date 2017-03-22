from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Product


def catalog(request):
    product_list = Product.objects.all()
    context = {'list': product_list}
    template = 'products/products.html'
    return render(request, template, context)


def product(request, slug):
    item = get_object_or_404(Product, slug=slug)
    context = {'item': item}
    template = 'products/item.html'
    return render(request, template, context)


'''class ListView(generic.ListView):
    model = Product
    template = 'products/products.html'


class ProductView(generic.DetailView):
    model = Product
    template = 'products/products.html'''
