from django.db import models


# Create your models here.
class summary(models.Model):
    r_name = models.CharField(max_length=120, default="")   # Receiver's name
    s_address = models.CharField(max_length=120, default="")    # Shipping address
    b_address = models.CharField(max_length=120, default="")    # Billing address
    s_type = models.CharField(max_length=120, default="")   # might change
    p_type = models.CharField(max_length=120, default="")   # might change
    card_name = models.CharField(max_length=120, default="")    # Card Owner's name
    card_num = models.CharField(max_length=16, default="")  # Card number
    card_exp_month = models.CharField(max_length=2, default="")  # Card Exp month
    card_exp_year = models.CharField(max_length=2, default="")  # Card Exp year

    def get_r_name(self):
        return self.r_name

    def get_s_address(self):
        return self.s_address

    def get_b_address(self):
        return self.b_address

    def get_s_type(self):
        return self.s_type

    def get_p_type(self):
        return self.p_type

    def get_card_name(self):
        return self.card_name

    def get_card_num(self):
        return self.card_num

    def get_card_exp_month(self):
        return self.card_exp_month

    def get_card_exp_year(self):
        return self.card_exp_year
