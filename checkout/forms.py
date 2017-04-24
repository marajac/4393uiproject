from django import forms


class CheckoutForm(forms.Form):
    r_name = forms.CharField(required=True, max_length=100)
    s_address = forms.CharField(required=True, max_length=100)
    b_address = forms.CharField(required=True, max_length=100)
    card_num = forms.IntegerField()
    card_exp_month = forms.IntegerField()
    card_exp_year = forms.IntegerField()
