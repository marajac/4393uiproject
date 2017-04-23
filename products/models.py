from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag', blank=True)
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'catalog_category', (), {'category_slug': self.slug}


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created from name.', null=True)
    brand = models.CharField(max_length=50, default='', blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    price_in_dollars = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    old_price = models.DecimalField(max_digits=9, decimal_places=2,
                                    blank=True, default=0.00)
    photo = models.ImageField(upload_to='product_photo', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    quantity = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for meta tag', null=True
                                     , blank=True)
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/%s/" % self.slug
        # return '/products/', {'product_slug': self.slug}

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None


'''class ProductDetail(models.Model):
    """The ``ProductDetail`` model represents information unique to a
    specific product. This is a generic design that can be used
    to extend the information contained in the ``Product`` model with
    specific, extra details."""
    product = models.ForeignKey('Product', related_name='details')
    attribute = models.ForeignKey('ProductAttribute')
    value = models.CharField(max_length=500)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s: %s - %s' % (self.product, self.attribute, self.value)


class ProductAttribute(models.Model):
    """The "ProductAttribute" model represents a class of feature found
    across a set of products. It does not store any data values
    related to the attribute, but only describes what kind of a
    product feature we are trying to capture. Possible attributes
    include things such as materials, colors, sizes, and many, many
    more."""
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return u'%s' % self.name'''
