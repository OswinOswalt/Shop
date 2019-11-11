from django.conf.urls import url
from econapp.views import (first_page,
                           category_view,
                           product_view,
                           dellivery,
                           installment,
                           cart_view,
                           add_to_cart_view,
                           remove_from_cart_view,
                            checkout_view,
                            order_create_view
                           )

urlpatterns = [
    url(r'^dellivery/', dellivery, name='dellivery'),
    url(r'^installment/$', installment, name='installment'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product'),
    url(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', add_to_cart_view, name= 'add_to_cart'),
    url(r'^remove_from_cart/(?P<product_slug>[-\w]+)/$', remove_from_cart_view, name = "remove_from_cart"),
    url(r'^cart/$', cart_view, name ="cart"),
    url(r'^checkout/$', checkout_view, name = 'checkout'),
    url(r'^order/$', order_create_view, name = 'create_order'),
    url(r'^$', first_page, name='base'),
]