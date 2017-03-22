from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    # ex: /products/
    url(r'^$', views.ProductView.as_view(), name='index'),
    # ex: /products/5/
    url(r'^(?P<pk>[0-9]+)/$', views.ProductView.as_view(), name='detail'),
]
