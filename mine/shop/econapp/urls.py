from django.conf.urls import url
from econapp.views import (first_page,
                           dellivery,
                           installment,
                            login_view,
                            logout_view,
                            index,
                           )

urlpatterns = [
    url(r'^account/', index, name='account'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^dellivery/', dellivery, name='dellivery'),
    url(r'^installment/$', installment, name='installment'),
    url(r'^$', first_page, name='base'),
]