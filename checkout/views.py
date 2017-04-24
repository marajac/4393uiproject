from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


@login_required
def checkout(request):
    context = {}
    template = 'checkout.html'
    return render(request, template, context)


def summary(request):
    context = {}
    template = 'summary.html'
    return render(request, template, context)

