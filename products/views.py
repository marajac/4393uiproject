from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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


def search(request):
    if request.method == 'GET':  # this will be GET now
        item_name = request.GET['search']  # do some research what it does
        #return HttpResponse(item_name)
        try:
            status = Product.objects.filter(name__icontains=item_name)
        except Product.DoesNotExist:
            status = None
        return render(request, 'products/search.html', {'result': status})
    else:
        return render(request, 'products/search.html', {})


'''class ListView(generic.ListView):
    model = Product
    template = 'products/products.html'


class ProductView(generic.DetailView):
    model = Product
    template = 'products/products.html'''
