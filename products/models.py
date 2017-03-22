from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(decimal_places=2, max_digits=6, default=0.00)
    product_description = models.TextField(default='Item description here')

    def __str__(self):
        return self.product_name

