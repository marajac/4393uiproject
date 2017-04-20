from django.conf.urls import url

from . import views


app_name = 'products'
urlpatterns = [
    # ex: /products/
    url(r'^$', views.catalog, name='index'),
    url(r'^search/$', views.search, name='search'),
    # ex: /products/5/
    url(r'^(?P<slug>[-\w]+)/$', views.product, name='detail'),
]