from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def checkout(request):
    context = {}
    template = 'checkout.html'
    return render(request, template, context)
