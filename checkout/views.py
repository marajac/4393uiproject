from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.cart import Cart

#from .forms import CheckoutForm

@login_required
def checkout(request):
#    form = CheckoutForm(request.POST or None)
#    confirm_message = None

#    if form.is_valid():
#        r_name = form.cleaned_data['r_name']
#        s_address = form.cleaned_data['s_address']
#        b_address = form.cleaned_data['b_address']
#        card_num = form.cleaned_data['card_num']
#        card_exp_month = form.cleaned_data['card_exp_month']
#       card_exp_year = form.cleaned_data['card_exp_year']
#        form = None

#    context = {'form': form, 'confirm_message': confirm_message, }
    context = {}
    template = 'checkout.html'
    return render(request, template, context)


def summary(request):
    cart = Cart(request)
    context = {'cart': cart}
    template = 'summary.html'
    return render(request, template, context)
