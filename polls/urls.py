from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views, search,search2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path('', views.index, name='index'),
    #url(r'^sss$', views.index),
    url(r'^$', views.index),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
