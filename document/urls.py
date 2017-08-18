from django.conf.urls import url

from document import views

urlpatterns = [
    url('^$', views.HomeView.as_view(), name="home"),
    url('^article/create/$', views.ArticleCreateView.as_view(), name="article_create"),
]
