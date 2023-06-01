from django.urls import path

from polls import views

app_name = "polls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # path('', views.index, name='index'),
    # url(r'^sss$', views.index),
    # url(r'^$', views.index),
    # url(r'^search-form$', search.search_form),
    # url(r'^search$', search.search),
    # url(r'^search-post$', search2.search_post),

    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
