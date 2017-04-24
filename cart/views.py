# views.py
from cart.cart import Cart
from products.models import Product
from django.shortcuts import render_to_response, render


def add_to_cart(request, product_id, quantity):
    quantity = Product.quantity
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.add(product, product.price_in_dollars, quantity=1)
    template = 'cart.html'
    context = {'cart': cart}
    return render(request, template, context)


def remove_from_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)
    template = 'cart.html'
    context = {'cart': cart}
    return render(request, template, context)


def get_cart(request):
    cart = Cart(request)
    template = 'cart.html'
    context = {'cart': cart}
    return render(request, template, context)
