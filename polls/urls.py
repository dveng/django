from django.urls import path

from polls import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),
    # url(r'^sss$', views.index),
    # url(r'^$', views.index),
    # url(r'^search-form$', search.search_form),
    # url(r'^search$', search.search),
    # url(r'^search-post$', search2.search_post),
]
