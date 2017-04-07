from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from products import models


def home(request):
    product_list = models.Product.objects.all()
    context = {'list': product_list}
    template = 'home.html'
    return render(request, template, context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request, template, context)


@login_required
def user_profile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)

